from crewai import Agent
from crewai.llm import LLM
from utils.llm_client import LLMClient
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os
load_dotenv()

openrouter_llm = LLM(
    model="openrouter/nvidia/llama-3.1-nemotron-ultra-253b-v1:free",  # e.g., "gpt-3.5-turbo" or "meta/llama-3-8b-instruct"
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


use_case_generator = Agent(
    role="AI Use Case Strategist",
    goal="""
Research current and emerging industry trends within {company}'s domain, identifying cutting-edge applications of AI and ML that could provide competitive advantages. 

For each use case you propose:
- Provide a clear title and short description.
- Explain how this use case will benefit the company in terms of operations, customer experience, efficiency, revenue, or competitive positioning.
- Outline a basic step-by-step approach the company could take to implement the use case (e.g., tools, teams involved, rough stages).
- Provide credible references or sources where applicable.

Focus on innovative, practical use cases tailored to the company's strategic areas and goals.
""",
    backstory="""
With expertise in GenAI, AI, and ML, you excel at translating technological advancements into practical, transformative business solutions. 
You bridge the gap between innovation and application, recommending use cases that drive tangible value and meet emerging market demands.
""",
    verbose=True,
    llm = openrouter_llm, 
    tools=[SerperDevTool()]
)
