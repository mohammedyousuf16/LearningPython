import time
from plyer import notification

while True:
    print('please drink some water')
    notification.notify(
        title='Water Reminder',
        message='Please sip some water',
                        )
    time.sleep(5)