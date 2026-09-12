from pydantic import BaseModel

class ChatReponse(BaseModel):
    message:str
    role:str =  "Assistant"
    exit:bool = False

class ChatRequest(BaseModel):
    message:str
    role:str = "User"
    