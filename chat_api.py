from fastapi import FastAPI
from model import ChatReponse,ChatRequest
from api_service import Api_Service
from chat_bot_history import ChatBotHistory
from generate_prompt import GeneratePrompt
from llm_client import LLMClient

app = FastAPI(title = "zomato chat api", description="not required", version=1.0)
api_service = Api_Service()
@app.get("/health_chat",response_model=ChatReponse)
def chat_health_check()->None:
    return ChatReponse(message = "running")

@app.post("/chat_google_bot",response_model=ChatReponse)
def chat_google_bot(request_msg:ChatRequest)->ChatReponse:
  
    response = api_service.generate_reponse(request_msg)
    return response
