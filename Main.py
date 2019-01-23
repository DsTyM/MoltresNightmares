"""
Bugs
______________________

1) Infinite balls will be moved to an unreached point.

Better Experience
______________________
2) Moltres Fire Ball should start from it's beak.
"""

# Test Comment
# Second Test Comment

import pygame
import random


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


class ForrestPart:
    def __init__(self, forrest_direction=""):
        global level_num

        self.rand_num_1 = random.randint(1, 2)
        self.rand_num_2 = random.randint(1, 2)
        self.size_fact = 2
        if self.rand_num_1 == 1 and forrest_direction in ("left", "down", "right", "up"):
            self.source = pygame.image.load("images/Levels/Level_" + str(level_num) + "/alt_2/" +
                                            forrest_direction + ".png").convert_alpha()
        elif self.rand_num_1 == 1 and forrest_direction == "center":
            self.source = pygame.image.load("images/Levels/Level_" + str(level_num) + "/alt_2/"
                                            + forrest_direction + "_" + str(self.rand_num_2) + ".png").convert_alpha()
        else:
            self.source = pygame.image.load("images/Levels/Level_" + str(level_num) + "/alt_1/"
                                            + forrest_direction + ".png").convert_alpha()
        self.width = self.source.get_rect().width
        self.height = self.source.get_rect().height
        self.x_coord, self.y_coord = 0, 0

    def get(self):
        return pygame.transform.scale(self.source, (int(self.width * self.size_fact),
                                                    int(self.height * self.size_fact)))


class Haunter:
    def __init__(self):
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
        self.x_coord, self.y_coord = -60, -60

        self.direction = "down"
        self.moves = ["down_1", "down_2", "down_1", "down_3"]
        self.move_step = random.randint(0, 3)

        self.x_distance = 180
        self.y_distance = 250

        self.old_x_speed = self.x_speed
        self.old_y_speed = self.y_speed

        self.speed_factor = 3

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
        global x_coord, y_coord

        if self.x_coord - x_coord < -self.x_distance and self.y_coord - y_coord < -self.y_distance:
            self.x_speed = self.speed_factor
            self.y_speed = self.speed_factor
            self.direction = "down_right"
        elif self.x_coord - x_coord > self.x_distance and self.y_coord - y_coord < -self.y_distance:
            self.x_speed = -self.speed_factor
            self.y_speed = self.speed_factor
            self.direction = "down_left"
        elif self.x_coord - x_coord < -self.x_distance and self.y_coord - y_coord > self.y_distance:
            self.x_speed = self.speed_factor
            self.y_speed = -self.speed_factor
            self.direction = "up_right"
        elif self.x_coord - x_coord > self.x_distance and self.y_coord - y_coord > self.y_distance:
            self.x_speed = -self.speed_factor
            self.y_speed = -self.speed_factor
            self.direction = "up_left"
        elif self.x_coord - x_coord < -self.x_distance:
            self.x_speed = self.speed_factor
            self.y_speed = 0
            self.direction = "right"
        elif self.x_coord - x_coord > self.x_distance:
            self.x_speed = -self.speed_factor
            self.y_speed = 0
            self.direction = "left"
        elif self.y_coord - y_coord < -self.y_distance:
            self.x_speed = 0
            self.y_speed = self.speed_factor
            self.direction = "down"
        elif self.y_coord - y_coord > self.y_distance:
            self.x_speed = 0
            self.y_speed = -self.speed_factor
            self.direction = "up"
        else:
            self.x_speed = 0
            self.y_speed = 0

    def check_direction(self):
        global x_coord, y_coord

        partial_val_x = int(size[0] / 12)
        partial_val_y = int(size[1] / 12)

        if self.x_coord < x_coord and self.y_coord < y_coord:
            self.direction = "down_right"
        elif self.x_coord > x_coord and self.y_coord > y_coord:
            self.direction = "up_left"
        elif self.x_coord < x_coord and self.y_coord > y_coord:
            self.direction = "up_right"
        elif self.x_coord > x_coord and self.y_coord < y_coord:
            self.direction = "down_left"
        if self.y_coord - partial_val_y < y_coord < self.y_coord + partial_val_y and self.x_coord < x_coord:
            self.direction = "right"
        elif self.y_coord - partial_val_y - 60 < y_coord < self.y_coord + partial_val_y and self.x_coord > x_coord:
            self.direction = "left"
        elif self.x_coord - partial_val_x - 20 < x_coord < self.x_coord + partial_val_x and self.y_coord < y_coord:
            self.direction = "down"
        elif self.x_coord - partial_val_x < x_coord < self.x_coord + partial_val_x and self.y_coord > y_coord:
            self.direction = "up"

    def get(self):
        return self.haunter


