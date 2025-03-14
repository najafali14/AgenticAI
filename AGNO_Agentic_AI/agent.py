# install requirements
# !pip install agno
# !pip install -U duckduckgo-search

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
# Or using Vertex AI
agent = Agent(
    model=Gemini(
        id="gemini-2.0-flash",
        api_key="Gemini_API_Key",

    ),
    tools=[DuckDuckGoTools()], #tool calling
    markdown=True,
)

# Print the response in the terminal
agent.print_response("today news with date in pakistan", stream=True)
