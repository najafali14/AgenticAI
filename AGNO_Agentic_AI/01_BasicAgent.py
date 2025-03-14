from agno.agent import Agent
from agno.models.google import Gemini

# create agent
agent = Agent(
    model=Gemini(
        id="gemini-2.0-flash",
        api_key="Your API_Key"
    ),
    markdown=True,
)
#print response
agent.print_response("tell me about python programming in 2 lines", stream=True)
