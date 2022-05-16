import os, pygame
from scripts.utils import *

if (DEBUG): print("loading assets...")

ICON_IMG = load_image(os.path.join("icon.ico"))
NONE_IMG = load_image(os.path.join("assets", "images", "none.png"))

# player animations
PLAYER_ANIM = [
    load_images(os.path.join("assets", "images", "entity", "player", "dead*.png")), # dead
    load_images(os.path.join("assets", "images", "entity", "player", "idle*.png")), # idle
    load_images(os.path.join("assets", "images", "entity", "player", "move*.png")), # move
    load_images(os.path.join("assets", "images", "entity", "player", "jump*.png")), # jump
    load_images(os.path.join("assets", "images", "entity", "player", "fall*.png")), # fall
    load_images(os.path.join("assets", "images", "entity", "player", "hurt*.png")), # hurt
    load_images(os.path.join("assets", "images", "entity", "player", "atk1*.png")), # attack 1
    load_images(os.path.join("assets", "images", "entity", "player", "atk2*.png")), # attack 2
    ]

if (DEBUG): print("...done")
