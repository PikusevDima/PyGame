import pygame
import file_utils
import math
import random
from pygame.sprite import Sprite


config = file_utils.read_config_json()
# display_rect = pygame.Rect(0, 0, config["width"], config["height"])
display_mask = pygame.mask.from_surface(pygame.Surface((config["width"], config["height"])))


class Car(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.images = [
            pygame.image.load("./assets/Player.png"),
        ]
        self.images = list(map(
            lambda x: pygame.transform.scale(
                pygame.transform.rotate(x, 0),
                (140, 280)
            ),
            self.images
        ))
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.mask: pygame.mask.Mask = pygame.mask.from_surface(self.image)

        self.rect.center = (config['width'] // 2, config['height'] // 2)

        self.speed_x = 15
        self.health = 1



    def update(self, *args, **kwargs):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.rect.x -= self.speed_x
        if key[pygame.K_d]:
            self.rect.x += self.speed_x

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > config['width'] - self.rect.width:
            self.rect.x = config['width'] - self.rect.width
    @property
    def hitbox(self):
        surface = pygame.Surface(self.rect.size)
        surface.fill(config['colors']['red'])
        surface.set_alpha(30)
        return surface
