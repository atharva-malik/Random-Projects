# DESKTOP NOTIFICATIONS!!!
import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title="Time to take a drink of water NOW!",
            app_name="Drinking Notification",
            message="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
           # app_icon="C:\\Atharva\\ICONS\\DRINKING_NOTIFICATION_ICON.ico",
           # timeout=10,
           # toast=True,
        )
        print("done once")
        time.sleep(60*60)
