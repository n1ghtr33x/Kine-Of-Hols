from pydantic import BaseModel

class PlayerData(BaseModel):
    player_name: str
    password: str

class LoginData(BaseModel):
    name: str
    password: str

class SaveData(BaseModel):
    name: str
    password: str
    elixir: int
    gold: int
    gems: int