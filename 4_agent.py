import os
import requests
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.prebuilt import create_react_agent

# Load env variables
load_dotenv()

# Optional: LangSmith project
os.environ["LANGCHAIN_PROJECT"] = "ReAct Agent"

# LLM
llm = ChatOpenAI()

# Tools
search_tool = DuckDuckGoSearchRun()

@tool
def get_weather_data(city: str) -> str:
    """
    Fetch current weather data for a given city
    """
    url = f'https://api.weatherstack.com/current?access_key=f07d9636974c4120025fadf60678771b&query={city}'
    response = requests.get(url)
    return str(response.json())

tools = [search_tool, get_weather_data]

# ✅ Create agent (LangGraph way)
agent = create_react_agent(llm, tools)

# ✅ Invoke (NEW FORMAT)
response = agent.invoke({
    "messages": [("user", "What is the current temp of Gurgaon?")]
})

print(response)