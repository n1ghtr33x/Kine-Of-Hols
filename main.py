from fastapi import FastAPI
from db.database import Database
from routes.rest import router as rest_router
from config import get_settings

settings = get_settings()

app = FastAPI()
db = Database(settings.DATABASE_URL)

app.include_router(rest_router)


if __name__ == "__main__":
    import uvicorn
    if settings.DEBUG:
        uvicorn.run(app, host=settings.HOST, port=settings.PORT)
    else:
        uvicorn.run(app, host=settings.HOST, port=settings.PORT, log_level="error")
