from crewai import Agent
from llm_config import get_llm

backend_agent = Agent(
    role="Backend Developer",
    goal="Build scalable APIs using FastAPI",
    backstory="Expert backend engineer with strong knowledge of databases and API design",
    llm=get_llm(),
    verbose=True
)