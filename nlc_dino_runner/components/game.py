import pygame
from utils.constants import (
    TITTLE,
    ICON,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BG,
    FPS

)


class Game:
    def __init__(self):
        pygame.init()
        self.playing= False
        pygame.display.set_caption(TITTLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.x_pos_bg = 0
        self.y_pos_bg = 400
        self.game_speed = 20
        self.clock = pygame.time.Clock()

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.updats()
            self.draw()
        pygame.quit()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False


    def updats(self):
        pass

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_backgroun()
        pygame.display.flip()



    def draw_backgroun(self):
        image_with = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_with + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_with:
            self.screen.blit(BG, (image_with + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed


