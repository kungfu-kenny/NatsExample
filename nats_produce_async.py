import asyncio
import nats
from time import sleep
from data_develop import develop_random_data
from config import (
    nats_url,
    nats_subject,
    index_end,
    index_begin
)


async def main():
    nc = await nats.connect(nats_url)
    for i in range(index_begin, index_end):
        await nc.publish(
            nats_subject, 
            develop_random_data(i)
        )
        sleep(0.02)
    await nc.flush()
    await nc.close()

if __name__ == '__main__':
    asyncio.run(main())