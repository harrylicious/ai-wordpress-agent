from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crew_logic import create_crew
import os
import requests
from dotenv import load_dotenv

load_dotenv()
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Initialize FastAPI app
app = FastAPI()

# Define a request model
class TopicRequest(BaseModel):
    topic: str
    language_code: str

# Define the API endpoint
@app.post("/run-crew")
async def run_crew(request: TopicRequest):
    try:
        # Create and execute the CrewAI process
        crew = create_crew(request.topic, request.language_code)
        result = crew.kickoff(inputs={"topic": request.topic, "language_code": request.language_code})
        
        return {"status": "success", "result": result}
    except Exception as e:
        print(f"Error: {str(e)}")  # Debugging
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")