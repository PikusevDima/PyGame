import config
import random
import pygame.key
from pygame.sprite import Sprite
from pygame import Surface, image, transform
import utils

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.index = 0

        self.images = [
            image.load("Mob1/.png"),
            image.load("assets/.png")
        ]
        self.images = list(map(
            lambda x: transform.scale(x, (64, 64)),
            self.images
        ))

        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (config.WIDTH / 2, config.HEIGHT / 2)

        self.health = 1
        self.points = 0
        self.resist = 5

        self.speed_x = 0
        self.speed_y = 5

class Mob(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = Surface((20, 20))
        self.color = config.COLORS["Red"]
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(self.rect.width // 2, config.WIDTH - self.rect.width // 2),
            random.randint(self.rect.height // 2, config.HEIGHT - self.rect.height // 2)
        )

        self.speed_x = 0
        self.speed_y = 5

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.x > config.WIDTH - self.rect.width or self.rect.x < 0:
            self.rect.x -= self.speed_x
            # self.speed_x *= 0.95

        self.rect.y += self.speed_y
        if self.rect.y > config.HEIGHT - self.rect.height or self.rect.y < 0:
            self.rect.y -= self.speed_y

    def reverse_speed_x(self):
        self.speed_x = -self.speed_x

    def reverse_speed_y(self):
        self.speed_y = -self.speed_y
