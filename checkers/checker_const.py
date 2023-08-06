import pygame as pg

# GAME FRAME RATE
FPS = 60

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS


CONTAINER = (154, 123, 79)
BORDER_COLOR = (205, 170, 109)
BLACK = (0, 0, 0)
CELL = (101,53,15)
WHITE = (255, 255, 255)


CROWN = pg.transform.scale(pg.image.load('checkers/assets/crown.png'), (44, 25))
