import time
import aiohttp
import asyncio

async def fetch_url(session, url):
    print(f"Начинаю качать {url}")
    async with session.get(url) as response:
        text = await response.text()
        print(f"Закончил: {url}, размер: {len(text)} байт")
        return len(text)

async def main():
    urls = [
        "https://yandex.ru",
        "https://google.com",
        "https://github.com"
    ]

    async with aiohttp.ClientSession() as session:
        task = [fetch_url(session, url) for url in urls]
        result = await asyncio.gather(*task)
        print(f"Всего байт: {sum(result)}")

asyncio.run(main())