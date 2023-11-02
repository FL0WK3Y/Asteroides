import pygame 
from pygame import Vector2
import os
# this class creates the ship
class Ship:
    def __init__(self, position):
        self.position = Vector2(position)
        self.image= pygame.image.load('/Users/gregorirodriguez/Desktop/Games/Asteroids/images/ship.png')
    def update(self):
        pass
    def draw(self,screen):
        screen.blit(self.image,self.position)

# this class creates the Asteroid
class Asteroid:
    def __init__(self, position):
        self.position = Vector2(position)
        self.image= pygame.image.load('/Users/gregorirodriguez/Desktop/Games/Asteroids/images/asteroid1.png')
    def update(self):
        pass
    def draw(self,screen):
        screen.blit(self.image,self.position)

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Asteroides")

# this the background
background = pygame.image.load(os.path.join('/Users/gregorirodriguez/Desktop/Games/Asteroids/images/space.png'))


game_over = False
ship = Ship((100,100,))
asteroid = Asteroid((300,300))

# this is the while loop that runs throught the game 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    screen.blit(background, (0,0))
    # this updates the ship on the game window
    ship.update()
    ship.draw(screen)
    # this updates the asteroid on the game window
    asteroid.update()
    asteroid.draw(screen)
    pygame.display.update()
pygame.quit()
