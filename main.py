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

font = pygame.font.Font("Font/monogram.ttf", 40)
level_surface = font.render("LEVEL:", False, YELLOW)
game_over_surface = font.render("GAME OVER", False, YELLOW)
score_text_surface = font.render("SCORE", False, YELLOW)
highscore_text_surface = font.render("HIGHSCORE", False, YELLOW)

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
        if keys[pygame.K_ESCAPE] and game.run:       
                game.run = False
        if keys[pygame.K_p] and game.run == False:       
                game.run = True
        

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
    if game.run:
        screen.blit(level_surface, (570, 740, 50, 50))
        formatted_level = str(game.level)
        level_text_surface = font.render(formatted_level, False, YELLOW)
        screen.blit(level_text_surface, (670, 740, 50, 50))
    else:
        screen.blit(game_over_surface, (570, 740, 50, 50))

    x = 50
    for life in range(game.lives):
        screen.blit(game.spaceship_group.sprite.image, (x, 745))
        x += 50

    screen.blit(score_text_surface, (50, 15, 50, 50))
    formatted_score = str(game.score).zfill(5)
    score_surface = font.render(formatted_score, False, YELLOW)
    screen.blit(score_surface, (50, 40, 50, 50))
    formatted_highscore = str(game.highscore).zfill(5)
    screen.blit(highscore_text_surface, (550, 15, 50, 50))
    highscore_surface = font.render(formatted_highscore, False, YELLOW)
    screen.blit(highscore_surface, (625, 40, 50, 50))

    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.lasers_group.draw(screen)
    game.aliens_group.draw(screen)
    game.alien_lasers_group.draw(screen)
    game.mystery_ship_group.draw(screen)
    
    
    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(screen)
    
    pygame.display.update()
    clock.tick(60)