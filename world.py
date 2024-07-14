import pygame
import random

import camera
import player
import lib

class World():
    def __init__(self, background_path: str) -> None:
        lib.world_reference = self

        self.display_surface = pygame.display.get_surface()
        self.world_background = pygame.image.load(background_path).convert_alpha()
        
        self.world_camera = camera.PlayerCenterCamera(self.world_background)
        self.zombies = pygame.sprite.Group()
        
        self.player = player.Player()
        lib.player_reference = self.player

        self.world_camera.add(self.player)

    def draw(self) -> None:
        self.world_camera.camera_draw(self.player)

    def update(self) -> None:
        self.world_camera.update()