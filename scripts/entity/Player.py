import enum
from scripts import *
from .Entity import *

class Player(Entity):

    @enum.unique
    class Input(enum.IntFlag):
        NONE  = 0b_0000_0000
        UP    = 0b_0000_0001
        DOWN  = 0b_0000_0010
        LEFT  = 0b_0000_0100
        RIGHT = 0b_0000_1000
        JUMP  = 0b_0001_0000
        ATK1  = 0b_0010_0000
        ATK2  = 0b_0100_0000

    # constructor
    def __init__(self, pos=pygame.math.Vector2(0, 0), max_hp=100):
        super().__init__(pos, max_hp)
        self.inputs = self.Input.NONE
        return

    # gets key inputs
    def get_key_events(self):
        self.inputs = self.Input.NONE
        keys        = pygame.key.get_pressed()

        if (keys[pygame.K_UP]):
            self.inputs |= self.Input.UP
        if (keys[pygame.K_DOWN]):
            self.inputs |= self.Input.DOWN
        if (keys[pygame.K_LEFT]):
            self.inputs |= self.Input.LEFT
        if (keys[pygame.K_RIGHT]):
            self.inputs |= self.Input.RIGHT
        if (keys[pygame.K_SPACE]):
            self.inputs |= self.Input.JUMP

        if (DEBUG and self.inputs != self.Input.NONE):
            print(self.inputs)
        return

    def move(self):
        if ((self.inputs is self.Input.NONE) or
            (self.inputs&self.Input.LEFT and self.inputs&self.Input.RIGHT)):
            self.anim_type      = Entity.Animation.IDLE
        elif ((self.inputs&self.Input.LEFT and not self.inputs&self.Input.RIGHT) or
              (not self.inputs&self.Input.LEFT and self.inputs&self.Input.RIGHT)):
            self.anim_type      = Entity.Animation.MOVE
            self.is_facing_left = bool(self.inputs&self.Input.LEFT)

        if (self.inputs&self.Input.JUMP):
            if (not (self.is_jumping or self.is_falling)):
                self.is_jumping = True
                self.is_falling = False
        return
