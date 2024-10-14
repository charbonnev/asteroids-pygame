from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

import pygame

pygame.init()

game_clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (updatable, drawable, asteroids)
AsteroidField.containers = (updatable)

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
asteroidField = AsteroidField()

def main():
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for entity in updatable:
            entity.update(dt)
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()        
        dt = game_clock.tick(60) / 1000 

if __name__ == "__main__":
    main()
