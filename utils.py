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


