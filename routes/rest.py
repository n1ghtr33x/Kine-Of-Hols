from fastapi import APIRouter, HTTPException
from utils.hash_password import hash_password, verify_password
from models.player import PlayerData, LoginData
from db.database import Database
from config import get_settings
from utils.id_generator import generate_unique_id
from models.response import UserData, login_fail, login_success

# Получаем настройки
settings = get_settings()

# Передаем db_url в конструктор
db = Database(settings.DATABASE_URL)

router = APIRouter()

@router.get("/version")
async def get_version():
    return {"version": settings.VERSION}

@router.post("/register")
async def register_player(data: PlayerData):
    await db.init_db()
    player_id = await generate_unique_id(db)

    result = await db.add_user(data.player_name, await hash_password(data.password), player_id)
    if result == "user added":
        return {"status": "success", "user_data": {"id": player_id, "player_name": data.player_name}}
    elif result == "user exists":
        raise HTTPException(status_code=400, detail="User already exists")
    else:
        raise HTTPException(status_code=500, detail="Unknown error")

@router.post("/login")
async def login_player(data: LoginData):
    await db.init_db()
    user = await db.get_user(data.name)
    if user:
        if await verify_password(data.password, user.password):
            return await login_success(
                data = UserData(
                    id = user.id,
                    name = user.name,
                    elixir = user.elixir,
                    gold = user.money,
                    gems = user.gems
                )
            )
        else:
            return await login_fail(
                data="Incorrect password"
            )
    else:
        return await login_fail(
            data="Incorrect user"
        )
