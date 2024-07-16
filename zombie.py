import pygame
import random

import lib

class BaseZombie(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2()
        self.speed = 100
        self.size = lib.block_size

        self.health = 5

        self.outside_barricade = True

        self.image = pygame.Surface([self.size, self.size])
        self.image.fill(lib.color.red)
        # self.image.set_colorkey(lib.color.red)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self) -> None:
        self.pos += self.vel * lib.delta_time
        self.rect.center = self.pos

        self.move()

        if self.health <= 0:
            self.kill()

    def move(self) -> None:
        if self.outside_barricade:
            self.move_to_barricade()
        else:
            self.move_to_player()