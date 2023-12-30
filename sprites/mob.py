import pygame
import file_utils
import math
from sprites.car import Car
import random

config = file_utils.read_config_json()
# display_rect = pygame.Rect(0, 0, config["width"], config["height"])
display_mask = pygame.mask.from_surface(pygame.Surface((config["width"], config["height"])))

random_image = random.randint(1, 3)
class Mob(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.images = [
            pygame.image.load("./assets/Mob1.png"),
        ]
        self.images = list(map(
            lambda x: pygame.transform.scale(
                pygame.transform.rotate(x, 180),
                (140, 280)
            ),
            self.images
        ))
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.mask: pygame.mask.Mask = pygame.mask.from_surface(self.image)

        self.rect.center = (
            random.randint(0, config["width"] - 240),
            random.randint(0, 10)
        )

        self.speed_y = random.randint(10, 30)
        self.speed_x = 0

    def update(self, *args, **kwargs):
        if self.rect.y + self.rect.height < config["height"]:
            self.rect.y += self.speed_y
        else:
            self.kill()

        if self.speed_y > 5:
            self.speed_y -= 0.1
        key = pygame.key.get_pressed()

        # управление по Y
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


    @staticmethod
    def parse_json(json: dict):
        car = Car()
        car.rect.center = json["postions"]
        car.velocity.update(json["speed"])
        car.turn(json["angle"])
        return car


#group_collide

