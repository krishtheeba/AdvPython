import time
import threading
from threading import Thread

def f1(i):
    print("Thread {} going to sleep for 3 seconds.".format(i))
    time.sleep(3)
    print("Thread {} is awake now.".format((threading.current_thread())))
    

for i in range(10):
    th = Thread(target=f1,args=(i,))
    #th.start()
    print("Current Thread count:{}".format(threading.active_count()))
