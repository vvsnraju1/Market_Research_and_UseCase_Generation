from crewai import Agent
from crewai_tools import SerperDevTool
from crewai.llm import LLM
from dotenv import load_dotenv
import os
load_dotenv()

openrouter_llm = LLM(
    model="openrouter/nvidia/llama-3.1-nemotron-ultra-253b-v1:free",  # e.g., "gpt-3.5-turbo" or "meta/llama-3-8b-instruct"
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


resource_collector_agent = Agent(
    role="AI Resource Curator",
    goal="""Analyze the list of AI/ML/GenAI use cases generated for {company}. 
    For each use case, search and identify high-quality, practical resources 
    such as relevant datasets, pre-trained models, open-source libraries, or 
    research papers. Focus on resources from trusted platforms like Kaggle, 
    HuggingFace, GitHub, or academic archives. Ensure that each resource is 
    actionable, industry-relevant, and can support the implementation of the 
    proposed use case. 
    Organize all findings into a clear markdown (.md) file, with clickable 
    links and brief descriptions for each resource.""",
    backstory="""You are an expert AI resource curator, skilled at sourcing the best 
    available datasets, models, and tools for applied machine learning projects. 
    Your mission is to bridge the gap between AI innovation and real-world execution 
    by providing developers and strategists with ready-to-use, high-quality assets.""",
    verbose=True,
    tools=[SerperDevTool()],  # Search tool to look up resources
    llm=openrouter_llm
)

