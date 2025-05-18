from plyer import notification
import schedule
import time
import threading

def notify_me():
    notification.notify(
        title="Reminder",
        message="Time to stretch and relax!",
        app_name="Healthy Notifier",
        app_icon="icon.ico",  # Replace with your actual .ico file path
        timeout=10
    )

def schedule_notifications():
    # Notify every 30 minutes
    schedule.every(30).minutes.do(notify_me)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    # Run scheduler in a separate thread to avoid blocking
    notifier_thread = threading.Thread(target=schedule_notifications)
    notifier_thread.start()
