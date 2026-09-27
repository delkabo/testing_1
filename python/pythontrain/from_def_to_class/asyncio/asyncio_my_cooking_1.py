import asyncio
import time

async def create_egg():
    print ("Начинаю готовить яйца")
    await asyncio.sleep(5)
    print("завершаю готовить яйца")

async def create_salat():
    print("Начинаю готовить салат")
    await create_egg()
    await asyncio.sleep(3)
    print("Завершаю готовить салат")

async def main():
    start = time.time()
    # start_coockie_egg = asyncio.create_task(create_egg())
    await create_salat()
    # await start_coockie_egg
    print(f"Затраченное время: {time.time() - start:.1f} сек" )

asyncio.run(main())