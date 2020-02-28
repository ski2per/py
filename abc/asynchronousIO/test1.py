import asyncio

async def do_subprocess():
    print('Subprocess sleeping')
    proc = await asyncio.create_subprocess_exec('sleep', '5')
    returncode = await proc.wait()
    print('Subprocess done sleeping.  Return code = %d' % returncode)

async def sleep_report(number):
    for i in range(number + 1):
        print('Slept for %d seconds' % i)
        await asyncio.sleep(1)

loop = asyncio.get_event_loop()

tasks = [
    asyncio.ensure_future(do_subprocess()),
    asyncio.ensure_future(sleep_report(5)),
]

loop.run_until_complete(asyncio.gather(*tasks))
loop.close()