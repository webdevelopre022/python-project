#YouTube channel 5starcoder
#subscribe my channel 
#project_12
import tkinter as tk
from time import strftime

# Create main window
root = tk.Tk()
root.title("Digital Clock with Date")
root.geometry("400x150")
root.resizable(False, False)
root.configure(bg="black")

# Time Label
time_label = tk.Label(root, font=("Arial", 40, "bold"), bg="black", fg="cyan")
time_label.pack(anchor="center")

# Date Label
date_label = tk.Label(root, font=("Arial", 20), bg="black", fg="white")
date_label.pack(anchor="center")

# Update function
def update():
    current_time = strftime('%H:%M:%S')
    current_date = strftime('%A, %d %B %Y')
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    root.after(1000, update)

# Start the update loop
update()
root.mainloop()
