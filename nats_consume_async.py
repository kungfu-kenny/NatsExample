import nats
import asyncio
from time import sleep
from nats_produce_async import develop_publish
from data_develop import develop_callback_async
from config import (
    nats_url,
    nats_subject
)


async def main(loop):
    nc = await nats.connect(nats_url)
    sub = await nc.subscribe(
        nats_subject, 
        cb=develop_callback_async
    )

    await sub.unsubscribe(limit=3000000)
    await develop_publish(nc)
    await nc.drain()
    

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    # loop.run_forever()
    loop.close()