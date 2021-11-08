from components.obstacles.obstacles import Obstacles


class Cactus(Obstacles):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325

    def update(self, *args, **kwargs) -> None:
        pass

    def draw(self):
        pass
