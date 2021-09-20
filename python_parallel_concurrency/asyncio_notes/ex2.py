import asyncio
import aiohttp
from timer import timer

url = 'https://betterprogramming.pub/asynchronous-programming-in-python-for-making-more-api-calls-faster-419a1d2ee058'


async def read_page(session, i):
    async with session.get(url) as resp:
        r = resp.text
        print(i, end=" ")


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [read_page(session, i) for i in range(1,11)]
        await asyncio.gather(*tasks)


@timer(1, 1)
def func():
    asyncio.run(main())
    print("\nTime in secs: ", end=" ")

