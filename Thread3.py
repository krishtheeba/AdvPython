import threading


class Box(threading.Thread):
	def __init__(self,name):
		threading.Thread.__init__(self) # super().__init__()
		self.name=name
	def run(self):
		print(f"Im {self.name} Thread")



print("MAIN THREAD STARTED")
obj1=Box("Thread1")
obj1.start()
print("EXIT FROM MAIN THREAD")