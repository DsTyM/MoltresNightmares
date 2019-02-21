import pygame
import random
import global_variables as gv


class Haunter:
    def __init__(self, coords):
        self.zoom_factor = 2.5
        self.haunter = pygame.image.load("images/Haunter/down/down_1.png").convert_alpha()
        self.width = self.haunter.get_rect().width
        self.height = self.haunter.get_rect().height
        self.haunter = pygame.transform.scale(self.haunter, (int(self.width * self.zoom_factor),
                                                             int(self.height * self.zoom_factor)))
        self.width = self.haunter.get_rect().width
        self.height = self.haunter.get_rect().height

        self.is_alive = True

        self.x_speed, self.y_speed = 0, 0
        self.x_coord, self.y_coord = coords

        self.direction = "down"
        self.moves = ["down_1", "down_2", "down_1", "down_3"]
        self.move_step = random.randint(0, 3)

        self.x_distance = 2 * gv.size[0]  # 180
        self.y_distance = 250  # 250

        self.old_x_speed = self.x_speed
        self.old_y_speed = self.y_speed

        self.speed_factor = 3

        self.can_move = False

    def change_haunter_move(self):
        self.move_step = (self.move_step + 1) % 4
        self.haunter = pygame.image.load("images/Haunter/" + self.direction + "/"
                                         + self.moves[self.move_step] + ".png").convert_alpha()
        self.width = self.haunter.get_rect().width
        self.height = self.haunter.get_rect().height
        self.haunter = pygame.transform.scale(self.haunter, (int(self.width * self.zoom_factor),
                                                             int(self.height * self.zoom_factor)))

        self.width = self.haunter.get_rect().width
        self.height = self.haunter.get_rect().height

    def check_distance_to_player(self):
        if self.x_coord - gv.x_coord < -self.x_distance and self.y_coord - gv.y_coord < -self.y_distance:
            self.x_speed = self.speed_factor
            self.y_speed = self.speed_factor
            self.direction = "down_right"
        elif self.x_coord - gv.x_coord > self.x_distance and self.y_coord - gv.y_coord < -self.y_distance:
            self.x_speed = -self.speed_factor
            self.y_speed = self.speed_factor
            self.direction = "down_left"
        elif self.x_coord - gv.x_coord < -self.x_distance and self.y_coord - gv.y_coord > self.y_distance:
            self.x_speed = self.speed_factor
            self.y_speed = -self.speed_factor
            self.direction = "up_right"
        elif self.x_coord - gv.x_coord > self.x_distance and self.y_coord - gv.y_coord > self.y_distance:
            self.x_speed = -self.speed_factor
            self.y_speed = -self.speed_factor
            self.direction = "up_left"
        elif self.x_coord - gv.x_coord < -self.x_distance:
            self.x_speed = self.speed_factor
            self.y_speed = 0
            self.direction = "right"
        elif self.x_coord - gv.x_coord > self.x_distance:
            self.x_speed = -self.speed_factor
            self.y_speed = 0
            self.direction = "left"
        elif self.y_coord - gv.y_coord < -self.y_distance:
            self.x_speed = 0
            self.y_speed = self.speed_factor
            self.direction = "down"
        elif self.y_coord - gv.y_coord > self.y_distance:
            self.x_speed = 0
            self.y_speed = -self.speed_factor
            self.direction = "up"
        else:
            self.x_speed = 0
            self.y_speed = 0

    def check_direction(self):
        partial_val_x = int(gv.size[0] / 12)
        partial_val_y = int(gv.size[1] / 12)

        if self.x_coord < gv.x_coord and self.y_coord < gv.y_coord:
            self.direction = "down_right"
        elif self.x_coord > gv.x_coord and self.y_coord > gv.y_coord:
            self.direction = "up_left"
        elif self.x_coord < gv.x_coord and self.y_coord > gv.y_coord:
            self.direction = "up_right"
        elif self.x_coord > gv.x_coord and self.y_coord < gv.y_coord:
            self.direction = "down_left"

        # adjusting haunter looking for Moltress
        if self.y_coord - partial_val_y - 60 < gv.y_coord < self.y_coord + partial_val_y \
                and self.x_coord < gv.x_coord:
            self.direction = "right"
        elif self.y_coord - partial_val_y - 60 < gv.y_coord < self.y_coord + partial_val_y \
                and self.x_coord > gv.x_coord:
            self.direction = "left"
        elif self.x_coord - partial_val_x - 20 < gv.x_coord < self.x_coord + partial_val_x \
                and self.y_coord < gv.y_coord:
            self.direction = "down"
        elif self.x_coord - partial_val_x - 20 < gv.x_coord < self.x_coord + partial_val_x \
                and self.y_coord > gv.y_coord:
            self.direction = "up"

    def get(self):
        return self.haunter


