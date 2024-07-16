import pygame

import lib

class Wall(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.size = lib.block_size
        self.pos = pygame.math.Vector2(x * self.size, y * self.size)

        self.image = pygame.Surface([width * self.size, height * self.size])
        self.image.fill(lib.color.green)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        