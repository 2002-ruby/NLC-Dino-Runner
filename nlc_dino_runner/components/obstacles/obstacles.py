from pygame.sprite import Sprite

from components import obstacles
from utils.constants import SCREEN_WIDTH


class Obstacle(Sprite):

    def __init__(self, image, index):
        self.image = image
        self.index = index
        self.rect = self.image[self.index].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, obstacle):
        self.rect.x -= 10
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.index], self.rect)
