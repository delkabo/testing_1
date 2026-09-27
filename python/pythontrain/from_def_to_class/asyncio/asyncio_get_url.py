# https://habr.com/ru/articles/958956/?ysclid=msz6cof2xa233193032
import asyncio
import aiohttp

async def fetch_url(session, url):
    print(f"начинаю качать {url}")
    async with session.get(url) as response:
         # await — ждем данные, но не блокируем других
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
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks) # Ждём все зaдaчи сразу
        print(f"Всего байт: {sum(results)}")

asyncio.run(main())

