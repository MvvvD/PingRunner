import requests
import schedule
import time

#test_code = 'https://httpstat.us/500'
google = 'http://www.google.com'


with open('error_log.txt', 'a') as file:
    file.write(f'Start of the record --- {time.strftime("%Y-%m-%d / %H:%M:%S")}\n')

def pinger():
    response_code = requests.get(google).status_code
    if response_code >= 400:
        error_log = f'Code: {response_code} --- {time.strftime("%Y-%m-%d / %H:%M:%S")}\n'
        with open('error_log.txt', 'a') as file:
            file.write(error_log)
        #checks again in 15 seconds if status code is >=400 to track more or less downtimes
        time.sleep(15)
        pinger()
    return response_code


schedule.every(1).minute.do(pinger)
while True:
    schedule.run_pending()
    time.sleep(1)
