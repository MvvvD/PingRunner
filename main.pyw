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
        print(error_log)
        with open('error_log.txt', 'a') as file:
            file.write(error_log)
    return response_code


schedule.every(1).minute.do(pinger)
while True:
    schedule.run_pending()
    time.sleep(1)
