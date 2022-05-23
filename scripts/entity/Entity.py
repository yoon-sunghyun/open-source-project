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

        self.hurtbox = None
        self.hitbox  = None

        self.is_jumping     = False
        self.is_falling     = False
        self.is_facing_left = False
        self.is_attacking   = False
        return

    # animates this Entity
    def animate(self):
        if (self.anim_list != None and len(self.anim_list) > 0 and self.anim_type != None):
            # increasing animation step
            self.anim_step += CLOCK.get_time()/100
            # resetting animation step
            if (self.anim_step >= len(self.anim_list[self.anim_type])):
                self.anim_step = 0
                if (self.is_attacking):
                    self.anim_type    = self.Animation.IDLE
                    self.is_attacking = False
            # updating sprite
            self.image = self.anim_list[self.anim_type][int(self.anim_step)]
            self.image = pygame.transform.flip(self.image, self.is_facing_left, False)
            self.rect  = self.image.get_rect(midbottom=tuple(self.pos))
            if DEBUG: self.debug_animate()
        return

    def debug_animate(self):
        # drawing image outline
        pygame.draw.rect(self.image, "white", self.image.get_rect(), 1)
        # drawing hurtbox outline
        hurtbox_in_image = pygame.Rect(
            ((self.rect.w-self.hurtbox.w)//2, (self.rect.h-self.hurtbox.h)),
            (self.hurtbox.w, self.hurtbox.h))
        pygame.draw.rect(self.image, "blue", hurtbox_in_image, 1)
        return
