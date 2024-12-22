# postgres 在不同数据集大小下的运行时间、CPU 和 MEM 使用率
# 数据总量 运行时间 平均CPU使用率 平均MEM使用率
# 50000 42 18.92% 5.00%
# 40000 31 17.53% 5.00%
# 30000 24 19.19% 4.90%
# 20000 17 17.01% 4.90%
# 10000 7 20.54% 4.90%

# openGauss 在不同数据集大小下的运行时间、CPU 和 MEM 使用率
# 数据总量 运行时间 平均CPU使用率 平均MEM使用率
# 50000 70 30.31% 21.60%
# 40000 55 30.83% 21.40%
# 30000 33 38.18% 21.40%
# 20000 23 36.53% 21.80%
# 10000 10 37.22% 21.80%

# 无需从文件读取，将以上数据绘制成为图表
# 第一幅图：postgres 与 openGauss 分别用不同的颜色表示，横坐标为数据总量，纵坐标为运行时间
# 第二幅图：postgres 与 openGauss 分别用不同的颜色表示，横坐标为数据总量，纵坐标为平均CPU使用率、平均MEM使用率（postgres 的cpu和mem两个指标用相近的颜色，opengauss 同理）
# 用平滑曲线连接数据点，横坐标的范围为 0 到 50000，其中 0-10000 没有数据点，需要以虚线表示

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

def plot_time_data():
    # postgres 数据
    postgres_data = {
        50000: 42,
        40000: 31,
        30000: 24,
        20000: 17,
        10000: 7
    }
    
    # openGauss 数据
    openGauss_data = {
        50000: 70,
        40000: 55,
        30000: 33,
        20000: 23,
        10000: 10
    }
    
    plt.figure(figsize=(10, 6))
    
    # 绘制 postgres 数据
    plt.plot(list(postgres_data.keys()), list(postgres_data.values()), label="postgres", color="tab:blue")
    
    # 绘制 openGauss 数据
    plt.plot(list(openGauss_data.keys()), list(openGauss_data.values()), label="openGauss", color="tab:orange")
    
    plt.title("INSERT Time")
    plt.xlabel("Data Size")
    plt.ylabel("Time (s)")
    
    plt.ylim(0, 100)
    plt.xlim(0, 50000)
    
    plt.legend(loc="upper right")
    plt.grid(True)
    plt.show()

def plot_usage_data():
    # postgres 数据
    postgres_data = {
        50000: (18.92, 5.00),
        40000: (17.53, 5.00),
        30000: (19.19, 4.90),
        20000: (17.01, 4.90),
        10000: (20.54, 4.90)
    }
    
    # openGauss 数据
    openGauss_data = {
        50000: (30.31, 21.60),
        40000: (30.83, 21.40),
        30000: (38.18, 21.40),
        20000: (36.53, 21.80),
        10000: (37.22, 21.80)
    }
    
    plt.figure(figsize=(10, 6))
    
    # 绘制 postgres 数据
    plt.plot(list(postgres_data.keys()), [x[0] for x in postgres_data.values()], label="postgres CPU", color="tab:blue")
    plt.plot(list(postgres_data.keys()), [x[1] for x in postgres_data.values()], label="postgres MEM", color="tab:blue", linestyle="--")
    
    # 绘制 openGauss 数据
    plt.plot(list(openGauss_data.keys()), [x[0] for x in openGauss_data.values()], label="openGauss CPU", color="tab:orange")
    plt.plot(list(openGauss_data.keys()), [x[1] for x in openGauss_data.values()], label="openGauss MEM", color="tab:orange", linestyle="--")
    
    plt.title("CPU and MEM Usage")
    plt.xlabel("Data Size")
    plt.ylabel("Percentage (%)")
    
    plt.ylim(0, 50)
    plt.xlim(0, 50000)
    
    plt.legend(loc="upper right")
    plt.grid(True)
    plt.show()

plot_time_data()

plot_usage_data()