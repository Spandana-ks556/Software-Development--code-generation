from crewai import Agent
from llm_config import get_llm

frontend_agent = Agent(
    role="Frontend Developer",
    goal="Build responsive and modern React applications",
    backstory="Skilled in React, UI components, and frontend performance optimization",
    llm=get_llm(),
    verbose=True
)