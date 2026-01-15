import noti_alert 
import schedule
import time

def break_noti():
    schedule.every(45).minutes.do(noti_alert.display_message)

    print("Scheduled notification started.")
    while True:
        schedule.run_pending()
        time.sleep(5)
        
if __name__ == '__main__':
    break_noti()
