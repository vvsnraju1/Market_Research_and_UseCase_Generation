from crewai import Crew, Process
from agents.research_agent import industry_research_agent
from agents.usecase_agent import use_case_generator
from agents.resource_agent import resource_collector_agent
from tasks.tasks import industry_research_task,use_case_generation_task,resource_collection_task

crew = Crew(
    agents=[industry_research_agent, use_case_generator, resource_collector_agent],
    tasks=[industry_research_task, use_case_generation_task, resource_collection_task],
    process=Process.sequential,
    verbose=True
)
    
def ask(question):
    global crew
    return crew.kickoff(inputs={'company':question})
