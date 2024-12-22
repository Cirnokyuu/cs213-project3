import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline

def read_log_data(file_path):
    time_data = []
    cpu_data = []
    mem_data = []
    
    with open(file_path, 'r') as file:
        for line in file:
            time_str, rest = line.split(" : ")
            cpu_str = rest.split(",")[0].strip()
            mem_str = rest.split(",")[1].strip()

            time_parts = time_str.split(":")
            total_seconds = int(time_parts[0]) * 3600 + int(time_parts[1]) * 60 + int(time_parts[2])
            time_data.append(total_seconds)
            
            cpu_percentage = float(cpu_str.split()[1].strip('%'))
            mem_percentage = float(mem_str.split()[1].strip('%'))
            cpu_data.append(cpu_percentage)
            mem_data.append(mem_percentage)
    
    return time_data, cpu_data, mem_data

def smooth_data(x, y):
    spline = make_interp_spline(x, y, k=3) 
    x_new = np.linspace(min(x), max(x), 500)
    y_new = spline(x_new)
    return x_new, y_new

def plot_data(time_data, cpu_data, mem_data):
    start_time = time_data[0]
    time_data = [t - start_time for t in time_data]

    time_smooth, cpu_smooth = smooth_data(time_data, cpu_data)
    _, mem_smooth = smooth_data(time_data, mem_data)

    plt.figure(figsize=(10, 6))

    plt.plot(time_smooth, cpu_smooth, label="CPU Usage (%)", color="tab:blue")
    plt.plot(time_smooth, mem_smooth, label="MEM Usage (%)", color="tab:orange")
    
    plt.title("CPU and MEM Usage of postgres")
    plt.xlabel("Time (s)")
    plt.ylabel("Percentage (%)")
    
    plt.ylim(0, 100)
    plt.xlim(0, time_data[-1])

    print(time_data[-1])
    print("average CPU usage: {:.2f}%".format(np.mean(cpu_data)))
    print("average MEM usage: {:.2f}%".format(np.mean(mem_data)))
    
    plt.legend(loc="upper left")
    plt.grid(True)
    plt.show()

file_path = 'log_1w.txt' 
time_data, cpu_data, mem_data = read_log_data(file_path)
plot_data(time_data, cpu_data, mem_data)
