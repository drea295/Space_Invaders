import pygame, sys
from spaceship import Spaceship

pygame.init()

screen_width = 750
screen_height = 700

grey = (29,29,27)


screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()

spaceship = Spaceship()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(grey)
    
    pygame.display.update()
    clock.tick(60)