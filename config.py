import os

folder_current = os.getcwd()
folder_storage = 'storage'
folder_use = os.path.join(folder_current, folder_storage)

string_range = 30

index_begin, index_end = 1, 3001
nats_subject = 'test_subject'
