import pygame


class LevelObject:
    def __init__(self, image_name, coords, size_fact=1.0):
        self.image_name = image_name
        self.coords = coords
        self.size_fact = size_fact

        self.source = pygame.image.load("images/objects/" + self.image_name).convert_alpha()
        self.width = self.source.get_rect().width
        self.height = self.source.get_rect().height

        self.source = pygame.transform.scale(self.source, (int(self.width * self.size_fact),
                                                           int(self.height * self.size_fact)))

        self.width = self.source.get_rect().width
        self.height = self.source.get_rect().height

    def get(self):
        return self.source

    def get_coords(self):
        return [self.width, self.height]
