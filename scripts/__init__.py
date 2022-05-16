import argparse
import os
import sys

DESCRIPTION = "Sejong Uni. Open Source Project"
PARSER = argparse.ArgumentParser(description=DESCRIPTION)
PARSER.add_argument(
    "-c", "--cursor",
    action  = "store_true",
    help    = "show system cursor instead of virtual cursor")
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

# cursor related setup
SHOW_CURSOR = ARGS.cursor or ARGS.debug
pygame.mouse.set_visible(SHOW_CURSOR)

from scripts.utils       import *
from scripts.assets      import *
from scripts.entity      import *
from scripts.environment import *

CANVAS_SCALE  = 200
CANVAS_SIZE   = pygame.math.Vector2(RATIO_W*CANVAS_SCALE, RATIO_H*CANVAS_SCALE)
CANVAS        = pygame.Surface(tuple(CANVAS_SIZE))

# creating environments
LEVEL = pygame.sprite.Group([Environment()])

# creating entities
ENEMIES = pygame.sprite.Group([Enemy()])
PLAYER  = pygame.sprite.GroupSingle(
    TestCharacter(pygame.math.Vector2(CANVAS_SIZE.x//2, CANVAS_SIZE.y//2)))

pygame.display.set_caption(f"[{DESCRIPTION}]-[{CLOCK.get_fps():.2f} FPS]")
pygame.display.set_icon(ICON_IMG)
