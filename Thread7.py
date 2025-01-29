from threading import Thread

class Box(Thread):
	def __init__(self,a1):
		Thread.__init__(self)
		self.name=a1
		print(f"Im Box thread:{a1}")
		
	def run(self):
		print(f"Hello...{self.name}")


for v in range(1,60):
	th=Box("Thread"+str(v))
	th.start()


for v in range(5):
	print("This is main thread section")


print("Exit from Main thread")


		
