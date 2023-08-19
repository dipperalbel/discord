import time
from lock import *
from json_functions import *
from datetime import datetime

second=60
minute=1*second
hour=60*minute
total_time=6*hour
max_amount=1440

def check_data_file():
    global total_time
    lock=GlobalLocks().global_lock
    print(lock)
    while True:
        with lock:
            premium_dict=load_user_data(target_file='data_ninjatrader.json')
            trials_to_check = []
            current_datetime = datetime.now()
            for key, nested_dict in premium_dict.items():
                if 'isTrial' in nested_dict and nested_dict['isTrial']:
                    trials_to_check.append(key)
            if len(trials_to_check)>0:
                for i in trials_to_check:
                    temp_dict=premium_dict[i]
                    temp_date=temp_dict['timestamp']
                    temp_datetime = datetime.strptime(temp_date, "%Y-%m-%d %H:%M:%S")
                    time_difference = current_datetime - temp_datetime
                    total_minutes = time_difference.total_seconds() / 60
                    if total_minutes>=max_amount:
                        temp_dict['isValid']=False
                        premium_dict[i]=temp_dict
            save_user_data(premium_dict,target_file='data_ninjatrader.json')        
        time.sleep(total_time)  