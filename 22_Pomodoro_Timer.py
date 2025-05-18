import time

def pomodoro_timer(work_minutes=25, break_minutes=5, cycles=4):
    for i in range(1, cycles + 1):
        print(f"\nCycle {i} - Work Time!")
        countdown(work_minutes * 60)

        print("Time for a short break!")
        countdown(break_minutes * 60)

    print("\nAll Pomodoro cycles completed! Great job!")

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_format = f'{mins:02d}:{secs:02d}'
        print(time_format, end='\r')
        time.sleep(1)
        seconds -= 1

if __name__ == "__main__":
    pomodoro_timer()
