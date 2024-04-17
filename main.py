import pygame, sys, random
from spaceship import Spaceship
from obstacle import Obstacle
from game import Game

pygame.init()

screen_width = 750
screen_height = 700
offset = 50

grey = (29,29,27)
YELLOW = (243, 216 ,63)

screen = pygame.display.set_mode((screen_width + offset, screen_height + 2*offset))

pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()

game = Game(screen_width, screen_height, offset)

shoot_laser = pygame.USEREVENT
pygame.time.set_timer(shoot_laser, 300)

MYSTERYSHIP = pygame.USEREVENT + 1 
pygame.time.set_timer(MYSTERYSHIP, random.randint(4000,8000))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == shoot_laser and game.run:
            game.alien_shoot_laser()
        if event.type == MYSTERYSHIP and game.run:
            game.create_mystery_ship()
            pygame.time.set_timer(MYSTERYSHIP, random.randint(4000,8000))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and game.run == False:
            game.reset()

    #update 
    if game.run:
        game.spaceship_group.update()
        game.move_aliens()
        game.alien_lasers_group.update()
        game.mystery_ship_group.update()
        game.check_for_collisions()

    screen.fill(grey)

    #draw
    pygame.draw.rect(screen, YELLOW, (10, 10, 780, 780), 2 ,0 ,60 ,60 ,60 ,60)
    pygame.draw.line(screen, YELLOW, (25, 730), (775, 730), 3)
    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.lasers_group.draw(screen)
    game.aliens_group.draw(screen)
    game.alien_lasers_group.draw(screen)
    game.mystery_ship_group.draw(screen)
    
    
    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(screen)
    
    pygame.display.update()
    clock.tick(60)