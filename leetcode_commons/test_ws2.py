import asyncio
import websockets

async def receive_message():
    uri = "ws://localhost:8000/ws/2"
    async with websockets.connect(uri) as websocket:
        while True:
            msg = await websocket.recv()
            print(f"Received: {msg}")

asyncio.get_event_loop().run_until_complete(receive_message())