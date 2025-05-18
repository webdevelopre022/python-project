import datetime
import time
from playsound import playsound

def alarm_clock(alarm_time, sound_file):
    print(f"Alarm set for {alarm_time}...")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("Wake up! Alarm time reached!")
            playsound(sound_file)
            break
        time.sleep(1)

# Example usage:
# Set time in 24-hour format: "HH:MM"
alarm_time = input("Enter alarm time (HH:MM, 24-hour format): ")
sound_file = "alarm_sound.mp3"  # Replace with your own sound file path
alarm_clock(alarm_time, sound_file)
