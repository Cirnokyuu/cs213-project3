import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

def plot_time_data():
    postgres_data = {
        50000: 42,
        40000: 31,
        30000: 24,
        20000: 17,
        10000: 7
    }
    
    openGauss_data = {
        50000: 70,
        40000: 55,
        30000: 33,
        20000: 23,
        10000: 10
    }
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(list(postgres_data.keys()), list(postgres_data.values()), label="postgres", color="tab:blue")
    
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
    postgres_data = {
        50000: (18.92, 5.00),
        40000: (17.53, 5.00),
        30000: (19.19, 4.90),
        20000: (17.01, 4.90),
        10000: (20.54, 4.90)
    }
    
    openGauss_data = {
        50000: (30.31, 21.60),
        40000: (30.83, 21.40),
        30000: (38.18, 21.40),
        20000: (36.53, 21.80),
        10000: (37.22, 21.80)
    }
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(list(postgres_data.keys()), [x[0] for x in postgres_data.values()], label="postgres CPU", color="tab:blue")
    plt.plot(list(postgres_data.keys()), [x[1] for x in postgres_data.values()], label="postgres MEM", color="tab:blue", linestyle="--")
    
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
