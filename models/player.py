from pydantic import BaseModel

class PlayerData(BaseModel):
    player_name: str
    password: str

class LoginData(BaseModel):
    name: str
    password: str