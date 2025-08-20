import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import tool, create_react_agent, AgentExecutor
from langchain_community.tools import DuckDuckGoSearchRun
from langchain import hub

# Load the .env file
load_dotenv()
# Set the Google API key for the LangChain library
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# 1. Initialize the LLM (Gemini Pro)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", 
                             temperature=0, 
                             convert_system_message_to_human=True)

# 2. Define the tools the agent can use
search = DuckDuckGoSearchRun()

@tool
def math_calculator(query: str) -> str:
    """A simple calculator to evaluate mathematical expressions."""
    try:
        return eval(query)
    except Exception as e:
        return f"Error: {e}"

tools = [search, math_calculator]

# 3. Create the agent
prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Function to be called from our Django view
def run_agent(query):
    """Runs the agent and returns the output."""
    response = agent_executor.invoke({"input": query})
    return response['output']