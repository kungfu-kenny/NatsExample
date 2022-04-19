from pynats import NATSClient
from data_develop import develop_callback
from config import nats_subject 


with NATSClient() as client:
    
    client.connect()
    client.subscribe(subject=nats_subject, callback=develop_callback)
    client.wait()