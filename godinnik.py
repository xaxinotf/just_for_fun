import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Цифровые Часы")

root.geometry("500x200")
root.resizable(False, False)
root.configure(background="black")

def update_time():
    current_time = strftime("%H:%M:%S %p")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

time_label = tk.Label(root, font=("Helvetica", 30, "bold"), background="black", foreground="#00FFCC")
time_label.pack(anchor="center", expand=True)

update_time()

root.mainloop()