from fastapi import WebSocket
from utils.id_generator import generate_unique_id

async def websocket_endpoint(websocket: WebSocket, db):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received: {data}")

            if data == "Hello":
                await websocket.send_json({"type": "version", "data": "0.0.1"})

            elif data.startswith("register|"):
                parts = data.split("|")
                if len(parts) != 3:
                    await websocket.send_json({"type": "error", "data": "Invalid request"})
                    continue

                name, password = parts[1], parts[2]
                await db.init_db()
                user_id = await generate_unique_id(db)
                result = await db.add_user(name, password, user_id)

                if result == "user added":
                    await websocket.send_json({"type": "user_data", "id": user_id, "player_name": name})
                elif result == "user exists":
                    await websocket.send_json({"type": "exists", "player_name": name})
                else:
                    await websocket.send_json({"type": "error", "data": "DB error"})
            else:
                await websocket.send_json({"type": "error", "data": "Invalid request"})
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await websocket.close()
