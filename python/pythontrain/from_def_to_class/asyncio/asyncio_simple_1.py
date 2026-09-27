import asyncio
import time

async def sleep_async(sec):
    print(f"Засыпаю на {sec} сек")
    await asyncio.sleep(sec)
    print("Проснулся")

async def main():
    task1 = asyncio.create_task(sleep_async(2))
    task2 = asyncio.create_task(sleep_async(2))

    await task1
    await task2

start = time.time()
asyncio.run(main())
print(f"Время: {time.time() - start:.1f} сек")