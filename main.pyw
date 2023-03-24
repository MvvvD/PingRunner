import requests
import schedule
import time


google = 'http://www.google.com'


with open('error_log.txt', 'a') as file:
    file.write(f'Start of the record --- {time.strftime("%Y-%m-%d / %H:%M:%S")}\n')

def pinger():
    try:
        requests.get(google).status_code
    except:
        error_log = f'Offline --- {time.strftime("%Y-%m-%d / %H:%M:%S")}\n'
        with open('error_log.txt', 'a') as file:
            file.write(error_log)
        time.sleep(15)
        pinger()
    
pinger()
schedule.every(5).minutes.do(pinger)
while True:
    schedule.run_pending()
    time.sleep(1)
