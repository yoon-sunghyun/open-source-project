from scripts import *

# loads a single image
def load_image(file_path):
    if (DEBUG): print(f"loading image: {file_path}")
    return pygame.image.load(file_path).convert_alpha()

# loads multiple images
def load_images(file_path_pattern):
    return [load_image(file_path) for file_path in sorted(glob.glob(file_path_pattern))]
