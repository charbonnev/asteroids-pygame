from constants import *
from player import Player

import pygame

pygame.init()

dt = 0
game_clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()        
        
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
