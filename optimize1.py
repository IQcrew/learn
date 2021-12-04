import time
import pygame
import random
from multiprocessing import Process


background = pygame.image.load("background.png")
screen = pygame.display.set_mode((500,500))



x = []

for i in range(600):
    x.append({"x": random.randrange(500), "y" : random.randrange(500), "INFO" : "UP", "SKIN" : background})




start =  time.time()

for i in x:
    screen.blit(i["SKIN"],(i["x"],i["y"]))

stop = time.time()

print(stop-start, "   FOR")







x = []
for i in range(6000):
    x.append({"x": random.randrange(500), "y" : random.randrange(500), "INFO" : "UP", "SKIN" : background})

    
def read(list):
    return list



