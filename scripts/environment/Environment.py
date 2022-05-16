from scripts import *

class Environment(pygame.sprite.Sprite):

    # constructor
    def __init__(self, pos=pygame.math.Vector2(0, 0), len=1):
        super().__init__()
        self.image = pygame.Surface((16*len, 16))
        self.rect  = self.image.get_rect(topleft=tuple(pos))
        for i in range(len):
            self.image.blit(NONE_IMG, (16*i, 0))
        return
