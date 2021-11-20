from components.obstacles.obstacles import Obstacle
from utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 240
        self.index = 0

    def draw(self, screen):
        if self.index >= 10:
            self.index = 0
        screen.blit(self.image[self.index//5], self.rect)
        self.index += 1

    # def run(self):
    #     self.image = BIRD[0] if self.index < 5 else BIRD[1]
    #     self.image = [0]
    #     self.index += 1
