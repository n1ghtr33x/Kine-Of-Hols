from fastapi import FastAPI
from db.database import Database
from routes.rest import router as rest_router
from routes.websocket import websocket_endpoint
from config import get_settings

settings = get_settings()

app = FastAPI()
db = Database(settings.DATABASE_URL)

app.include_router(rest_router)

@app.websocket("/ws")
async def websocket_route(websocket):
    await websocket_endpoint(websocket, db)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
