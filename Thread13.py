import threading

COUNT=0

class Box(threading.Thread):
	def __init__(self,name,c):
		threading.Thread.__init__(self)
		self.name=name
		self.c=c
	def run(self):
		print("Thread name:{}".format(self.name))
		threadLock.acquire()
		print("CriticalSection")
		threadLock.release()
		print(f"Exit from {self.name}")



threadLock = threading.Lock()
THREADS=[]
	
t1=Box("Thread-A",1)	
t2=Box("Thread-B",2)

# start new threads
t1.start()
t2.start()

# Add threads to THREADS list

THREADS.append(t1)
THREADS.append(t2)

# waiting for all threads to complete

for v in THREADS:
	v.join()

print("\nExit From Main Thread")