from multiprocessing import Process
from threading import Thread
import os
num_threads = os.cpu_count()
print(num_threads)
m = []

o = True


y = 0

def prnt():
    while True:
        global y
        y += 1
        print(f"dudo je debil po {y}")

for i in range(num_threads):
    m.append(Process(target=prnt()))

for i in m:
    i.start()
    i.join()








