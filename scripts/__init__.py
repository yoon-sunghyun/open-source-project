import argparse
import glob
import os
import random
import sys

MAIN_PATH = os.path.join(os.path.dirname(__file__), "..")

DESCRIPTION = "Sejong Uni. Open Source Project"
PARSER = argparse.ArgumentParser(description=DESCRIPTION)
PARSER.add_argument(
    "-d", "--debug",
    action  = "store_true",
    help    = "run in debug mode")
PARSER.add_argument(
    "-f", "--fps",
    action  = "store",
    default = 60,
    type    = int,
    help    = "set framerate(30~90); default is 60")
ARGS  = PARSER.parse_args()
DEBUG = ARGS.debug

# pygame related setup
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.init()

# FPS(frames-per-second) related setup
CLOCK = pygame.time.Clock()
FPS   = ARGS.fps if 30 <= ARGS.fps <= 90 else 60

# display related setup
RATIO_W = 1.6
RATIO_H = 1.0

DISPLAY_SCALE = 600
DISPLAY_SIZE  = pygame.math.Vector2(RATIO_W*DISPLAY_SCALE, RATIO_H*DISPLAY_SCALE)
DISPLAY       = pygame.display.set_mode(tuple(DISPLAY_SIZE))

CANVAS_SCALE  = 200
CANVAS_SIZE   = pygame.math.Vector2(RATIO_W*CANVAS_SCALE, RATIO_H*CANVAS_SCALE)
CANVAS        = pygame.Surface(tuple(CANVAS_SIZE)).convert_alpha()

from scripts.utils  import *
from scripts.assets import *

GRAVITY  = 2.0
FRICTION = -0.15

# creating entities
from scripts.entity import *
ENEMY  = pygame.sprite.GroupSingle(Enemy(pygame.math.Vector2(CANVAS_SIZE.x*2/3, CANVAS_SIZE.y//2)))
PLAYER = pygame.sprite.GroupSingle(Player(pygame.math.Vector2(CANVAS_SIZE.x*1/3, CANVAS_SIZE.y//2)))

pygame.display.set_caption(f"[{DESCRIPTION}]-[{CLOCK.get_fps():.2f} FPS]")
pygame.display.set_icon(ICON_IMG)
