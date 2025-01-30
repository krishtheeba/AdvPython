# synchronous approach
def f1():
	print("Hi")
	time.sleep(1)
	print("Two")

def main():
	for v in range(10):
		f1()

if __name__ == '__main__':
	import time
	start = time.perf_counter()
	main()
	elapsed = time.perf_counter() - start
	print(f" Executed in {elapsed:0.2f} seconds")

