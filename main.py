import pygame, sys
from spaceship import Spaceship
from obstacle import Obstacle
from game import Game

pygame.init()

screen_width = 750
screen_height = 700

grey = (29,29,27)

screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()

game = Game(screen_width, screen_height )

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #update   
    game.spaceship_group.update()

    screen.fill(grey)

    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.lasers_group.draw(screen)
    game.aliens_group.draw(screen)
    game.move_aliens()
    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(screen)
    
    pygame.display.update()
    clock.tick(60)