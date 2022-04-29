import os
if __name__ == "__main__":
    print("Пока всего один процесс")
pid = os.fork (); #Создание нового процесса
print("Уже два процесса")
if pid == 0:
	print("Это Дочерний процесс его pid =", os.getpid())
	print("А pid его Родительского процесса =", os.getppid())
elif pid > 0:
	print("Это Родительский процесс pid=", os.getpid())
else:
	print("Ошибка вызова fork, потомок не создан ")