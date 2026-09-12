import httpx
from model import ChatReponse,ChatRequest
from dotenv import load_dotenv
import os
import streamlit as st
load_dotenv()

class ClientApiService:
    def __init__(self):
        self.base_url = os.getenv("base_url")
        if not self.base_url:
            self.base_url = st.secrets["base_url"]
    
    def call_chat_api(self,message:str)->str:
        url = self.base_url + "/chat_google_bot"
        payload = {"message":message}
        response =  httpx.post(url,json = payload, timeout=30.0,)
        response.raise_for_status()
        return ChatReponse(**response.json())

    def chat_bot(self,message:str)->ChatReponse:
        try:
            response =  self.call_chat_api(message)
            return response
        except httpx.ConnectError:
            print("run uvicorn to run the api in local")
        except httpx.HTTPStatusError as error:
            print(f"status error {error.response.status_code}")
        return ChatReponse(message= "error occured", exit = True)

        

