import os
import time
import threading

current_time = lambda : time.strftime("%H:%M:%S", time.localtime())

def threadFunc(i):
    id = threading.get_ident()
    pid = os.getpid()
    print(f'Это поток-{i} его id = {id}, pid = {pid}' )

if __name__ == '__main__':
    # первый доч процесс
    pid = os.fork()
    if pid == 0:
        flag = 1

    if pid > 0:
        # второй доч процесс
        flag = 2
        pid = os.fork()
    
    if pid > 0:
        print(f"Это Родительского процесса процесс его pid = {os.getpid()}. А pid его Родительского процесса = {os.getppid()}. Текущее время {current_time()}")
        os.system('ps -x')
    elif pid == 0:
        print(f"Это Дочерний процесс его pid = {os.getpid()}. А pid его Родительского процесса = {os.getppid()}. Текущее время {current_time()}")
        
        if flag == 1:
            os.system('pstree 0')
        elif flag == 2:
            for i in [1, 2, 3]:
                t = threading.Thread(target=threadFunc, args=(i,))
                t.start()
                t.join()
        