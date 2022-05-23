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
        self.anim_list = PLAYER_ANIM
        self.anim_type = self.Animation.IDLE
        self.image     = self.anim_list[self.anim_type][0]
        self.rect      = self.image.get_rect(midbottom=tuple(pos))
        self.hurtbox   = self.rect
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
        super().update()
        inputs   = self.get_key_events()
        self.acc = pygame.math.Vector2(0, GRAVITY)
        if (not (self.hp <= 0 or self.is_attacking)):
            # moving
            if ((inputs is self.Input.NONE) or
                (inputs&self.Input.LEFT and inputs&self.Input.RIGHT)):
                self.anim_type      = self.Animation.IDLE
            elif ((inputs&self.Input.LEFT and not inputs&self.Input.RIGHT) or
                  (not inputs&self.Input.LEFT and inputs&self.Input.RIGHT)):
                self.anim_type      = self.Animation.MOVE
                self.is_facing_left = bool(inputs&self.Input.LEFT)
                self.acc.x          = 3*(-1 if self.is_facing_left else 1)
            # jumping
            if (inputs&self.Input.JUMP and not (self.is_jumping or self.is_falling)):
                self.acc.y      = -40
                self.is_jumping = True
                self.is_falling = False
            # attacking
            if (inputs&self.Input.ATK1 and inputs&self.Input.ATK2):
                self.is_attacking = False
            elif (inputs&self.Input.ATK1):
                self.anim_type    = self.Animation.ATK1
                self.anim_step    = 0
                self.is_attacking = True
            elif (inputs&self.Input.ATK2):
                self.anim_type    = self.Animation.ATK2
                self.anim_step    = 0
                self.is_attacking = True
        # physics
        self.acc.x += self.vel.x*FRICTION
        self.vel   += self.acc
        self.pos   += (self.vel+self.acc*0.5)*(CLOCK.get_time()/100)
        self.rect.midbottom = self.pos
         # jumping/falling
        if (self.pos.y >= CANVAS_SIZE.y):
            # grounded
            self.vel.y      = 0
            self.pos.y      = CANVAS_SIZE.y
            self.is_jumping = False
            self.is_falling = False
        elif (self.vel.y < 0):
            # jumping
            if (not self.is_attacking):
                self.anim_type = self.Animation.JUMP
            self.is_jumping = True
            self.is_falling = False
        elif (self.vel.y > 0):
            # falling
            if (not self.is_attacking):
                self.anim_type = self.Animation.FALL
            self.is_jumping = False
            self.is_falling = True
        super().animate()
        return
