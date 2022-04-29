from threading import Barrier, Thread
from time import sleep, time
br = Barrier(3)
store = []
start_time = time()
def f1(x):
   store.append(x**2)
   sleep(0.5)
   print(f"Поставка_1 в сорт. центр: {x**2} ({time() - start_time })")
   br.wait()
def f2(x):
   store.append(x*2)
   sleep(2)
   print(f"Поставка_2 в сорт. центр: {x*2} ({time() - start_time })")
   br.wait()
Thread(target=f1, args=(3,)).start()
Thread(target=f2, args=(3,)).start()
br.wait()
print("Поставка из сорт. центра: ", sum(store),({time() - start_time }))