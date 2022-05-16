from scripts import *
from .Player import Player

class TestCharacter(Player):

    # constructor
    def __init__(self, pos=pygame.math.Vector2(0, 0), max_hp=100):
        super().__init__(pos, max_hp)
        # graphics related attributes
        self.anim_list = PLAYER_ANIM
        self.anim_type = self.Animation.IDLE
        self.image     = self.anim_list[self.anim_type][0]
        self.rect      = self.image.get_rect(midbottom=tuple(pos))
        self.hurtbox   = self.rect
        return
