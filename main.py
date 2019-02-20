import pygame
import global_variables as gv
from fireball import FireBall
from forrest_parts import ForrestPart
from level_objects import LevelObject
from enemy import Haunter

#ff
"""
Notes
______________________

It can hold 10 ghost horizontally
eg: Haunter([50 + (70 * 0), 50]), Haunter([50 + (70 * 1), 50]) to Haunter([50 + (70 * 9), 50])
"""

"""
Bugs
______________________

1) Infinite balls will be moved to an unreached point.

Better Experience
______________________
2) Moltres Fire Ball should start from it's beak.
"""


# returns tuple of: min_player_width, min_player_height, max_player_width, max_player_height
def get_max_min_haunter_width_height():
    arr = ["down_right", "down_left", "up_right", "up_left", "right", "left", "down", "up"]
    widths = []
    heights = []
    for temp_dir in arr:
        fig = pygame.image.load("images/Haunter/" + temp_dir + "/" + temp_dir + "_1.png").convert_alpha()
        fig_width = fig.get_rect().width
        fig_height = fig.get_rect().height

        widths.append(fig_width)
        heights.append(fig_height)
    return min(widths), min(heights), max(widths), max(heights)


def change_player_move():
    global p_move_i, p_dir, p_moves, player, player_width, player_height, p_fact

    p_move_i = (p_move_i + 1) % 4
    player = pygame.image.load("images/Moltres/" + p_dir + "/"
                               + p_moves[p_move_i] + ".png").convert_alpha()
    player_width = player.get_rect().width
    player_height = player.get_rect().height
    player = pygame.transform.scale(player, (int(player_width * p_fact),
                                             int(player_height * p_fact)))


# returns tuple of: min_player_width, min_player_height, max_player_width, max_player_height
def get_max_min_player_width_height():
    global p_fact

    arr = ["down_right", "down_left", "up_right", "up_left", "right", "left", "down", "up"]
    widths = []
    heights = []
    for temp_dir in arr:
        fig = pygame.image.load("images/Moltres/" + temp_dir + "/" + temp_dir + "_1.png").convert_alpha()
        fig_width = fig.get_rect().width
        fig_height = fig.get_rect().height

        widths.append(fig_width)
        heights.append(fig_height)
    return min(widths), min(heights), max(widths), max(heights)


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
    global y_away_from_beginning, level_1_objects

    temp_num = 0

    if platform_dir == "up":
        temp_num = 3
    elif platform_dir == "down":
        temp_num = -3

    y_away_from_beginning += temp_num
    stairs_dim[1] += temp_num
    for temp_haunter in gv.haunters_level_1:
        if temp_haunter.is_alive:
            temp_haunter.y_coord += temp_num
    for temp_forrest_part in forrest_parts:
        temp_forrest_part.y_coord += temp_num

    if gv.level_num == 1:
        for l_1_object in level_1_objects:
            l_1_object.coords[1] += temp_num


def reset_level():
    global player_width, player_height, y_away_from_beginning, tree_dim, stairs_dim, \
        forrest_parts

    gv.x_coord, gv.y_coord = int(gv.size[0] / 2 - player_width), int(gv.size[1] * 0.75 - player_height)

    y_away_from_beginning = gv.size[1]

    tree_dim = [600, -150]

    stairs_dim = [int(gv.size[0] / 2),
                  y_away_from_beginning + 1 - (11 * 2 * ForrestPart("up").size_fact * 12) * level_loops_fact - 15]

    # Forrest

    forrest_parts = []

    # Left Level Parts
    for iterate_temp in range(12 * level_loops_fact):
        if iterate_temp == 0:
            forrest_part_temp = ForrestPart("down_left")
        else:
            forrest_part_temp = ForrestPart("left")
        forrest_part_temp.y_coord = y_away_from_beginning + 1 - ((iterate_temp + 1) * forrest_part_temp.size_fact * 24)
        forrest_parts.append(forrest_part_temp)

    # Right Level Parts
    for iterate_temp in range(12 * level_loops_fact):
        if iterate_temp == 0:
            forrest_part_temp = ForrestPart("down_right")
        else:
            forrest_part_temp = ForrestPart("right")
        forrest_part_temp.x_coord = gv.size[0] - forrest_part_temp.size_fact * 24
        forrest_part_temp.y_coord = y_away_from_beginning + 1 - ((iterate_temp + 1) * forrest_part_temp.size_fact * 24)
        forrest_parts.append(forrest_part_temp)

    # Down Level Parts
    for iterate_temp in range(15):
        forrest_part_temp = ForrestPart("down")
        forrest_part_temp.x_coord = (iterate_temp + 1) * forrest_part_temp.size_fact * 24
        forrest_part_temp.y_coord = y_away_from_beginning + 1 - (forrest_part_temp.size_fact * 24)
        forrest_parts.append(forrest_part_temp)

    # Center Level Parts
    for iterate_temp in range(15):
        for j in range(12 * level_loops_fact - 1):
            forrest_part_temp = ForrestPart("center")
            forrest_part_temp.x_coord = (iterate_temp + 1) * forrest_part_temp.size_fact * 24
            forrest_part_temp.y_coord = y_away_from_beginning + 1 - ((j + 2) * forrest_part_temp.size_fact * 24)
            forrest_parts.append(forrest_part_temp)

    # Up Level Parts
    for iterate_temp in range(15):
        forrest_part_temp = ForrestPart("up")
        forrest_part_temp.x_coord = (iterate_temp + 1) * forrest_part_temp.size_fact * 24
        forrest_part_temp.y_coord = y_away_from_beginning + 1 - (
                (11 + 1) * 2 * forrest_part_temp.size_fact * 12) * level_loops_fact
        forrest_parts.append(forrest_part_temp)

    # Up_Left and Up_Right Level Parts
    for iterate_temp in range(2):
        forrest_part_temp = None
        if iterate_temp == 0:
            forrest_part_temp = ForrestPart("up_left")
            forrest_part_temp.x_coord = 0
        elif iterate_temp == 1:
            forrest_part_temp = ForrestPart("up_right")
            forrest_part_temp.x_coord = 16 * forrest_part_temp.size_fact * 24
        forrest_part_temp.y_coord = y_away_from_beginning + 1 - (
                (11 + 1) * 2 * forrest_part_temp.size_fact * 12) * level_loops_fact
        forrest_parts.append(forrest_part_temp)


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BLUE_2 = (36, 68, 125)
GREEN_2 = (30, 102, 17)

