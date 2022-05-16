from scripts import *
from .Entity import Entity

class Enemy(Entity):

    # constructor
    def __init__(self, pos=pygame.math.Vector2(0, 0), max_hp=00):
        super().__init__(pos, max_hp)
        return
