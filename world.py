import pygame
import random

import camera
import player
import lib
import wall

class World():
    def __init__(self, background_path: str) -> None:
        lib.world_reference = self

        self.display_surface = pygame.display.get_surface()
        self.world_background = pygame.image.load(background_path).convert_alpha()
        
        self.world_camera = camera.PlayerCenterCamera(self.world_background)
        self.zombies = pygame.sprite.Group()
        self.wall_container = pygame.sprite.Group()
        self.collidables = pygame.sprite.Group()
        
        self.player = player.Player()
        lib.player_reference = self.player

        self.walls = [
            [0, 0, 20, 1]
        ]

        self.world_camera.add(self.player)
        self.create_walls()

    def create_walls(self) -> None:
        for wall_data in self.walls:
            x, y, width, height = wall_data
            w = wall.Wall(x, y, width, height)
            self.world_camera.add(w)
            self.wall_container.add(w)
            self.collidables.add(w)

    def player_wall_collision(self) -> None:
        collision_tollerance = 15

        for wall in self.wall_container:
            if self.player.rect.colliderect(wall.rect):
                if abs(self.player.rect.left - wall.rect.right) < collision_tollerance:
                    self.player.pos.x = wall.rect.right + self.player.size / 2
                if abs(self.player.rect.right - wall.rect.left) < collision_tollerance:
                    self.player.pos.x = wall.rect.left - self.player.size / 2
                if abs(self.player.rect.top - wall.rect.bottom) < collision_tollerance:
                    self.player.pos.y = wall.rect.bottom + self.player.size / 2
                if abs(self.player.rect.bottom - wall.rect.top) < collision_tollerance:
                    self.player.pos.y = wall.rect.top - self.player.size / 2

    def draw(self) -> None:
        self.world_camera.camera_draw(self.player)

    def update(self) -> None:
        self.world_camera.update()
        
        self.player_wall_collision()