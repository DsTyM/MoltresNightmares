import pygame


class FireBall:
    def __init__(self):
        self.size_fact = 0.7
        self.source = pygame.image.load("images/Fire Ball.png").convert_alpha()
        self.width = self.source.get_rect().width
        self.height = self.source.get_rect().height
        self.x_speed, self.y_speed = 0, 0
        self.x_coord, self.y_coord = 0, 0

    def get(self):
        return pygame.transform.scale(self.source, (int(self.width * self.size_fact),
                                                    int(self.height * self.size_fact)))


class FaintBall:
    def __init__(self):
        self.size_fact = 0.4
        self.source = pygame.image.load("images/Faint Ball.png").convert_alpha()
        self.width = self.source.get_rect().width
        self.height = self.source.get_rect().height
        self.x_speed, self.y_speed = 0, 0
        self.x_coord, self.y_coord = 0, 0

    def get(self):
        return pygame.transform.scale(self.source, (int(self.width * self.size_fact),
                                                    int(self.height * self.size_fact)))
