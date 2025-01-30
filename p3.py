# asynchronous approach
import asyncio

async def f1():
	print("Hi")
	await asyncio.sleep(1)#time.sleep(1)
	print("Two")

async def main():
	await asyncio.gather(f1(),f1(),f1(),f1(),f1(),f1(),f1(),f1(),f1(),f1())

if __name__ == '__main__':
	import time
	start = time.perf_counter()
	asyncio.run(main())
	elapsed = time.perf_counter() - start
	print(f" Executed in {elapsed:0.2f} seconds")

