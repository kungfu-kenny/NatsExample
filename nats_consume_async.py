import asyncio
from time import sleep
import nats
from config import (
    nats_url,
    nats_subject
)


async def main(loop):
    nc = await nats.connect(nats_url)
    async def message_handler(msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()
        print("Received a message on '{subject} {reply}': {data}".format(
            subject=subject, 
            reply=reply, data=data)
        )

    sub = await nc.subscribe(nats_subject, cb=message_handler)
    await sub.unsubscribe(limit=3000000)
    

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.run_forever()
    loop.close()