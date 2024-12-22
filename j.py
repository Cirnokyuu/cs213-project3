import os
import time

pid = 2801
user = 'omm'
filename = 'log.txt'

def get_process_info(pid, user):
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
