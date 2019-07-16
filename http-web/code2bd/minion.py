import json
import time
import socket
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


# async def hello(uri):
#    async with websockets.connect(uri) as ws:
#        await ws.send("Hello from {}".format(socket.gethostname()))

name = "test"


async def main(uri):

    msg = {
        "mid": name,
        "msg": "hello",
        "hostname": ""
    }

    async with websockets.connect(uri) as ws:
        try:
            msg['hostname'] = socket.gethostname()
            while True:
                await ws.send(json.dumps(msg))
                time.sleep(10)
        except ConnectionClosed as e:
            print("Gru died")
            exit(-1)


asyncio.get_event_loop().run_until_complete(main('ws://localhost:8000/ws'))
# asyncio.get_event_loop().run_forever(main('ws://localhost:8000/ws'))
asyncio.get_event_loop().run_forever()
