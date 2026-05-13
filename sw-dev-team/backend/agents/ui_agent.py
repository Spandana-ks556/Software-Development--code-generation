from crewai import Agent
from llm_config import get_llm

frontend_agent = Agent(
    role="UI/UX Designer",
    goal="Design intuitive and modern user interfaces",
    backstory="Expert in creating wireframes, UX flows, and visually appealing UI designs",
    llm=get_llm(),
    verbose=True
)