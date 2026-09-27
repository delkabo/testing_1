import asyncio
import time

async def boil_water():
    print("Ставлю чайник для супа")
    await asyncio.sleep(5) # Долго кипятится
    print("Кипяток для супа готов!")
    return "Кипяток"

async def make_cold_tea():
    print("Завариваю чай на холодной воде")
    await asyncio.sleep(2) # Чай насматривается по-своему
    print("Холодный чай готов!")

async def main():
    start = time.time()
    print(f"{start:.1f}")
    # Запускаем кипячение в фоне, НЕ ждём
    kettle_task = asyncio.create_task(boil_water())
    # kettle_task = boil_water()
    # А сами делаем холодный чай (он не требует кипятка)
    await make_cold_tea()

    # Чай готовб и тут вспоминаем про кипяток для супа
    print("Ах да, у меня же еще суп...")
    hot_water = await kettle_task # Ждём, если все еще не готово
    print(f"Добавляю {hot_water} в суп")
    print(f"Время: {time.time() - start:.1f} сек")

asyncio.run(main())