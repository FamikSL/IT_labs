from threading import Thread, BoundedSemaphore
from time import sleep, time
import random
ticket_office = BoundedSemaphore(value=3)
def ticket_buyer(number):
   start_service = time()
   with ticket_office:       
       sleep(1 + random.random())       
       print(f"Клиент {number}, Время_обслуживания: {time() - start_service}")
buyer = [Thread(target=ticket_buyer, args=(i,)) for i in range(9)]
for b in buyer:
   b.start()