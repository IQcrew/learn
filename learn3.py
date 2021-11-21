from typing import Text
import pygame,sys,random,threading,os
from pygame.locals import *
pygame.init()

#icon find
icon_2D = pygame.image.load(os.path.join("Assets/icon_2D.png"))
loading_1 = pygame.image.load(os.path.join("Assets/loading_1.png"))
loading_2 = pygame.image.load(os.path.join("Assets/loading_2.png"))
loading_3 = pygame.image.load(os.path.join("Assets/loading_3.png"))
loading_4 = pygame.image.load(os.path.join("Assets/loading_4.png"))
loading_imgs = [loading_1,loading_2,loading_3,loading_4]

#things
screen = (500,500)

#colors
white=(255, 255, 255)
black=(0,0,0)

#set
window_size = (500,500)
color_fill=(white)
FPS = 60

#screen
pygame.display.set_caption('2D_ONEGE')
screen_1 = pygame.display.set_mode((screen),0,64)
clock = pygame.time.Clock()

#icon use
pygame.display.set_icon(icon_2D)

#print imagine
def imagine(imagine_draw,position):
    screen_1.blit(imagine_draw,(position))
    pygame.display.flip()
    pygame.display.update() 

#loading animation
def loading():
    
    for i in range(15):
        screen_1.fill(color_fill)
        screen_1.blit(icon_2D,(186,100))
        for img in len(loading_imgs):
            imagine(loading_imgs[img],(70,250))
        

#window draw
def window_draw():
    loading()
    pygame.display.update()

#camera move
def camera_move():
    scroll_1 = 0

#repead screane + quit if press QUIT button or f on kayboard
def main():
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == K_f:
                sys.exit()
        window_draw()
        camera_move()


#check name and start def
if __name__ == "main":
    main()