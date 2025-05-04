from crewai import Agent
from utils.llm_client import LLMClient
from crewai_tools import SerperDevTool
from crewai.llm import LLM
from dotenv import load_dotenv
import os
load_dotenv()

openrouter_llm = LLM(
    model="openrouter/nvidia/llama-3.1-nemotron-ultra-253b-v1:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


industry_research_agent = Agent(
    role="Industry Research Specialist",
    goal="""
     Conduct a comprehensive analysis of the {company} industry sector to identify current market trends competitor strategies, and unique positioning opportunities for {company}. Focus on key offerings, recent advancements, strategic focus areas, and high-potential growth areas in the industry.
     
     Your response MUST be in the following JSON format:
     
     {
       "industry_analysis": {
         "market_trends": ["trend1", "trend2", "trend3"],
         "competitor_strategies": ["strategy1", "strategy2"],
         "unique_opportunities": ["opportunity1", "opportunity2"]
       }
     }
     """,
    backstory="""As an experienced industry analyst, you specialize in quickly assessing 
     the competitive landscape and identifying strategic opportunities. Your insights 
     are highly valuable for decision-makers aiming to enhance competitive positioning 
a     nd strategic alignment within the industry.""",
    verbose=True,
    tools=[SerperDevTool()],
    llm=openrouter_llm
)

