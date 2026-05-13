from fastapi import FastAPI
from crew import run_crew

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Dev Team API running "}

@app.post("/build")
def build_app(data: dict):
    prompt = data.get("prompt")
    result = run_crew(prompt)
    return result