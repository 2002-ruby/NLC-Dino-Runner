from pygame.sprite import Sprite
from utils.constants import SCREEN_WIDTH


class Obstacles(Sprite):

    def __init__(self, image, obstacle_type):
        self.image = image
        self.obstacle_type = obstacle_type
        self.rect = self.image[self.obstacle_typetype].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, *args, **kwargs) -> None:
        pass

    def draw(self):
        pass
