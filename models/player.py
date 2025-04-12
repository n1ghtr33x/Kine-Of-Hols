from pydantic import BaseModel

class PlayerData(BaseModel):
    player_name: str
    password: str
