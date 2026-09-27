import asyncio

async def print_text(word):
    print(f"Начало обработки {word}")
    await asyncio.sleep(2) 
    print(f"Конец обработки {word}")
    return word

async def main():
    words = [
        "Я",
        "Жарю",
        "Шашлык"
    ]
    
    texts = [print_text(word) for word in words]
    print(texts)
    results = await asyncio.gather(*texts)
    print(results)

asyncio.run(main())