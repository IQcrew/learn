from timeit import default_timer as timer
import random
value = 0.0
for i in range(100):
    start = timer()
    stop = timer()
    value += (start-stop)
print("cas1: ",value)

value = 0.0
for i in range(100):
    start = timer()
    stop = timer()
    value += (start-stop)
print("cas2: ",value)