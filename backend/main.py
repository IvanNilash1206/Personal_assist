# backend/main.py
from fastapi import FastAPI

app = FastAPI(title="PulseAI Backend")

@app.get("/")
async def root():
    return {"message": "PulseAI backend is alive"}
