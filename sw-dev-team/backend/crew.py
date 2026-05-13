

from crewai import Agent, Task, Crew
from llm_config import get_llm
import time

llm = get_llm()


backend_agent = Agent(
    role="Backend Developer",
    goal="Create minimal FastAPI backend",
    backstory="Expert in writing short and efficient backend APIs",
    llm=llm,
    verbose=True
)


frontend_agent = Agent(
    role="Frontend Developer",
    goal="Create minimal React UI",
    backstory="Expert in building clean UI with minimal code",
    llm=llm,
    verbose=True
)


def run_crew(user_prompt):
    try:
       
        task_backend = Task(
            description=f"""
            Build backend for: {user_prompt}

            Rules:
            - Use FastAPI
            - Max 120 lines
            - Keep code minimal
            - Include 2-3 endpoints only
            """,
            expected_output="Minimal FastAPI code",
            agent=backend_agent
        )

        time.sleep(6)  

       
        task_frontend = Task(
            description=f"""
            Build frontend for: {user_prompt}

            Rules:
            - Use React
            - Max 120 lines
            - Simple UI only
            - Call backend endpoints (assume /chat API)

            Keep everything short and clean.
            """,
            expected_output="Minimal React code",
            agent=frontend_agent
        )

        crew = Crew(
            agents=[backend_agent, frontend_agent],
            tasks=[task_backend, task_frontend],
            verbose=True
        )

        result = crew.kickoff()
        backend_output = ""
        frontend_output = ""

        try:
            backend_output = str(result.tasks_output[0])
            frontend_output = str(result.tasks_output[1])
        except:
            backend_output = "Backend generation failed"
            frontend_output = "Frontend generation failed"

        return {
            "backend": backend_output,
            "frontend": frontend_output
        }

    except Exception as e:
        
        if "Rate limit" in str(e):
            print(" Rate limit hit, retrying...")
            time.sleep(15)
            return run_crew(user_prompt)
        return str(e)

