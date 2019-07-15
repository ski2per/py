import socket
import asyncio
import websockets


async def hello(uri):
    async with websockets.connect(uri) as ws:
        await ws.send("Hello from {}".format(socket.gethostname()))


asyncio.get_event_loop().run_until_complete(hello('ws://localhost:8000/ws'))
asyncio.get_event_loop().run_forever()
