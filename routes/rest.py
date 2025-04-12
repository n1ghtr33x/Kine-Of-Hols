from fastapi import APIRouter, HTTPException
from models.player import PlayerData
from db.database import Database
from config import get_settings
from utils.id_generator import generate_unique_id

# Получаем настройки
settings = get_settings()

# Передаем db_url в конструктор
db = Database(settings.DATABASE_URL)

router = APIRouter()

@router.get("/version")
async def get_version():
    return {"version": "0.0.1"}

@router.post("/register")
async def register_player(data: PlayerData):
    await db.init_db()
    player_id = await generate_unique_id(db)

    result = await db.add_user(data.player_name, data.password, player_id)
    if result == "user added":
        return {"status": "success", "user_data": {"id": player_id, "player_name": data.player_name}}
    elif result == "user exists":
        raise HTTPException(status_code=400, detail="User already exists")
    else:
        raise HTTPException(status_code=500, detail="Unknown error")
