from crewai import Agent
from llm_config import get_llm

qa_agent = Agent(
    role="QA Tester",
    goal="Test application thoroughly and identify bugs",
    backstory="Expert in writing unit tests, integration tests, and ensuring software reliability",
    llm=get_llm(),
    verbose=True
)