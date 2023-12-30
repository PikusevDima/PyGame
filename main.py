import random
from sprites.mob import Mob
import pygame
import utils
from sprites.car import Car
import file_utils
from sprites.mob2 import Mob1

config = file_utils.read_config_json()
# save = file_utils.read_json()

pygame.init()
pygame.mixer.init()
pygame.font.init()

font = pygame.font.SysFont(pygame.font.get_default_font(), 20)

screen = pygame.display.set_mode(
    (config['width'], config['height'])
)


car = Car()
player = pygame.sprite.Group()
player.add(car)

mob = Mob()
mob_group = pygame.sprite.Group()
mob_group.add(mob)

mob1 = Mob1()
mob_group1 = pygame.sprite.Group()
mob_group1.add(mob1)


n_mobs = 1
for i in range(n_mobs):
    mob_group1.add(Mob())

n_mobs1 = 1
for i in range(n_mobs):
    mob_group.add(Mob())

clock = pygame.time.Clock()
running = True

score = 0

while running:
    clock.tick(config['framerate'])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.update()
    mob_group.update()
    mob_group1.update()

    score += 1

    if len(mob_group) < n_mobs:
        mob_group.add(Mob())

    if len(mob_group1) < n_mobs1:
        mob_group.add(Mob1())

    hits = pygame.sprite.groupcollide(player, mob_group, False, True)
    if hits:
        car.health -= 1

    hits = pygame.sprite.groupcollide(player, mob_group1, False, True)
    if hits:
        car.health -= 1

    if car.health == 0:
        running = False

    screen.fill(config['colors']['black'])
    pygame.draw.line(screen, (249, 252, 63),
                     (210, 900),
                     (210, 0),
                     6)
    player.draw(screen)
    mob_group.draw(screen)


    bound_rendered = font.render(f"Score: {score}", True, (0, 255, 255))
    screen.blit(bound_rendered, (10, 50))

    pygame.display.flip()

pygame.quit()
