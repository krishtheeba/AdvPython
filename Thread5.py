import threading,time

class Box(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.count=0
	def run(self):
		self.count=10
		print(f'Count value:{self.count}')

	def f1(self):
		print(f"f1 thread:{self.count}")

obj=Box()
obj.start()
for var in range(500):
	time.sleep(1)
	obj.f1()


print("Exit from main thread")
