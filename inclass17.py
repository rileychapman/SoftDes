import pygame
import time
class AnimatedCircle(object):
    """ Reperesents a circle that can draw itself to a pygame window. """
    def __init__(self, center_x, center_y, v_x, v_y, radius):
        """ Initialize the Circle object.
        
            center_x: the x-coordinate of the center of the circle
            center_y: the y-coordinate of the center of the circle
            v_x: the x-velocity of the circle
            v_y: the y-velocity of the circle
            radius: the radius of the circle
        """
        self.center_x = center_x
        self.center_y = center_y
        self.v_x = v_x
        self.v_y = v_y
        self.radius = radius
    
    def draw(self,screen):
        """ Draw the Circle to the screen.
        
            screen: the pygame screen to draw to
        """
        pygame.draw.circle(screen, pygame.Color(0,0,0), (self.center_x,self.center_y), self.radius, 1)

    def animate(self):
        """ Update the position of the circle """
        self.x += self.v_x
        self.y += self.v_y

if __name__ == '__main__':
    pygame.init()
    size = (640,480)
    screen = pygame.display.set_mode(size)

    circ = AnimatedCircle(100,100, 0, 0, 20)
    running = True
    while running:
        screen.fill(pygame.Color(255,255,255))
        circ.draw(screen)

        for event in pygame.event.get():
            if event.type == 'QUIT':
                running = False
        time.sleep(.01)
        pygame.display.update()

    pygame.quit()