# bullets.pop(bullets.index(bullet))

pygame.init()

gv.level_num = 1

# Set the width and height of the screen [width, height]
gv.size = (816, 574)
screen = pygame.display.set_mode(gv.size)

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

min_player_width, min_player_height, max_player_width, max_player_height = get_max_min_player_width_height()

# Loop until the user clicks the close button.
done = False

y_away_from_beginning = gv.size[1]

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

fireballs = []

gv.haunters_level_1 = []
gv.haunters_level_1.append(Haunter([50, 50]))
gv.haunters_level_1.append(Haunter([120, -500]))

min_haunter_width, min_haunter_height, gv.max_haunter_width, gv.max_haunter_height = get_max_min_haunter_width_height()

# Speed in pixels per frame
x_speed, y_speed = 0, 0

# Current position
gv.x_coord, gv.y_coord = int(gv.size[0] / 2 - player_width), int(gv.size[1] * 0.75 - player_height)

p_dir = "down"
p_moves = ["down_1", "down_2", "down_1", "down_3"]
p_move_i = 0

PLAYER_MOVE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PLAYER_MOVE_EVENT, 200)

HAUNTER_MOVE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(HAUNTER_MOVE_EVENT, 300)

# Level_1
forrest_parts = []
level_loops_fact = 6

st_fact = ForrestPart("up").size_fact * 1.5
stairs = pygame.image.load("images/stairs.png").convert_alpha()
stairs_width = stairs.get_rect().width
stairs_height = stairs.get_rect().height
stairs = pygame.transform.scale(stairs, (int(stairs_width * st_fact),
                                         int(stairs_height * st_fact)))
stairs_dim = [int(gv.size[0] / 2),
              y_away_from_beginning + 1 - (11 * 2 * ForrestPart("up").size_fact * 12) * level_loops_fact - 15]

dg_fact = 2.5

dead_ghost = None
dead_ghost_counter = 0

pressed_keys = []

# Level Objects

# Level 1
level_1_objects = []
level_1_objects.append(LevelObject("tree.png", [550, 10], 1.8))

y_away_from_beginning_max = (gv.size[1] + 2) * level_loops_fact

level_display_font = pygame.font.SysFont("Serif", 35, True, False)

level_display_counter = 0

reset_level()

score = 0

score_display_font = pygame.font.SysFont("Serif", 25, True, False)

# Start Screen Background
start_screen_image = pygame.image.load("images/start_screen.png").convert_alpha()
start_screen_image = pygame.transform.scale(start_screen_image, gv.size)

is_start_screen = True

