import os
import json
import string
import random
from uuid import uuid4
from pprint import pprint
from datetime import datetime
from config import (
    string_range, 
    nats_subject,
    folder_use    
    )


def check_folder(folder:str=folder_use) -> None:
    """
    Function which is about checking folders
    Input:  folder = string values of it
    Output: we created folder if we have to
    """
    os.path.exists(folder) or os.mkdir(folder)

def get_date_current() -> str:
    """
    Function which is about getting current datetime for the files
    Input:  None
    Output: we created string values of the current situations
    """
    return datetime.utcnow().strftime("%Y-%m-%d-%H-%M")

def get_file_name_json(value_input:bool=True) -> str:
    """
    Function which is dedicated to get file name of the selected json
    Input:  value_input = check values of the json
    Output: string with the selected to get name
    """
    if value_input:
        return f"received_{nats_subject}_{get_date_current()}.json"
    return f"merged_{nats_subject}.json"

def develop_file_writes(callback_received:bytes) -> None:
    """
    Function which is dedicated to writed the file presence
    Input:  callback_received = bytes which were previously sent
    Output: we created or appended values to the file
    """
    check_folder(folder_use)
    value_file = os.path.join(folder_use, get_file_name_json())
    if os.path.exists(value_file):
        with open(value_file, 'r') as file_write:
            value_use = json.load(file_write)
        value_use.append(json.loads(callback_received))
    else:
        value_use = [json.loads(callback_received)]
    with open(value_file, 'w') as file_write:
        json.dump(
            value_use, 
            file_write,
            indent=4
        )

def develop_random_data(index:int=0) -> dict:
    """
    Function which is about the usage of the random data
    Input:  None
    Output: dictionary with the selected values of the random data
    """
    return json.dumps(
        {
            "index": index,
            "uuid": str(uuid4()),
            "name_person": ''.join(random.choice(string.ascii_lowercase) for _ in range(string_range)),
            "date_created": datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')
        }
    )

def develop_callback(message:object) -> None:
    """
    Function which is about to add the values to the callback
    Input:  message = received values of it
    Output: we dealed with the previous 
    """
    develop_file_writes(message.payload)
    print('Received Index: ', json.loads(message.payload).get('index', -1))
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

def merge_callback_result() -> None:
    """
    Function which is dedicated to use value
    Input:  None
    Output: we created the values of the merged dataframe
    """
    list_merged, value_use = [], []
    for file in os.listdir(folder_use):
        if file == get_file_name_json(False):
            list_merged.append(file)
        elif f"received_{nats_subject}" in file:
            list_merged.append(file)
    for f in list_merged:
        with open(os.path.join(folder_use, f), 'r') as read:
            value_use.extend(json.load(read))
    with open(os.path.join(folder_use, get_file_name_json(False)), 'w') as file_write:
        json.dump(
            value_use, 
            file_write,
            indent=4
        )
    for f in list_merged:
        if f != get_file_name_json(False):
            os.remove(
                os.path.join(
                    folder_use, 
                    f
                )
            )