from model import ChatRequest,ChatReponse
from chat_bot_history import ChatBotHistory
from generate_prompt import GeneratePrompt
from llm_client import LLMClient

class Api_Service:
    def __init__(self,chat_bot_history=ChatBotHistory(),
                 generate_prompt=GeneratePrompt(),
                 llm_client=LLMClient()):
        self.chat_bot_history =  chat_bot_history
        self.generate_prompt = generate_prompt
        self.llm_client = llm_client

    def generate_reponse(self,chat_request:ChatRequest)-> ChatReponse:
        if chat_request.message.strip().lower() == "bye":
            self.chat_bot_history.remove_history()
            return ChatReponse(message="goodbye",exit=True)
        
        
        prompt = self.generate_prompt.generate_chatbot_prompt(chat_request,self.chat_bot_history.get_chat_bot_history())
        self.chat_bot_history.add_request(chat_request.message)
       
        response = self.llm_client.call_google_openai(prompt)
        self.chat_bot_history.add_response(response)
        return response