import pygame
import file_utils
import math
from sprites.car import Car
import random

config = file_utils.read_config_json()
# display_rect = pygame.Rect(0, 0, config["width"], config["height"])
display_mask = pygame.mask.from_surface(pygame.Surface((config["width"], config["height"])))

random_image = random.randint(1, 3)
class Mob1(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.images = [
            pygame.image.load("./assets/Mob1.png"),
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

        self.rect.center = (
            random.randint(230, config["width"] - 20),
            800
        )

        self.speed_y = random.randint(10, 15)

    def update(self, *args, **kwargs):
        if self.rect.y + self.rect.height > config["height"]:
            self.rect.y -= self.speed_y
        else:
            self.kill()

        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            self.accelerate(1)
        if key[pygame.K_s]:
            self.rect.y -= self.speed_y


    @property
    def hitbox(self):
        surface = pygame.Surface(self.rect.size)
        surface.fill(config['colors']['red'])
        surface.set_alpha(30)
        return surface

    def to_json(self):
        return {
            "postions": self.rect.center,
            "speed": 0
        }
    def accelerate(self, value):
        self.rect.y += self.speed_y + value
