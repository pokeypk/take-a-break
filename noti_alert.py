from plyer import notification
import time

def display_message():
    notification.notify(
        title="Short Break Alert",
        message="It's been 45 minutes. Don't forget to stretch a bit and go to the toilet.",
        timeout=10
)

time.sleep(11)

display_message()
