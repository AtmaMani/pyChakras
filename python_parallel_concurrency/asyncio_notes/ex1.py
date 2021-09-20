import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:
            html = await response.text()
            print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())