class Gengar:
    def __init__(self, coords):
        self.zoom_factor = 2.5
        self.haunter = pygame.image.load("images/Gengar/down/down_1.png").convert_alpha()
        self.width = self.haunter.get_rect().width
        self.height = self.haunter.get_rect().height
        self.haunter = pygame.transform.scale(self.haunter, (int(self.width * self.zoom_factor),
                                                             int(self.height * self.zoom_factor)))
        self.width = self.haunter.get_rect().width
        self.height = self.haunter.get_rect().height

        self.is_alive = True

        self.x_speed, self.y_speed = 0, 0
        self.x_coord, self.y_coord = coords

        self.direction = "down"
        self.moves = ["down_1", "down_2", "down_1", "down_3"]
        self.move_step = random.randint(0, 3)

        self.x_distance = 180  # 180
        self.y_distance = 250  # 250

        self.old_x_speed = self.x_speed
        self.old_y_speed = self.y_speed

        self.speed_factor = 3

        self.can_move = False

    def change_gengar_target(self):
        self.moves = [self.direction + "_1", self.direction + "_2", self.direction + "_1", self.direction + "_3"]
        self.haunter = pygame.image.load("images/Gengar/" + self.direction + "/"
                                         + self.moves[self.move_step] + ".png").convert_alpha()
        self.width = self.haunter.get_rect().width
        self.height = self.haunter.get_rect().height
        self.haunter = pygame.transform.scale(self.haunter, (int(self.width * self.zoom_factor),
                                                             int(self.height * self.zoom_factor)))

        self.width = self.haunter.get_rect().width
        self.height = self.haunter.get_rect().height

    def change_gengar_move(self):
        self.move_step = (self.move_step + 1) % 4
        self.haunter = pygame.image.load("images/Gengar/" + self.direction + "/"
                                         + self.moves[self.move_step] + ".png").convert_alpha()
        self.width = self.haunter.get_rect().width
        self.height = self.haunter.get_rect().height
        self.haunter = pygame.transform.scale(self.haunter, (int(self.width * self.zoom_factor),
                                                             int(self.height * self.zoom_factor)))

        self.width = self.haunter.get_rect().width
        self.height = self.haunter.get_rect().height

    def check_distance_to_player(self):
        if self.x_coord - gv.x_coord < -self.x_distance and self.y_coord - gv.y_coord < -self.y_distance:
            self.x_speed = self.speed_factor
            self.y_speed = self.speed_factor
            self.direction = "down_right"
        elif self.x_coord - gv.x_coord > self.x_distance and self.y_coord - gv.y_coord < -self.y_distance:
            self.x_speed = -self.speed_factor
            self.y_speed = self.speed_factor
            self.direction = "down_left"
        elif self.x_coord - gv.x_coord < -self.x_distance and self.y_coord - gv.y_coord > self.y_distance:
            self.x_speed = self.speed_factor
            self.y_speed = -self.speed_factor
            self.direction = "up_right"
        elif self.x_coord - gv.x_coord > self.x_distance and self.y_coord - gv.y_coord > self.y_distance:
            self.x_speed = -self.speed_factor
            self.y_speed = -self.speed_factor
            self.direction = "up_left"
        elif self.x_coord - gv.x_coord < -self.x_distance:
            self.x_speed = self.speed_factor
            self.y_speed = 0
            self.direction = "right"
        elif self.x_coord - gv.x_coord > self.x_distance:
            self.x_speed = -self.speed_factor
            self.y_speed = 0
            self.direction = "left"
        elif self.y_coord - gv.y_coord < -self.y_distance:
            self.x_speed = 0
            self.y_speed = self.speed_factor
            self.direction = "down"
        elif self.y_coord - gv.y_coord > self.y_distance:
            self.x_speed = 0
            self.y_speed = -self.speed_factor
            self.direction = "up"
        else:
            self.x_speed = 0
            self.y_speed = 0

    def check_direction(self):
        partial_val_x = int(gv.size[0] / 12)
        partial_val_y = int(gv.size[1] / 12)

        if self.x_coord < gv.x_coord and self.y_coord < gv.y_coord:
            self.direction = "down_right"
        elif self.x_coord > gv.x_coord and self.y_coord > gv.y_coord:
            self.direction = "up_left"
        elif self.x_coord < gv.x_coord and self.y_coord > gv.y_coord:
            self.direction = "up_right"
        elif self.x_coord > gv.x_coord and self.y_coord < gv.y_coord:
            self.direction = "down_left"

        if self.y_coord - partial_val_y - 60 < gv.y_coord < self.y_coord + partial_val_y \
                and self.x_coord < gv.x_coord:
            self.direction = "right"
        elif self.y_coord - partial_val_y - 60 < gv.y_coord < self.y_coord + partial_val_y \
                and self.x_coord > gv.x_coord:
            self.direction = "left"
        elif self.x_coord - partial_val_x - 20 < gv.x_coord < self.x_coord + partial_val_x \
                and self.y_coord < gv.y_coord:
            self.direction = "down"
        elif self.x_coord - partial_val_x - 20 < gv.x_coord < self.x_coord + partial_val_x \
                and self.y_coord > gv.y_coord:
            self.direction = "up"

    def get(self):
        return self.haunter
