import asyncio


async def hello():
    await asyncio.sleep(2)

    print("Hello Abdul")


asyncio.run(hello())