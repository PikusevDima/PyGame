import random
import math
import pygame


def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


def get_lenght(x1, y1, x2, y2):
    x = (x1 - x2) ** 2
    y = math.pow(y1 - y2, 2)
    return math.sqrt(x + y)

def generate_point(a, b, c, d):
    return random.randint(a, b), random.randint(c, d)
