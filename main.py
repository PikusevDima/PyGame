import random
from sprites.mob import Mob
import pygame
import utils
from sprites.car import Car
import file_utils

config = file_utils.read_config_json()
# save = file_utils.read_json()

pygame.init()
pygame.mixer.init()
pygame.font.init()

font = pygame.font.SysFont(pygame.font.get_default_font(), 20)

screen = pygame.display.set_mode(
    (config['width'], config['height'])
)
mobs = pygame.sprite.Group()



car = Car()
car_group = pygame.sprite.Group()
car_group.add(car)
# for data in save:
#     car = Car.parse_json(data)
#     car_group.add(car)

clock = pygame.time.Clock()
running = True

time = 8 * config['framerate']
score = 0

while running:
    clock.tick(config['framerate'])
    if time == 0:
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    car_group.update()
    time -= 1

    screen.fill(config['colors']['black'])
    pygame.draw.line(screen, (249, 252, 63),
                     (210, 900),
                     (210, 0),
                     6)
    car_group.draw(screen)

    time_rendered = font.render(f"Time: {time / config['framerate']}", True, (255, 255, 255))
    screen.blit(time_rendered, (10, 10))

    bound_rendered = font.render(f"Score: {score}", True, (0, 255, 255))
    screen.blit(bound_rendered, (10, 50))

    pygame.display.flip()

pygame.quit()
