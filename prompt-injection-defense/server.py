from fastapi import FastAPI
from pydantic import BaseModel
from inference import process_input

# Create FastAPI app
app = FastAPI()

# Request model
class InputData(BaseModel):
    text: str

# Root route (test if server works)
@app.get("/")
def home():
    return {"message": "🚀 Prompt Injection Defense Server is running!"}

# Main API endpoint
@app.post("/analyze")
def analyze(data: InputData):
    result = process_input(data.text)
    return result