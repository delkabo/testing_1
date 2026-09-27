import asyncio

async def boil_water():
    print("Ставлю чайник на огонь")
    await asyncio.sleep(3)
    print("Вода закипела!")
    return "Кипяток"

async def make_tea():
    # Ждем кипятка
    water = await boil_water()
    print(f" Завариваю чай с {water}")
    await asyncio.sleep(1) # Чай настаивается
    print("Чай готов")

async def main():
    await make_tea()

asyncio.run(main())