def change_player_move():
    global p_move_i, p_dir, p_moves, player, player_width, player_height

    p_move_i = (p_move_i + 1) % 4
    player = pygame.image.load("images/Moltres/" + p_dir + "/"
                               + p_moves[p_move_i] + ".png").convert_alpha()
    player_width = player.get_rect().width
    player_height = player.get_rect().height
    player = pygame.transform.scale(player, (int(player_width * p_fact),
                                             int(player_height * p_fact)))


def select_direction():
    global x_speed, y_speed, pressed_keys, p_dir, p_moves

    if pressed_keys[pygame.K_RIGHT] and pressed_keys[pygame.K_UP]:
        x_speed = 3
        y_speed = -3
        p_dir = "up_right"
        p_moves = [p_dir + "_1", p_dir + "_2", p_dir + "_1", p_dir + "_3"]
        change_player_move()
    elif pressed_keys[pygame.K_LEFT] and pressed_keys[pygame.K_UP]:
        x_speed = -3
        y_speed = -3
        p_dir = "up_left"
        p_moves = [p_dir + "_1", p_dir + "_2", p_dir + "_1", p_dir + "_3"]
        change_player_move()
    elif pressed_keys[pygame.K_LEFT] and pressed_keys[pygame.K_DOWN]:
        x_speed = -3
        y_speed = 3
        p_dir = "down_left"
        p_moves = [p_dir + "_1", p_dir + "_2", p_dir + "_1", p_dir + "_3"]
        change_player_move()
    elif pressed_keys[pygame.K_RIGHT] and pressed_keys[pygame.K_DOWN]:
        x_speed = 3
        y_speed = 3
        p_dir = "down_right"
        p_moves = [p_dir + "_1", p_dir + "_2", p_dir + "_1", p_dir + "_3"]
        change_player_move()
    elif pressed_keys[pygame.K_LEFT]:
        x_speed = -3
        p_dir = "left"
        p_moves = [p_dir + "_1", p_dir + "_2", p_dir + "_1", p_dir + "_3"]
        change_player_move()
    elif pressed_keys[pygame.K_RIGHT]:
        x_speed = 3
        p_dir = "right"
        p_moves = [p_dir + "_1", p_dir + "_2", p_dir + "_1", p_dir + "_3"]
        change_player_move()
    elif pressed_keys[pygame.K_UP]:
        y_speed = -3
        p_dir = "up"
        p_moves = [p_dir + "_1", p_dir + "_2", p_dir + "_1", p_dir + "_3"]
        change_player_move()
    elif pressed_keys[pygame.K_DOWN]:
        y_speed = 3
        p_dir = "down"
        p_moves = [p_dir + "_1", p_dir + "_2", p_dir + "_1", p_dir + "_3"]
        change_player_move()


def change_dead_ghost():
    # Dead Ghost
    global dead_ghost, dead_ghost_counter

    if 0 < dead_ghost_counter < 4:
        dead_ghost = pygame.image.load("images/dead_ghost/d" + str(dead_ghost_counter) +
                                       ".png").convert_alpha()
        dead_ghost_width = dead_ghost.get_rect().width
        dead_ghost_height = dead_ghost.get_rect().height
        dead_ghost = pygame.transform.scale(
            dead_ghost, (int(dead_ghost_width * dg_fact),
                         int(dead_ghost_height * dg_fact)))

    if 0 < dead_ghost_counter <= 4:
        dead_ghost_counter += 1


def move_platform(platform_dir=""):
    global y_away_from_beginning, tree_dim, haunters

    temp_num = 0

    if platform_dir == "up":
        temp_num = 3
    elif platform_dir == "down":
        temp_num = -3

    y_away_from_beginning += temp_num
    tree_dim[1] += temp_num
    stairs_dim[1] += temp_num
    for temp_haunter in haunters:
        if temp_haunter.is_alive:
            temp_haunter.y_coord += temp_num
    for temp_forrest_part in forrest_parts:
        temp_forrest_part.y_coord += temp_num


