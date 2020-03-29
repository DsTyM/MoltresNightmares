import pygame
import random
import global_variables as gv


class ForrestPart:
    def __init__(self, forrest_direction=""):
        self.rand_num_1 = random.randint(1, 2)
        self.rand_num_2 = random.randint(1, 2)
        self.size_fact = 2
        if self.rand_num_1 == 1 and forrest_direction in ("left", "down", "right", "up"):
            self.source = pygame.image.load("images/Levels/Level_" + str(gv.level_num) + "/alt_2/" +
                                            forrest_direction + ".png").convert_alpha()
        elif self.rand_num_1 == 1 and forrest_direction == "center":
            self.source = pygame.image.load("images/Levels/Level_" + str(gv.level_num) + "/alt_2/"
                                            + forrest_direction + "_" + str(self.rand_num_2) + ".png").convert_alpha()
        else:
            self.source = pygame.image.load("images/Levels/Level_" + str(gv.level_num) + "/alt_1/"
                                            + forrest_direction + ".png").convert_alpha()
        self.width = self.source.get_rect().width
        self.height = self.source.get_rect().height
        self.x_coord, self.y_coord = 0, 0

    def get(self):
        return pygame.transform.scale(self.source, (int(self.width * self.size_fact),
                                                    int(self.height * self.size_fact)))
