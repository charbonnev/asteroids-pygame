from constants import *

import pygame

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            screen.fill("black")
            pygame.display.flip()

if __name__ == "__main__":
    main()
