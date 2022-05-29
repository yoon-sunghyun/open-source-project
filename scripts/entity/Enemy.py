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

        self.atk_cooldown = 0
        self.jmp_cooldown = 0
        return

    def get_ai_events(self, player):
        inputs = self.Input.NONE
        if (self.hp != 0 and player.hp != 0):
            if (abs(player.rect.midbottom[0]-self.rect.midbottom[0]) < 70):
                if (player.is_attacking):
                    if (self.rect.midbottom[0] > player.rect.midbottom[0]):
                        inputs |= self.Input.RIGHT
                    if (self.rect.midbottom[0] < player.rect.midbottom[0]):
                        inputs |= self.Input.LEFT
                elif (not self.atk_cooldown):
                    inputs |= random.choice([self.Input.ATK1, self.Input.ATK2])
                    self.atk_cooldown = 1500
            elif (self.rect.midbottom[0] > player.rect.midbottom[0] and not player.is_attacking):
                inputs |= self.Input.LEFT
            elif (self.rect.midbottom[0] < player.rect.midbottom[0] and not player.is_attacking):
                inputs |= self.Input.RIGHT
            if (self.rect.midbottom[1]-player.rect.midbottom[1] > 50 or player.is_attacking):
                if (not self.jmp_cooldown):
                    inputs |= self.Input.JUMP
                    self.jmp_cooldown = 1500
            self.is_facing_left = (self.rect.midbottom[0] > player.rect.midbottom[0])
        return inputs

    def update(self, *args):
        super().update(self.get_ai_events(args[0]))
        self.atk_cooldown = max(0, self.atk_cooldown-CLOCK.get_time())
        self.jmp_cooldown = max(0, self.jmp_cooldown-CLOCK.get_time())
        return