def reset_level():
    global x_coord, y_coord, size, player_width, player_height, y_away_from_beginning, tree_dim, stairs_dim, \
        forrest_parts

    x_coord, y_coord = int(size[0] / 2 - player_width), int(size[1] * 0.75 - player_height)

    y_away_from_beginning = size[1]

    tree_dim = [600, -150]

    stairs_dim = [int(size[0] / 2),
                  y_away_from_beginning + 1 - (11 * 2 * ForrestPart("up").size_fact * 12) * level_loops_fact - 15]

    # Forrest

    forrest_parts = []

    # Left Level Parts
    for i_temp in range(12 * level_loops_fact):
        if i_temp == 0:
            forrest_part_temp = ForrestPart("down_left")
        else:
            forrest_part_temp = ForrestPart("left")
        forrest_part_temp.y_coord = y_away_from_beginning + 1 - ((i_temp + 1) * forrest_part_temp.size_fact * 24)
        forrest_parts.append(forrest_part_temp)

    # Right Level Parts
    for i_temp in range(12 * level_loops_fact):
        if i_temp == 0:
            forrest_part_temp = ForrestPart("down_right")
        else:
            forrest_part_temp = ForrestPart("right")
        forrest_part_temp.x_coord = size[0] - forrest_part_temp.size_fact * 24
        forrest_part_temp.y_coord = y_away_from_beginning + 1 - ((i_temp + 1) * forrest_part_temp.size_fact * 24)
        forrest_parts.append(forrest_part_temp)

    # Down Level Parts
    for i_temp in range(15):
        forrest_part_temp = ForrestPart("down")
        forrest_part_temp.x_coord = (i_temp + 1) * forrest_part_temp.size_fact * 24
        forrest_part_temp.y_coord = y_away_from_beginning + 1 - (forrest_part_temp.size_fact * 24)
        forrest_parts.append(forrest_part_temp)

    # Center Level Parts
    for i_temp in range(15):
        for j in range(12 * level_loops_fact - 1):
            forrest_part_temp = ForrestPart("center")
            forrest_part_temp.x_coord = (i_temp + 1) * forrest_part_temp.size_fact * 24
            forrest_part_temp.y_coord = y_away_from_beginning + 1 - ((j + 2) * forrest_part_temp.size_fact * 24)
            forrest_parts.append(forrest_part_temp)

    # Up Level Parts
    for i_temp in range(15):
        forrest_part_temp = ForrestPart("up")
        forrest_part_temp.x_coord = (i_temp + 1) * forrest_part_temp.size_fact * 24
        forrest_part_temp.y_coord = y_away_from_beginning + 1 - (
                (11 + 1) * 2 * forrest_part_temp.size_fact * 12) * level_loops_fact
        forrest_parts.append(forrest_part_temp)

    # Up_Left and Up_Right Level Parts
    for i_temp in range(2):
        forrest_part_temp = None
        if i_temp == 0:
            forrest_part_temp = ForrestPart("up_left")
            forrest_part_temp.x_coord = 0
        elif i_temp == 1:
            forrest_part_temp = ForrestPart("up_right")
            forrest_part_temp.x_coord = 16 * forrest_part_temp.size_fact * 24
        forrest_part_temp.y_coord = y_away_from_beginning + 1 - (
                (11 + 1) * 2 * forrest_part_temp.size_fact * 12) * level_loops_fact
        forrest_parts.append(forrest_part_temp)


def split_haunters():
    global haunters

    for i_temp in range(len(haunters)):
        for j_temp in range(len(haunters)):
            if i_temp != j_temp:
                haunter_1 = haunters[i_temp]
                haunter_2 = haunters[j_temp]
                # x_coord, y_coord, width, height
                if haunter_1.x_coord < haunter_2.x_coord < haunter_1.x_coord + haunter_1.width \
                        and haunter_1.y_coord < haunter_2.y_coord < haunter_1.y_coord + haunter_1.height:
                    pass
                    # move to another direction
                    # avoid_haunter()



# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BLUE_2 = (36, 68, 125)
GREEN_2 = (30, 102, 17)

pygame.init()

level_num = 1

# Set the width and height of the screen [width, height]
size = (816, 574)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Moltres Nightmares")

logo_image = pygame.image.load("images/logo.png").convert_alpha()
pygame.display.set_icon(logo_image)

# theme_sound = pygame.mixer.Sound("sounds/theme_2.wav")
# theme_sound.set_volume(0.5)
# theme_sound.play(loops=-1)

fb_sound = pygame.mixer.Sound("sounds/FB_Sound.wav")
# change it to 0.3
fb_sound.set_volume(0.15)

# Player Initialization
p_fact = 2.5
player = pygame.image.load("images/Moltres/down/down_1.png").convert_alpha()
player_width = player.get_rect().width
player_height = player.get_rect().height
player = pygame.transform.scale(player, (int(player_width * p_fact),
                                         int(player_height * p_fact)))

# Loop until the user clicks the close button.
done = False

