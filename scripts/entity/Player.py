from scripts import *
from .Entity import *

class Player(Entity):

    # constructor
    def __init__(self, pos=pygame.math.Vector2(0, 0), max_hp=100):
        super().__init__(pos, max_hp)
        self.anim_list = PLAYER_ANIM
        self.anim_type = self.Animation.IDLE
        self.image     = self.anim_list[self.anim_type][0]
        self.rect      = self.image.get_rect(midbottom=tuple(pos))
        return

    # gets key inputs
    def get_key_events(self):
        inputs = self.Input.NONE
        keys   = pygame.key.get_pressed()

        if (keys[pygame.K_UP]):     inputs |= self.Input.UP
        if (keys[pygame.K_DOWN]):   inputs |= self.Input.DOWN
        if (keys[pygame.K_LEFT]):   inputs |= self.Input.LEFT
        if (keys[pygame.K_RIGHT]):  inputs |= self.Input.RIGHT
        if (keys[pygame.K_SPACE]):  inputs |= self.Input.JUMP
        if (keys[pygame.K_d]):      inputs |= self.Input.ATK1
        if (keys[pygame.K_s]):      inputs |= self.Input.ATK2

        if (DEBUG and inputs != self.Input.NONE):
            print(inputs)
        return inputs

    # updates this Player
    def update(self):
        super().update(self.get_key_events())
        return
