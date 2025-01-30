import asyncio

async def task():
	print("Hi..")
	await asyncio.sleep(1)
	print("Im Here")

asyncio.run(task())
