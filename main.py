from pydantic import Field
from instructor import OpenAISchema
from openai import OpenAI
from groq import Groq

def get_completion(messages, tool_functions, client, model):
    while True:
        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=[{"type": "function", "function": func.openai_schema} for func in tool_functions],
            tool_choice="auto",
            temperature=0.5,
            max_tokens=4096,
        )

        completion_message = completion.choices[0].message
        if completion_message.tool_calls is None:
            return(completion_message.content)
        else:
            messages.append(completion_message)
            for tool_call in completion_message.tool_calls:
                print(f"\033[90m🛠️ {tool_call.function.name} {tool_call.function.arguments}\033[0m")
                tool_result = execute_tool(tool_call, tool_functions)
                messages.append({
                    "tool_call_id": tool_call.id, 
                    "role": "tool", 
                    "name": tool_call.function.name, 
                    "content": tool_result,
                    })

def execute_tool(tool_call, funcs):
    # inspired by https://github.com/VRSEN/agency-swarm/threads/thread.py - original source?
    func = next(iter([func for func in funcs if func.__name__ == tool_call.function.name]))

    if not func:
        return f"Error: Function {tool_call.function.name} not found. Available functions: {[func.__name__ for func in funcs]}"
    try:
        func = func(**eval(tool_call.function.arguments))
        output = func.run()
        return output
    except Exception as e:
        return "Error: " + str(e)



class GetWeather(OpenAISchema):
    """
    Get the weather info.
    """
    city: str = Field(..., description="The name of the city")

    def run(self):
      return(f"Rainy, 10 degrees celsius")

class GetDirections(OpenAISchema):
    """
    Get driving directions from one city to another.
    """
    from_city: str = Field(..., description="The name of the departure city")
    to_city: str = Field(..., description="The name of the destination city")

    def run(self):
      return(f"Drive north.")

tool_functions = [GetWeather, GetDirections]

messages=[
    {"role": "system", "content": "You answer questions - short and sweet."},
    {"role": "user", "content": "What's the weather in NYC and how do I get there from Florida?"},
]

print(get_completion(messages.copy(), tool_functions, OpenAI(), "gpt-4-turbo") + "\n")
print(get_completion(messages.copy(), tool_functions, Groq(), "llama3-70b-8192") + "\n")

