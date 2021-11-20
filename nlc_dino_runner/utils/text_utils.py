import pygame

from utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, IMG_DIR

FONT_STYLE = 'freesansbold.ttf'
black_color = (0, 0, 0)
def get_score_element (points):
   font = pygame.font.Font(FONT_STYLE, 22)
   text = font.render('Points : ' + str(points) , True, black_color)
   text_rect = text.get_rect()
   text_rect.center = (1000, 50)
   return text, text_rect

def get_centered_message(message, width = SCREEN_WIDTH // 2, height = SCREEN_HEIGHT// 2, size=30):
   font = pygame.font.Font(FONT_STYLE, size)
   text = font.render(message, True, black_color)
   text_rect = text.get_rect()
   text_rect.center = (width, height)
   return text, text_rect

def emitir_sonido (name_sound):
        path = IMG_DIR + str("/") + name_sound
        sonido_fondo = pygame.mixer.Sound(path)
        pygame.mixer.Sound.play(sonido_fondo)