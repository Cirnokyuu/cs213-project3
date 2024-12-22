import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline

# 读取数据函数
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
    spline = make_interp_spline(x, y, k=3)  # 使用三次样条插值来平滑数据
    x_new = np.linspace(min(x), max(x), 500)  # 生成更多的插值点
    y_new = spline(x_new)
    return x_new, y_new

def plot_data(time_data, cpu_data, mem_data):
    # 将时间数据从文件中的起始时间调整为 0
    start_time = time_data[0]
    time_data = [t - start_time for t in time_data]

    # 平滑 CPU 和 MEM 数据
    time_smooth, cpu_smooth = smooth_data(time_data, cpu_data)
    _, mem_smooth = smooth_data(time_data, mem_data)

    plt.figure(figsize=(10, 6))

    # 绘制 CPU 和 MEM 曲线
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

# 主程序
file_path = 'log_1w.txt'  # 这里填写 log.txt 文件路径
time_data, cpu_data, mem_data = read_log_data(file_path)
plot_data(time_data, cpu_data, mem_data)

# postgresql
# 数据总量 运行时间 平均CPU使用率 平均MEM使用率
# 50000 42 18.92% 5.00%
# 40000 31 17.53% 5.00%
# 30000 24 19.19% 4.90%
# 20000 17 17.01% 4.90%
# 10000 7 20.54% 4.90%