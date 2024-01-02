import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

import random

pygame.init()

FPS = pygame.time.Clock()

HEIGHT = 800
WIDTH = 1200
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
PLAYER_SIZE = (20, 20)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

player = pygame.Surface(PLAYER_SIZE)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()
player_speed = [1, 1]

playing = True

while playing:
    FPS.tick(120)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False

    main_display.fill(COLOR_BLACK)
    # print(player_rect)

    keys = pygame.key.get_pressed()

    # if player_rect.bottom >= HEIGHT:
    #     player_speed = random.choice(([1, -1], [-1, -1]))
    #
    # elif player_rect.right >= WIDTH:
    #     player_speed = random.choice(([-1, 1], [1, 1]))
    #
    # elif player_rect.top <= 0:
    #     player_speed = random.choice(([-1, -1], [-1, 1]))
    #
    # elif player_rect.left <= 0:
    #     player_speed = random.choice(([1, 1], [1, -1]))

    main_display.blit(player, player_rect)

    player_rect = player_rect.move(player_speed)

    pygame.display.flip()


