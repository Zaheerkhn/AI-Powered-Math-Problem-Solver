import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, LLMMathChain
from langchain.agents import AgentType, Tool, initialize_agent
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.callbacks import StreamlitCallbackHandler

# --- Page Config ---
st.set_page_config(page_title="Math Problem Solver", page_icon="🧮", layout="centered")

# --- Custom Styling ---
st.markdown(
    """
    <style>
        .stChatMessage { text-align: left; border-radius: 10px; padding: 10px; }
        .stButton>button { background-color: #4CAF50; color: white; border-radius: 5px; }
        .stTextArea>div>textarea { font-size: 16px; }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Title Section ---
st.title("AI-Powered Math Problem Solver")
st.subheader("Solving complex math problems with AI")

# --- Load Environment Variables ---
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "True"
os.environ["LANGCHAIN_PROJECT"] = "Math Problem Solver"
groq = os.getenv("GROQ_API_KEY")

# --- Load Model ---
llm = ChatGroq(groq_api_key=groq, model_name="Gemma2-9b-It", streaming=True)

# --- Define Tools ---
math_chain = LLMMathChain(llm=llm)
wikipedia_wrapper = WikipediaAPIWrapper()

wiki = Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description="A tool for searching information on various topics."
)

calculator = Tool(
    name="Calculator",
    func=math_chain.run,
    description="A tool for solving math-related questions with pure numerical expressions."
)

# --- Prompt for Reasoning ---
prompt = """ 
You are an AI that solves math problems step by step in a logical manner.
Provide a detailed explanation with a structured approach.
Question: {question}
"""
prompt_template = PromptTemplate(input_variables=["question"], template=prompt)

chain = LLMChain(llm=llm, prompt=prompt_template)

reasoning_tool = Tool(
    name="Reasoning Tool",
    func=chain.run,
    description="A tool for solving logical and reasoning-based math problems."
)

tools = [wiki, calculator, reasoning_tool]

# --- Initialize Agent ---
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)

# --- Chat Memory ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "Assistant", "content": "Hello! I can solve any math problem for you. What would you like me to solve today?"}]

# --- Display Chat Messages ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"].lower()):
        st.write(msg["content"])

# --- User Input ---
question = st.chat_input("Enter your math problem here...")

# --- Solve Button ---
if question:
    st.session_state.messages.append({"role": "User", "content": question})
    with st.chat_message("user"):
        st.write(question)

    with st.spinner("🤖 Solving your problem..."):
        st_sb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = agent.run(question, callbacks=[st_sb])
        st.session_state.messages.append({"role": "Assistant", "content": response})

    with st.chat_message("assistant"):
        st.write(response)
