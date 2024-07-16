import pygame
import random
import math

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Pygame Zombies"

class Color():
    def __init__(self):
        self.black = pygame.Color(0, 0, 0, 255)
        self.white = pygame.Color(255, 255, 255, 255)
        self.red = pygame.Color(255, 0, 0, 255)
        self.green = pygame.Color(0, 255, 0, 255)
        self.blue = pygame.Color(0, 0, 255, 255)

    def get_random():
        return pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255)
    
    def get_grayscale():
        value = random.randint(0, 255)
        return pygame.Color(value, value, value, 255)
    
def get_pos_vectors(origin_pos: pygame.math.Vector2, target_pos: pygame.math.Vector2, speed: float) -> list:
    distance = [target_pos.x - origin_pos.x, target_pos.y - origin_pos.y]
    normal = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
    direction = [distance[0] / normal, distance[1] / normal]
    vectors = [direction[0] * speed, direction[1] * speed]

    return vectors

def get_distance(origin_pos: pygame.math.Vector2, target_pos: pygame.math.Vector2) -> float:
    distance = [target_pos.x - origin_pos.x, target_pos.y - origin_pos.y]
    normal = math.sqrt(distance[0] ** 2 + distance [1] ** 2)

    return normal
    
color = Color()

delta_time = 0
fps_limit = 120
block_size = 40

events = None
world_reference = None
player_reference = None

global_offset = pygame.math.Vector2()