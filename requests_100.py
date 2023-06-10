import contextlib
import time
from blacksheep.client import ClientSession
import aiohttp
import asyncio
from requests_futures import sessions

URL = "http://httpbin.org/delay/3"
TIMES = 100


@contextlib.contextmanager
def report_time(test):
    t0 = time.perf_counter()
    yield
    print("Время на выполнение с помощью `%s': %.2fs"
          % (test, time.perf_counter() - t0))


async def get_aiohttp(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            await response.read()


async def client_blacksheep(url):
    async with ClientSession() as client:
        await client.get(url)


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    with report_time("aiohttp"):
        loop.run_until_complete(
            asyncio.gather(*[get_aiohttp(URL) for i in range(TIMES)]))

    session = sessions.FuturesSession(max_workers=TIMES)
    with report_time("FuturesSession w/ max workers"):
        futures = [session.get(URL) for i in range(TIMES)]
        for f in futures:
            f.result()

    loop = asyncio.get_event_loop()
    with report_time("blacksheep"):
        loop.run_until_complete(
            asyncio.gather(*[client_blacksheep(URL) for i in range(TIMES)]))
