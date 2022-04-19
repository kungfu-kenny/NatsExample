from pynats import NATSClient
from data_develop import develop_callback
from config import nats_subject, nats_url


with NATSClient(url=nats_url) as client:
    try:
        client.connect()
        client.subscribe(subject=nats_subject, callback=develop_callback)
        client.wait()
    except Exception as e:
        print("We faced error such as:", e)
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')