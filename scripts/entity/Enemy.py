from scripts import *
from .Entity import *

class Enemy(Entity):

    # constructor
    def __init__(self, pos=pygame.math.Vector2(0, 0), max_hp=100):
        super().__init__(pos, max_hp)
        self.anim_list = ENEMY_ANIM
        self.anim_type = self.Animation.IDLE
        self.image     = self.anim_list[self.anim_type][0]
        self.rect      = self.image.get_rect(midbottom=tuple(pos))
        return

    def get_ai_events(self, player):
        inputs = self.Input.NONE
        if (abs(player.rect.midbottom[0]-self.rect.midbottom[0]) < 75):
            # inputs |= random.choice([self.Input.ATK1, self.Input.ATK2])
            pass
        elif (self.rect.midbottom[0] > player.rect.midbottom[0]):
            inputs |= self.Input.LEFT
        elif (self.rect.midbottom[0] < player.rect.midbottom[0]):
            inputs |= self.Input.RIGHT
        if (self.rect.midbottom[1]-player.rect.midbottom[1] > 50 or player.is_attacking):
            inputs |= self.Input.JUMP
        self.is_facing_left = (self.rect.midbottom[0] > player.rect.midbottom[0])
        return inputs

    def update(self, *args):
        super().update(self.get_ai_events(args[0]))
        return
