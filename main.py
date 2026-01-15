import noti_alert 
import schedule
import time

def break_noti():
    schedule.every(45).minutes.do(noti_alert.display)

    print("Scheduled notification started.")
    usrinp = input("Type 'E' to exit: ")
    
    while True:
        schedule.run_pending()
        time.sleep(5)
        if usrinp == 'E':
            break

if __name__ == '__main__':
    break_noti()
