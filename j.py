# 当前环境linux
# 写一个 python 脚本，获取某进程每秒的 CPU 占用率，内存占用率
# 直接输出到终端，输出仅一行，包括时间
# 你需要保证你的输出与 linux 中 top 命令的输出一致
# 进程 pid 为 2801，user 为 omm，command 为 gaussdb

import os
import time

pid = 2801
user = 'omm'
filename = 'log.txt'

def get_process_info(pid, user):
    # 若有多个进程，则输出 cpu 与 mem 的总和
    # 你需要保证你的输出与 linux 中 top 命令的输出结果一致
    cmd = f"top -b -n 1 -u omm | grep 2801"
    res = os.popen(cmd).read().strip()
    res = res.split()
    time_info = time.strftime('%H:%M:%S', time.localtime())
    cpu = res[8]
    mem = res[9]
    return f'{time_info} : CPU {cpu}%, MEM {mem}%'

while True:
    info = get_process_info(pid, user)
    print(info)
    with open(filename, 'a') as f:
        f.write(info + '\n')
        time.sleep(1)
