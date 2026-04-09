from fastapi import FastAPI
from pydantic import BaseModel

# ✅ CORRECT IMPORT (after folder rename)
from prompt_injection_defense.inference import run_task

app = FastAPI()


# ✅ Request Schema
class InputData(BaseModel):
    task: str


# ✅ Health Check Route
@app.get("/")
def home():
    return {"message": "🚀 Server is running!"}


# ✅ Main API Route
@app.post("/run")
def run(data: InputData):
    try:
        result = run_task(data.task)
        return {
            "status": "success",
            "task": data.task,
            "result": result
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }