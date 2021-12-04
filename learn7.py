import time
lst = [i for i in range(100000)]


start = time.time()
for i in lst:
    i + 1
stop = time.time()

print(stop-start)

start = time.time()
for i in range(len(lst)):
    lst[i] + 1
stop = time.time()

print(stop-start)