is_pause = False

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == PLAYER_MOVE_EVENT:  # is called every 't' milliseconds
            change_player_move()

        if event.type == HAUNTER_MOVE_EVENT:
            for haunter in gv.haunters_level_1:
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

                if gv.x_coord > gv.size[0] - 40:
                    gv.x_coord = gv.size[0] - 40

                if event.key == pygame.K_SPACE:
                    fb_sound.play()

                    fireball_1 = FireBall()

                    add_n = 89
                    fireball_1.x_coord, fireball_1.y_coord = gv.x_coord + add_n, gv.y_coord + add_n

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
        # Let Haunters Move
        for haunter in gv.haunters_level_1:
            if not haunter.can_move:
                if haunter.y_coord > 0:
                    haunter.can_move = True

        # Haunter AI
        for haunter in gv.haunters_level_1:
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

            if haunter.can_move:
                haunter.x_coord += haunter.x_speed
                haunter.y_coord += haunter.y_speed

            for l1 in level_1_objects:
                if l1.coords[1] - 35 < haunter.y_coord + gv.max_haunter_height < l1.coords[1] + l1.height and \
                        l1.coords[0] - 45 < haunter.x_coord + gv.max_haunter_width < l1.coords[0] + l1.width + 30:
                    haunter.x_coord -= haunter.x_speed
                    haunter.y_coord -= haunter.y_speed

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # Move the object according to the speed vector.
        # Also move the whole level and limit the player at x axis.
        if 40 <= gv.x_coord <= gv.size[0] - 175:
            gv.x_coord += x_speed
        elif gv.x_coord < 40:
            gv.x_coord = 40
        else:
            gv.x_coord = gv.size[0] - 175

        if y_speed == -3:
            if y_away_from_beginning > y_away_from_beginning_max:
                if gv.y_coord >= 16:
                    gv.y_coord += y_speed
                else:
                    gv.y_coord = 16
            else:
                if gv.y_coord > int(gv.size[1] * 0.15):
                    gv.y_coord += y_speed
                else:
                    move_platform("up")
        if y_speed == 3:
            if y_away_from_beginning < gv.size[1]:
                if gv.y_coord <= gv.size[1] - 175:
                    gv.y_coord += y_speed
                else:
                    gv.y_coord = gv.size[1] - 175
            else:
                if gv.y_coord < int(gv.size[1] * 0.6):
                    gv.y_coord += y_speed
                else:
                    move_platform("down")
        for l1 in level_1_objects:
            if l1.coords[1] - 75 < gv.y_coord + max_player_height < l1.coords[1] + l1.height and \
                    l1.coords[0] - 70 < gv.x_coord + max_player_width < l1.coords[0] + l1.width + 50:
                gv.x_coord -= x_speed
                gv.y_coord -= y_speed

        # Check for level change
        if stairs_dim[0] - 80 < gv.x_coord < stairs_dim[0] - 20 and \
                stairs_dim[1] - 70 < gv.y_coord < stairs_dim[1] - 50 and gv.level_num < 3:
            gv.level_num += 1
            level_display_counter = 0
            reset_level()

    # Screen Projection
    if is_start_screen:
        screen.blit(start_screen_image, (0, 0))
        text1 = level_display_font.render('Press Enter to start', True, WHITE)
        screen.blit(text1, [gv.size[1] / 2 - 25, gv.size[0] / 4])
    elif is_pause:
        text1 = level_display_font.render('Pause', True, WHITE)
        screen.blit(text1, [gv.size[1] / 2 + 75, gv.size[0] / 4])
    elif level_display_counter < 120:  # 2 seconds
        screen.fill(BLACK)
        text1 = level_display_font.render('Level: ' + str(gv.level_num), True, WHITE)
        screen.blit(text1, [gv.size[1] / 2 + 50, gv.size[0] / 4])
        level_display_counter += 1
    else:
        screen.fill(BLACK)

        for forrest_part in forrest_parts:
            screen.blit(forrest_part.get(), [forrest_part.x_coord, forrest_part.y_coord])

        screen.blit(stairs, stairs_dim)

        if gv.level_num == 1:
            for level_1_object in level_1_objects:
                screen.blit(level_1_object.get(), level_1_object.coords)

        for fireball in fireballs:
            if -50 < fireball.x_coord < gv.size[0] + 50 and -50 < fireball.y_coord < gv.size[1] + 50:
                fireball.x_coord += fireball.x_speed
                fireball.y_coord += fireball.y_speed
                screen.blit(fireball.get(), [fireball.x_coord, fireball.y_coord])

            # Check if Haunters are going to be killed.
            for haunter in gv.haunters_level_1:
                temp_val_x = haunter.x_coord + int(haunter.width) / 2
                temp_val_y = haunter.y_coord + int(haunter.height) / 2
                if temp_val_x - 30 < fireball.x_coord < temp_val_x + 30 and \
                        temp_val_y - 30 < fireball.y_coord < temp_val_y + 30 and \
                        haunter.is_alive:
                    haunter.is_alive = False
                    score += 100
                    dead_ghost_counter = 1
                    fireball.x_coord = gv.size[0] + 55
                    fireball.y_coord = gv.size[1] + 55
                    x_appear = haunter.x_coord - 40
                    y_appear = haunter.y_coord - 10
                    if 0 < dead_ghost_counter <= 4:
                        change_dead_ghost()
                        screen.blit(dead_ghost, [x_appear, y_appear])

            for l1 in level_1_objects:
                if l1.coords[0] - 10 < fireball.x_coord < l1.coords[0] + l1.width + 10 and \
                        l1.coords[1] - 10 < fireball.y_coord < l1.coords[1] + l1.height + 10:
                    fireball.x_coord = gv.size[0] + 55
                    fireball.y_coord = gv.size[1] + 55

        for haunter in gv.haunters_level_1:
            if haunter.is_alive and gv.level_num == 1:
                screen.blit(haunter.get(), [haunter.x_coord, haunter.y_coord])

        screen.blit(player, [gv.x_coord, gv.y_coord])

        score_text = score_display_font.render('Score: ' + str(score), True, WHITE)
        screen.blit(score_text, [gv.size[0] - 170, 10])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
