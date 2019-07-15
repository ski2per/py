import time
import socket
import asyncio
import websockets


# async def hello(uri):
#    async with websockets.connect(uri) as ws:
#        await ws.send("Hello from {}".format(socket.gethostname()))

async def main(uri):
    async with websockets.connect(uri) as ws:
        while True:
            await ws.send("Hello from {}".format(socket.gethostname()))
            time.sleep(5)


# asyncio.get_event_loop().run_until_complete(main('ws://localhost:8000/ws'))
asyncio.get_event_loop().run_forever(main('ws://localhost:8000/ws'))
# asyncio.get_event_loop().run_forever()
