from dotenv import load_dotenv

load_dotenv()
from pprint import pprint
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from tavily import TavilyClient
from langchain_tavily import TavilySearch


# tavily = TavilyClient()
# @tool
# def search(query: str) -> str:
#     """"Tool that searches over internet
#     Args:
#         query: The query to search for
#     Returns:
#         The Search Result
#         """
#     print(f"searching for {query}")
#     #return "Berlin weather is rainy"
#     return tavily.search(query=query)

llm = ChatOllama(temperature=0, model="gpt-oss:20b")
#tools = [search]
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from agentic-ai-learning!")
    result = agent.invoke({"messages":HumanMessage(content="search for 3 job postings for an ai engineer in the Berlin Area on linkedIn and list their details")})
    pprint(result)


if __name__ == "__main__":
    main()
