from model import ChatRequest,ChatReponse
from chat_bot_history import ChatBotHistory

class GeneratePrompt:

    def generate_chatbot_prompt(self,chat_request: ChatRequest,chat_history)->str:
        prompt = " Role:system \n message: You are an assistant \n"
        for chat in chat_history:
            prompt += f"role: {chat["role"]}\n message: {chat["message"]}\n"
        prompt += f"role: user \n message:{chat_request.message} \n"
        print("test")
        print(prompt)
        return prompt