import asyncio
import websockets
import json
import time
async def receive_message():
    uri = "ws://localhost:8000/kiosk/ws/1?state=default"
    async with websockets.connect(uri) as websocket:
        while True:
            msg = await websocket.recv()
            asd = json.loads(msg)
            print(type(asd))
            print(f"Received: {asd}")
            

asyncio.get_event_loop().run_until_complete(receive_message())