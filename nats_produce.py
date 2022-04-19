import time
from pynats import NATSClient
from data_develop import develop_random_data
from config import (
    index_begin,
    index_end,
    nats_subject
)


with NATSClient() as client:
    client.connect()

    for i in range(index_begin, index_end):
        client.publish(
            subject=nats_subject, 
            payload=develop_random_data(i)
        )
        time.sleep(0.01)
        print(f'Sent Index: ', i)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')