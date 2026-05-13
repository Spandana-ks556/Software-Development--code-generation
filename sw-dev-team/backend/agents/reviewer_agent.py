from crewai import Agent
from llm_config import get_llm

reviewer_agent = Agent(
    role="Code Reviewer",
    goal="Review and improve code quality",
    backstory="Senior engineer ensuring clean, efficient, and maintainable code",
    llm=get_llm(),
    verbose=True
)