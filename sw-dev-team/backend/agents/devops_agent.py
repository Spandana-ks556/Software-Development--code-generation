from crewai import Agent
from llm_config import get_llm

devops_agent = Agent(
    role="DevOps Engineer",
    goal="Deploy and automate application using Docker and CI/CD",
    backstory="Expert in cloud deployment, containerization, and automation pipelines",
    llm=get_llm(),
    verbose=True
)