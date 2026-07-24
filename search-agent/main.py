from dotenv import load_dotenv

load_dotenv()
from pprint import pprint
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

@tool
def search(query: str) -> str:
    """"Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The Search Result
        """
    print(f"searching for {query}")
    return "Berlin weather is rainy"

llm = ChatOllama(temperature=0, model="gpt-oss:20b")
tools = [search]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from agentic-ai-learning!")
    result = agent.invoke({"messages":HumanMessage(content="What is the weather in Berlin?")})
    pprint(result)


if __name__ == "__main__":
    main()
