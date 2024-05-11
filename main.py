from pydantic import Field
from instructor import OpenAISchema
from openai import OpenAI
from groq import Groq
from utils import get_completion

class GetWeather(OpenAISchema):
    """
    Determine weather in a location

    ## Limitations
    - Only returns temperature in fahrenheit
    - Hardcoded to return the same value every time
    """
    location: str = Field(..., description="The city and state e.g. San Francisco, CA")

    def run(self):
      return(f"Rainy, 48 degrees fahrenheit in {self.location}")

class GetDirections(OpenAISchema):
    """
    Get driving directions from one city to another.

    ## Limitations
    - Distances are only given in miles
    - Hardcoded to return the same value every time
    """
    from_city: str = Field(..., description="The name of the departure city")
    to_city: str = Field(..., description="The name of the destination city")

    def run(self):
      return(f"Drive north to get from {self.from_city} to {self.to_city}")

tool_functions = [GetWeather, GetDirections]

messages=[
    {"role": "system", "content": "You answer questions - short and sweet."},
    {"role": "user", "content": "What's the weather in NYC and how do I get there from Florida?"},
]

print(get_completion(messages.copy(), tool_functions, OpenAI(), "gpt-4-turbo") + "\n")
print(get_completion(messages.copy(), tool_functions, Groq(), "llama3-70b-8192") + "\n")

