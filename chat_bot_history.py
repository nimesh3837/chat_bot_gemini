class ChatBotHistory:
    def __init__(self):
        self.history = []

    def add_request(self,message):
        self.history.append({"role": "user","message" : message} )

    def add_response(self,message):
        self.history.append({"role": "assistant","message" : message} )

    def get_chat_bot_history(self):
        return self.history
    def remove_history(self):
        self.history= []