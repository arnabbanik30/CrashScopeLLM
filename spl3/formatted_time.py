from datetime import datetime

def get_formatted_time():

    current_time = datetime.now()
    formatted_time = current_time.strftime("%m-%d %H:%M:%S")

    return formatted_time

