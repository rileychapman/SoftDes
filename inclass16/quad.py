# -*- coding: utf-8 -*-
""" 
Created on Wed Mar 26 23:07:27 2014

@author: pruvolo is awesome! hi paul! :)
"""

import pygame
from pygame.locals import *
import time

class Quadrilateral(object):
    """ Represents a quadrilateral that can draw itself to a Pygame window """
    def __init__(self,x1,y1,x2,y2,x3,y3,x4,y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
      
    def draw(self,screen):
        pygame.draw.line(screen,pygame.Color(0,0,0),(self.x1,self.y1),(self.x2,self.y2))
        pygame.draw.line(screen,pygame.Color(0,0,0),(self.x2,self.y2),(self.x3,self.y3))
        pygame.draw.line(screen,pygame.Color(0,0,0),(self.x3,self.y3),(self.x4,self.y4))
        pygame.draw.line(screen,pygame.Color(0,0,0),(self.x4,self.y4),(self.x1,self.y1))

class Rectangle(Quadrilateral):
    def __init__(self,x_ul,y_ul,width,height):
        super(Rectangle, self).__init__(x_ul, y_ul, x_ul +width, y_ul, x_ul + width, y_ul+height, x_ul, y_ul+height)

class Square(Rectangle):
    def __init__(self,x_ul,y_ul,side):
        super(Square, self).__init__(x_ul,y_ul,x_ul +side, y_ul, x_ul + side, y_ul+side, x_ul, y_ul+side)


if __name__ == '__main__':
    pygame.init()

    size = (640,480)
    screen = pygame.display.set_mode(size)

    quad = Quadrilateral(100,100,200,90,200,300,100,300)
    rect = Rectangle(300,300,100,50)
    square = Square(100,300,100)
    running = True

    while running:
        screen.fill(pygame.Color(255,255,255))
        quad.draw(screen)
        rect.draw(screen)
        square.draw(screen)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        time.sleep(.01)
        pygame.display.update()

    pygame.quit()