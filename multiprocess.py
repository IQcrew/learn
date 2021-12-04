from multiprocessing.context import Process
import os
import time



def x1():
    y = 1
    while y < 100000000:
        y += 1

def x2():
    y = 1
    while y < 100000000:
        y += 1
def x3():
    y = 1
    while y < 100000000:
        y += 1
def x4():
    y = 1
    while y < 100000000:
        y += 1
def x5():
    y = 1
    while y < 100000000:
        y += 1
def x6():
    y = 1
    while y < 100000000:
        y += 1

def x7():
    y = 1
    while y < 100000000:
        y += 1

def x8():
    y = 1
    while y < 100000000:
        y += 1


def xdx():
    z = 1
    while z < 100000000:
        z += 1


if __name__ == "__main__":
    
    num_threads = os.cpu_count()
    processes = [
        Process(target=x1),
        Process(target=x2),
        Process(target=x3),
        Process(target=x4),
        Process(target=x5),
        Process(target=x6),
        Process(target=x7),
        Process(target=x8)
    ]

    start = time.time()

    for proces in processes:
        proces.start()
    for proces in processes:
        proces.join()
    end = time.time()
    print(end-start)



    start2 = time.time()
    
    x1(),
    x2(),
    x3(),
    x4(),
    x5(),
    x6(),
    x7(),
    x8()

    end2 = time.time()
    print(end2-start2)