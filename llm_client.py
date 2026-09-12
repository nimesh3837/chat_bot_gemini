from model import ChatReponse,ChatRequest
import os
from google import genai
from dotenv import load_dotenv
load_dotenv()
class LLMClient:
    def __init__(self):
        self.api_key = os.getenv("api_key")
        self.client = genai.Client(api_key=self.api_key) 

    def call_google_openai(self,prompt:str):
        reponse  =  self.client.models.generate_content(
            model = os.getenv("ai_model"),
            contents=prompt )

        # chat = self.client.chats.create(
        # model=os.getenv("ai_model"))
        # response = chat.send_message(prompt)  
        #another way to call this one rememebr teh chat history from llm side

        return ChatReponse(message=reponse.text)