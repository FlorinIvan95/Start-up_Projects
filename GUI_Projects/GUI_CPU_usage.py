import psutil
import time
import tkinter as tk
from tkinter import ttk


def update_cpu_usage():
    cpu_percent = psutil.cpu_percent(percpu=True)
    overall_percent = sum(cpu_percent) / len(cpu_percent)
    overall_progress.config(value=overall_percent)
    overall_label.config(text="Overall: {:.2f}%".format(overall_percent))
    for i in range(len(cpu_percent)):
        progress[i].config(value=cpu_percent[i])
        label[i].config(text="Core {}: {:.2f}%".format(i, cpu_percent[i]))
    root.after(1000, update_cpu_usage)


root = tk.Tk()
root.title("CPU Usage")

num_cores = psutil.cpu_count()

overall_frame = tk.Frame(root)
overall_frame.pack()

overall_progress = ttk.Progressbar(
    overall_frame, orient="horizontal", length=200, mode="determinate")
overall_progress.pack(side="left")

overall_label = tk.Label(overall_frame, text="")
overall_label.pack(side="left", padx=10)

progress = []
label = []

for i in range(num_cores):
    frame = tk.Frame(root)
    frame.pack()

    p = ttk.Progressbar(frame, orient="horizontal",
                        length=200, mode="determinate")
    p.pack(side="left")
    progress.append(p)

    l = tk.Label(frame, text="")
    l.pack(side="left", padx=10)
    label.append(l)

update_cpu_usage()
root.mainloop()
