import urwid
import asyncio

async def snmp():
    print("Doing the snmp thing")
    await asyncio.sleep(1)

async def proxy():
    print("Doing the proxy thing")
    await asyncio.sleep(2)

async def main():
    while True:
        await snmp()
        await proxy()


loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
