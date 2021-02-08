from typing import List, Dict

from fastapi import FastAPI
from starlette.responses import HTMLResponse
from starlette.websockets import WebSocket, WebSocketDisconnect
import json
import time
app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Websocket</title>
    </head>
    <body>
        <h1>Messages Received</h1>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws/{0}");
            ws.onmessage = function(event) {{
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            }};

        </script>
    </body>
</html>"""

num = 2

@app.get("/")
async def get():
    global num
    num += 1
    return HTMLResponse(html.format(num))

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Notifier(metaclass=Singleton):
    def __init__(self):
        self.connections: Dict[WebSocket] = {}
        self.messenger = self.get_notification_generator()

    async def get_notification_generator(self):
        while True:
            message, id = yield
            await self._notify(message, id=id)

    async def push(self, id: int, msg: str):
        await self.messenger.asend([msg, id])

    async def push_all(self, msg: str):
        await self.messenger.asend([msg, None])

    async def connect(self, websocket: WebSocket, id):
        await websocket.accept()
        self.connections[id] = websocket

    def remove(self, websocket: WebSocket):
        self.connections[id] = None

    async def _notify(self, message: str, id = None):
        if id:
            await self.connections[id].send_text(message)
        else:
            living_connections = {}
            while len(self.connections) > 0:
                # Looping like this is necessary in case a disconnection is handled
                # during await websocket.send_text(message)
                id, websocket = self.connections.popitem()
                await websocket.send_text(message)
                living_connections[id] = websocket
            self.connections = living_connections


notifier = Notifier()


@app.websocket("/ws/{id}")
async def websocket_endpoint(websocket: WebSocket, id: int, state='default'):
    print(state)
    await notifier.connect(websocket, id)
    
    try:
        while True:
            data = await websocket.receive_json()
            print(type(data))
            print(data)
            await websocket.send_json({'hi':'123'})
            await websocket.close(code=1000)
            notifier.remove(websocket)    

    except WebSocketDisconnect:
        notifier.remove(websocket)


@app.get("/push/all/{message}")
async def push_to_connected_websockets(message: str):
    await notifier.push_all(f"! Push notification: {message} !")


@app.get("/push/{id}/{message}")
async def push_to_connected_websockets(id: int, message: str):
    await notifier.push(id, f"! Push notification: {message} !")

@app.on_event("startup")
async def startup():
    # Prime the push notification generator
    await notifier.messenger.asend(None)