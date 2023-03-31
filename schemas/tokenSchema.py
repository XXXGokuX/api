from pydantic import BaseModel

class tokenSchema(BaseModel):
    access_token:str
    token_type:str

class tokenDataSchema(BaseModel):
    id: int