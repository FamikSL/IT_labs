import os
import time
import threading

current_time = lambda : time.strftime("%H:%M:%S", time.localtime())


if __name__ == '__main__':
    # первый доч процесс
    pid = os.fork()
 
    if pid > 0:
        # второй доч процесс
        pid = os.fork()
    
    if pid > 0:
        print(f"Это Род. процесса процесс его pid = {os.getpid()}. А pid его Родительского процесса = {os.getppid()}. Текущее время {current_time()}")
        os.system('ps -x')
    elif pid == 0:
        print(f"Это Дочерний процесс его pid = {os.getpid()}. А pid его Родительского процесса = {os.getppid()}. Текущее время {current_time()}")
        
        