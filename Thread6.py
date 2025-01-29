import threading

class Box(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.count=0
	def run(self):
		self.count=10
		print(f'Count value:{self.count}')

	def f1(self):
		print(f"f1 thread:{self.count}")

obj1=Box()
obj1.start()
obj1.f1()

obj2=Box()
obj2.start()
obj2.f1()

print("Exit from main thread")