y_away_from_beginning = size[1]

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

fireballs = []

haunters = []
for i in range(5):
    h = Haunter()
    h.x_distance += (i + 1) * 65
    h.y_distance += (i + 1) * random.randint(-20, 20)
    h.x_coord += i * 60
    haunters.append(h)

# Speed in pixels per frame
x_speed, y_speed = 0, 0

# Current position
x_coord, y_coord = int(size[0] / 2 - player_width), int(size[1] * 0.75 - player_height)

p_dir = "down"
p_moves = ["down_1", "down_2", "down_1", "down_3"]
p_move_i = 0

PLAYER_MOVE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PLAYER_MOVE_EVENT, 200)

HAUNTER_MOVE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(HAUNTER_MOVE_EVENT, 300)

# Level_1
forrest_parts = []
level_loops_fact = 2

st_fact = ForrestPart("up").size_fact * 1.5
stairs = pygame.image.load("images/stairs.png").convert_alpha()
stairs_width = stairs.get_rect().width
stairs_height = stairs.get_rect().height
stairs = pygame.transform.scale(stairs, (int(stairs_width * st_fact),
                                         int(stairs_height * st_fact)))
stairs_dim = [int(size[0] / 2),
              y_away_from_beginning + 1 - (11 * 2 * ForrestPart("up").size_fact * 12) * level_loops_fact - 15]

dg_fact = 2.5

dead_ghost = None
dead_ghost_counter = 0

pressed_keys = []

# Tree Initialization
t_fact = 1.8
tree = pygame.image.load("images/tree.png").convert_alpha()
tree_width = tree.get_rect().width
tree_height = tree.get_rect().height
tree = pygame.transform.scale(tree, (int(tree_width * t_fact),
                                     int(tree_height * t_fact)))
tree_dim = [600, -150]

y_away_from_beginning_max = (size[1] + 2) * level_loops_fact

level_display_font = pygame.font.SysFont("Serif", 35, True, False)

level_display_counter = 0

reset_level()

score = 0

score_display_font = pygame.font.SysFont("Serif", 25, True, False)

# Start Screen Background
start_screen_image = pygame.image.load("images/start_screen.png").convert_alpha()
start_screen_image = pygame.transform.scale(start_screen_image, size)

is_start_screen = True

