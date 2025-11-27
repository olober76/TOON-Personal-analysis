import json

from fastapi import APIRouter, HTTPException, Response, Body


generateAIResponse = APIRouter(prefix="generate")

@generateAIResponse.post("/")
async def generate_ai_response(
    request: Response_Body = Body(...)
):
    try:
        # Simulate AI response generation logic - INI CUMAN  KERANGKA
        ai_response = {
            "message": "This is a simulated AI response based on the input.",
            "input_received": request.input_data
        }
        return ai_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))