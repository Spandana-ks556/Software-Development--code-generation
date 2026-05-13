from crewai import Agent
from llm_config import get_llm

pm_agent = Agent(
    role="Product Manager",
    goal="Define clear and detailed software requirements",
    backstory="Experienced in writing PRDs, user stories, and product roadmaps",
    llm=get_llm(),
    verbose=True
)