is_pause = False

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == PLAYER_MOVE_EVENT:  # is called every 't' milliseconds
            change_player_move()

        if event.type == HAUNTER_MOVE_EVENT:
            for haunter in haunters:
                haunter.change_haunter_move()

        if event.type == pygame.QUIT:
            done = True
            # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
            pressed_keys = pygame.key.get_pressed()
            # Figure out if it was an arrow key.
            # If so, adjust speed.

            if not is_start_screen and not is_pause:
                select_direction()

                if x_coord > size[0] - 40:
                    x_coord = size[0] - 40

                if event.key == pygame.K_SPACE:
                    fb_sound.play()

                    fireball_1 = FireBall()

                    add_n = 89
                    fireball_1.x_coord, fireball_1.y_coord = x_coord + add_n, y_coord + add_n

                    fb_speed_fact = 6

                    if p_dir == "down":
                        fireball_1.x_speed = 0
                        fireball_1.y_speed = fb_speed_fact
                    elif p_dir == "up":
                        fireball_1.x_speed = 0
                        fireball_1.y_speed = -fb_speed_fact
                    elif p_dir == "right":
                        fireball_1.x_speed = fb_speed_fact
                        fireball_1.y_speed = 0
                    elif p_dir == "left":
                        fireball_1.x_speed = -fb_speed_fact
                        fireball_1.y_speed = 0
                    elif p_dir == "down_right":
                        fireball_1.x_speed = fb_speed_fact
                        fireball_1.y_speed = fb_speed_fact
                    elif p_dir == "down_left":
                        fireball_1.x_speed = -fb_speed_fact
                        fireball_1.y_speed = fb_speed_fact
                    elif p_dir == "up_right":
                        fireball_1.x_speed = fb_speed_fact
                        fireball_1.y_speed = -fb_speed_fact
                    elif p_dir == "up_left":
                        fireball_1.x_speed = -fb_speed_fact
                        fireball_1.y_speed = -fb_speed_fact

                    fireballs.append(fireball_1)

            if event.key == pygame.K_p and not is_start_screen:
                is_pause = not is_pause

            if event.key == pygame.K_RETURN:
                if is_start_screen:
                    is_start_screen = False

        # User let up on a key
        elif event.type == pygame.KEYUP:
            pressed_keys = pygame.key.get_pressed()

            select_direction()

            # If this is an arrow key,
            # reset back to zero.
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0

    # --- Game logic should go here

    if not is_start_screen and not is_pause:
        # Haunter AI
        for haunter in haunters:
            haunter.old_x_speed = haunter.x_speed
            haunter.old_y_speed = haunter.y_speed

            haunter.check_direction()

            haunter.check_distance_to_player()

            haunter.moves = [haunter.direction + "_1", haunter.direction + "_2",
                             haunter.direction + "_1", haunter.direction + "_3"]

            if haunter.old_x_speed == 0 and haunter.x_speed != 0:
                haunter.change_haunter_move()
            elif haunter.old_y_speed == 0 and haunter.y_speed != 0:
                haunter.change_haunter_move()

            haunter.x_coord += haunter.x_speed
            haunter.y_coord += haunter.y_speed

        split_haunters()

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # Move the object according to the speed vector.
        # Also move the whole level and limit the player at x axis.
        if 40 <= x_coord <= size[0] - 175:
            x_coord += x_speed
        elif x_coord < 40:
            x_coord = 40
        else:
            x_coord = size[0] - 175

        if y_speed == -3:
            if y_away_from_beginning > y_away_from_beginning_max:
                if y_coord >= 16:
                    y_coord += y_speed
                else:
                    y_coord = 16
            else:
                if y_coord > int(size[1] * 0.15):
                    y_coord += y_speed
                else:
                    move_platform("up")
        if y_speed == 3:
            if y_away_from_beginning < size[1]:
                if y_coord <= size[1] - 175:
                    y_coord += y_speed
                else:
                    y_coord = size[1] - 175
            else:
                if y_coord < int(size[1] * 0.6):
                    y_coord += y_speed
                else:
                    move_platform("down")

        # Check for level change
        if stairs_dim[0] - 80 < x_coord < stairs_dim[0] - 20 and \
                stairs_dim[1] - 70 < y_coord < stairs_dim[1] - 50 and level_num < 3:
            level_num += 1
            level_display_counter = 0
            reset_level()

    # Screen Projection
    if is_start_screen:
        screen.blit(start_screen_image, (0, 0))
        text1 = level_display_font.render('Press Enter to start', True, WHITE)
        screen.blit(text1, [size[1] / 2 - 25, size[0] / 4])
    elif is_pause:
        text1 = level_display_font.render('Pause', True, WHITE)
        screen.blit(text1, [size[1] / 2 + 75, size[0] / 4])
    elif level_display_counter < 120:  # 2 seconds
        screen.fill(BLACK)
        text1 = level_display_font.render('Level: ' + str(level_num), True, WHITE)
        screen.blit(text1, [size[1] / 2 + 50, size[0] / 4])
        level_display_counter += 1
    else:
        screen.fill(BLACK)

        for forrest_part in forrest_parts:
            screen.blit(forrest_part.get(), [forrest_part.x_coord, forrest_part.y_coord])

        screen.blit(stairs, stairs_dim)

        screen.blit(tree, tree_dim)

        for fireball in fireballs:
            if -50 < fireball.x_coord < size[0] + 50 and -50 < fireball.y_coord < size[1] + 50:
                fireball.x_coord += fireball.x_speed
                fireball.y_coord += fireball.y_speed
                screen.blit(fireball.get(), [fireball.x_coord, fireball.y_coord])

            # Check if Haunters are going to be killed.
            for haunter in haunters:
                temp_val_x = haunter.x_coord + int(haunter.width) / 2
                temp_val_y = haunter.y_coord + int(haunter.height) / 2
                if temp_val_x - 30 < fireball.x_coord < temp_val_x + 30 and \
                        temp_val_y - 30 < fireball.y_coord < temp_val_y + 30 and \
                        haunter.is_alive:
                    haunter.is_alive = False
                    score += 100
                    dead_ghost_counter = 1
                    fireball.x_coord = size[0] + 55
                    fireball.y_coord = size[1] + 55
                    x_appear = haunter.x_coord - 40
                    y_appear = haunter.y_coord - 10
                    if 0 < dead_ghost_counter <= 4:
                        change_dead_ghost()
                        screen.blit(dead_ghost, [x_appear, y_appear])

        for haunter in haunters:
            if haunter.is_alive:
                screen.blit(haunter.get(), [haunter.x_coord, haunter.y_coord])

        screen.blit(player, [x_coord, y_coord])

        score_text = score_display_font.render('Score: ' + str(score), True, WHITE)
        screen.blit(score_text, [size[0] - 170, 10])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
