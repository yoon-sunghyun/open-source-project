from scripts import *

if (DEBUG): print("loading assets...")

ICON_IMG = load_image(os.path.join(MAIN_PATH, "icon.ico"))
NONE_IMG = load_image(os.path.join(MAIN_PATH, "assets", "images", "none.png"))

# player animations
if (DEBUG): print("--- player animation ---")
PLAYER_ANIM = [
    load_images(os.path.join(MAIN_PATH, "assets", "images", "entity", "player", "dead*.png")), # dead
    load_images(os.path.join(MAIN_PATH, "assets", "images", "entity", "player", "idle*.png")), # idle
    load_images(os.path.join(MAIN_PATH, "assets", "images", "entity", "player", "move*.png")), # move
    load_images(os.path.join(MAIN_PATH, "assets", "images", "entity", "player", "jump*.png")), # jump
    load_images(os.path.join(MAIN_PATH, "assets", "images", "entity", "player", "fall*.png")), # fall
    load_images(os.path.join(MAIN_PATH, "assets", "images", "entity", "player", "hurt*.png")), # hurt
    load_images(os.path.join(MAIN_PATH, "assets", "images", "entity", "player", "atk1*.png")), # attack 1
    load_images(os.path.join(MAIN_PATH, "assets", "images", "entity", "player", "atk2*.png")), # attack 2
    ]

# enemy animations
if (DEBUG): print("--- enemy animation ---")
ENEMY_ANIM = [
    load_images(os.path.join(MAIN_PATH, "assets", "images", "entity", "enemy", "dead*.png")), # dead
    load_images(os.path.join(MAIN_PATH, "assets", "images", "entity", "enemy", "idle*.png")), # idle
    load_images(os.path.join(MAIN_PATH, "assets", "images", "entity", "enemy", "move*.png")), # move
    load_images(os.path.join(MAIN_PATH, "assets", "images", "entity", "enemy", "jump*.png")), # jump
    load_images(os.path.join(MAIN_PATH, "assets", "images", "entity", "enemy", "fall*.png")), # fall
    load_images(os.path.join(MAIN_PATH, "assets", "images", "entity", "enemy", "hurt*.png")), # hurt
    load_images(os.path.join(MAIN_PATH, "assets", "images", "entity", "enemy", "atk1*.png")), # attack 1
    load_images(os.path.join(MAIN_PATH, "assets", "images", "entity", "enemy", "atk2*.png")), # attack 2
    ]

if (DEBUG): print("...done")
