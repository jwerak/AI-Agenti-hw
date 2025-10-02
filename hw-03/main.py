from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool, Tool

from langchain_community.utilities.wolfram_alpha import WolframAlphaAPIWrapper
from langchain_community.tools.wolfram_alpha.tool import WolframAlphaQueryRun
from langchain_experimental.utilities import PythonREPL
from langgraph.prebuilt import create_react_agent
from visualizer import visualize

load_dotenv()
wolfram = WolframAlphaQueryRun(api_wrapper=WolframAlphaAPIWrapper())

# Model
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found in environment variables. Please set it in your .env file."
    )

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)


@tool
def get_food() -> str:
    """Get a plate of spaghetti."""
    return "Here is your plate of spaghetti 🍝"


python_repl = PythonREPL()
repl_tool = Tool(
    name="python_repl",
    description="A Python shell. Use this to execute python commands. Input should be a valid python command. If you want to see the output of a value, you should print it out with `print(...)`.",
    func=python_repl.run,
)

tools = [get_food, repl_tool, wolfram]

# Agent
graph = create_react_agent(model=llm, tools=tools, prompt="You are a helpful assistant")

# Visualize the graph
visualize(graph, "graph.png")

# ---------------------------
# Run the graph
# MESSAGES are stored ONLY within the graph state !!!!
# EACH USER INPUT IS A NEW STATE !!!!
# =>  NO HISTORY for chat interaction !!!!!!
# ---------------------------
while True:
    user_input = input("User: ")
    if user_input.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break
    for event in graph.stream({"messages": ("user", user_input)}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)
