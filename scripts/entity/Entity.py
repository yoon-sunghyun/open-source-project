import enum
from scripts import *

class Entity(pygame.sprite.Sprite):

    @enum.unique
    class Animation(enum.IntEnum):
        DEAD = 0
        IDLE = 1
        MOVE = 2
        JUMP = 3
        FALL = 4
        HURT = 5
        ATK1 = 6
        ATK2 = 7

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
        super().__init__()
        # graphics related attributes
        self.anim_list = None
        self.anim_type = None
        self.anim_step = 0
        self.image     = NONE_IMG
        self.rect      = self.image.get_rect()
        # gameplay realted attributes
        self.acc       = pygame.math.Vector2(0, 0)
        self.vel       = pygame.math.Vector2(0, 0)
        self.pos       = pos

        self.max_hp    = max_hp
        self.hp        = max_hp
        self.dmg       = max_hp//5

        self.is_jumping     = False
        self.is_falling     = False
        self.is_facing_left = False
        self.is_hurt        = False
        self.is_attacking   = False
        return

    def take_damage(self, damage):
        if (not self.is_hurt):
            self.anim_type    = self.Animation.HURT
            self.anim_step    = 0
            self.is_hurt      = True
            self.is_attacking = False
            self.hp           = max(0, self.hp-damage)
        return

    # animates this Entity
    def animate(self):
        if (self.anim_list != None and len(self.anim_list) > 0 and self.anim_type != None):
            # increasing animation step
            self.anim_step += CLOCK.get_time()/100
            # resetting animation step
            if (self.anim_step >= len(self.anim_list[self.anim_type])):
                if (self.anim_type == self.Animation.DEAD):
                    self.anim_step = len(self.anim_list[self.anim_type])-1
                else:
                    if (self.is_hurt):
                        self.is_hurt = False
                    if (self.is_attacking):
                        self.is_attacking = False
                    self.anim_step = 0
            # updating sprite
            self.image = self.anim_list[self.anim_type][int(self.anim_step)]
            self.image = pygame.transform.flip(self.image, self.is_facing_left, False)
            self.rect  = self.image.get_rect(midbottom=tuple(self.pos))
            if DEBUG: self.debug_animate()
        return

    def debug_animate(self):
        # drawing image outline
        pygame.draw.rect(self.image, "white", self.image.get_rect(), 1)
        return

    def update(self, inputs):
        # movement
        self.acc = pygame.math.Vector2(0, GRAVITY)
        if (self.hp == 0 and self.pos.y == CANVAS_SIZE.y and self.anim_type != self.Animation.DEAD):
            self.anim_type = self.Animation.DEAD
            self.anim_step = 0
        elif (not (self.is_hurt or self.is_attacking)):
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
                self.acc.y      = -50
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
        # left & right bound
        if (self.pos.x < 0):
            self.pos.x = 0
        if (self.pos.x > CANVAS_SIZE.x):
            self.pos.x = CANVAS_SIZE.x
        # jumping/falling
        if (self.pos.y >= CANVAS_SIZE.y):
            # grounded
            self.vel.y      = 0
            self.pos.y      = CANVAS_SIZE.y
            self.is_jumping = False
            self.is_falling = False
        elif (self.vel.y < 0):
            # jumping
            if (not (self.hp == 0 or self.is_hurt or self.is_attacking)):
                self.anim_type = self.Animation.JUMP
            self.is_jumping = True
            self.is_falling = False
        elif (self.vel.y > 0):
            # falling
            if (not (self.hp == 0 or self.is_hurt or self.is_attacking)):
                self.anim_type = self.Animation.FALL
            self.is_jumping = False
            self.is_falling = True
        self.animate()
        return
