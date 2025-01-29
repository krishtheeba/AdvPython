import threading
import time


def f1():
	print("Im f1 thread")
	for v in range(5):
		time.sleep(1)
	print("Exit From f1 thread")

def f2():
	print("Im f2 thread")
	for v in range(5):
		time.sleep(1)
	print("Exit From f2 thread")

print("\t*****Main thread*****")

t1=threading.Thread(target=f1)
t2=threading.Thread(target=f2)

t1.start()
print("\t*****After calling f1 thread*****")
t2.start()
print("\t*****After Calling f2 thread*****")
t1.join()
t2.join()
print("\t*****Exit from Main thread*****")