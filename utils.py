from datetime import datetime

def cur_time():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")
