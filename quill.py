from multiprocessing import Process

def f():
    print("hello world")

for n in range(100):
    p = Process(target=f)
    p.start()
