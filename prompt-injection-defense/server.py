from fastapi import FastAPI
from inference import process_input

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Server working"}

@app.post("/analyze")
def analyze(data: dict):
    return process_input(data["text"])