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

shoot_laser = pygame.USEREVENT

pygame.time.set_timer(shoot_laser, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == shoot_laser:
            game.alien_shoot_laser()

    #update   
    game.spaceship_group.update()
    game.move_aliens()
    game.alien_lasers_group.update()

    screen.fill(grey)

    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.lasers_group.draw(screen)
    game.aliens_group.draw(screen)
    game.alien_lasers_group.draw(screen)
    
    
    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(screen)
    
    pygame.display.update()
    clock.tick(60)