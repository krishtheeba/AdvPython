import time
from threading import Thread

class Box(Thread):
	def __init__(self,a1):
		Thread.__init__(self)
		self.name=a1
		print(f"Im Box thread:{a1}")
		
	def run(self):
		for v in range(10):
			print(f"Hello...{self.name}")
			#time.sleep(0.1)


for v in range(5000):
	th=Box("Thread"+str(v))
	th.start()


for v in range(10):
	print("This is main thread section")


for v in range(5000):
	th.join()

print("Exit from Main thread")


		
