import os

folder_current = os.getcwd()
folder_storage = 'storage'
folder_plot = 'plot'
folder_use = os.path.join(folder_current, folder_storage)
folder_use_plot =  os.path.join(folder_current, folder_plot)

string_range = 30

index_begin, index_end = 1, 100001

nats_subject = 'test_subject_2'
nats_url = "nats://127.0.0.1:4222"

value_x = [
    100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,
    1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000,
]