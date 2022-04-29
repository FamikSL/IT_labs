from copy import copy
from threading import Thread, Lock
import threading
from time import sleep
mutex = Lock()
resource = 1

def Add_one(N, thread_safe):
    global resource
    if thread_safe:
        mutex.acquire()
    try:
        thread_id = threading.get_ident()

        for i in range(N):
            resource += 1
            sleep(0.5)
        print('\nProcessing data:', resource, "ThreadId:", thread_id)
    finally:
        if thread_safe:
            mutex.release()

def Multp(N, thread_safe):
    global resource
    if thread_safe:
        mutex.acquire()
    try:
        thread_id = threading.get_ident()
        for i in range(N):
            resource *= 2
            sleep(0.5)
        print('\nProcessing data:', resource, "ThreadId:", thread_id)
    finally:
        if thread_safe:
            mutex.release()
thread_safe = False
N =5
thread2 = threading.Thread(target = Multp, args=(N,thread_safe))
thread1 = threading.Thread(target = Add_one, args=(N,thread_safe))


thread1.start()
thread2.start()
thread1.join()
thread2.join()