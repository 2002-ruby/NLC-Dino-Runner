import pygame

from components.obstacles.bird import Bird
from components.obstacles.cactus import Cactus
from components.obstacles.large_cactus import LargeCactus
from utils import text_utils
from utils.constants import SMALL_CACTUS, BIRD, LARGE_CACTUS

import random


class ObstacleManager:

    def __init__(self):
        self.obstacles = []
        # self.random = random.randint(1, 2)

    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                self.obstacles.append(Bird(BIRD))
            elif random.randint(0, 2) == 2:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.hammer is not None and game.player.hammer.rect.colliderect(obstacle.rect):
                game.player.hammer.kill()
                self.obstacles.pop()
            else:
                obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    game.player_heart_manager.reduce_heart()
                    if game.player_heart_manager.heart_count > 0:
                        game.player.shield = True
                        game.player.show_text = False
                        start_time = pygame.time.get_ticks()
                        game.player.shield_time_up = start_time + 1000
                    else:
                        self.obstacles.remove(obstacle)
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count += 1
                        text_utils.emitir_sonido('mixkit-long-game-over-notification-276.wav')
                        break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
