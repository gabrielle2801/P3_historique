from random import randint
from pprint import pprint
from pygame.locals import *
import pygame
from ressource import *
from constants import MAX_NUMBER_ITEM, WEAPONS_LIST


class Game(pygame.sprite.Sprite):

    X_SIZE = 4
    Y_SIZE = 7
    # print(windows_surface)

    def __init__(self):
        pygame.init()
        self.matrix = [
            [None for x in range(0, Game.X_SIZE)]
            for y in range(0, Game.Y_SIZE)
        ]
        self.player = Player(self)
        self.player_position = None
        self.old_player_position = (0, 0)
        self.load_file()
        self.load_items()
        self.start()

    def start(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()
                elif event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        self.player.move_down()
                    elif event.key == K_UP:
                        self.player.move_up()
                    elif event.key == K_RIGHT:
                        self.player.move_right()
                    elif event.key == K_LEFT:
                        self.player.move_left()
            self.display()
            self.check_win()

            clock.tick(30)

    def display(self):
        pygame.init()
        wall = wall_image.convert()
        floor = floor_image.convert()
        player = player_image.convert()
        guardian = guardian_image.convert()
        needle = needle_image.convert()
        pipe = pipe_image.convert()
        ether = ether_image.convert()

        for i in range(Game.Y_SIZE):
            for j in range(Game.X_SIZE):
                if self.matrix[i][j] == '+':
                    window.blit(wall, (j * 44, i * 44))
                elif self.matrix[i][j] == '-':
                    window.blit(floor, (j * 44, i * 44))
                elif self.matrix[i][j] == 'D':
                    window.blit(player, (j * 44, i * 44))
                elif self.matrix[i][j] == 'A':
                    window.blit(guardian, (j * 44, i * 44))
                elif self.matrix[i][j] == 'needle':
                    window.blit(needle, (j * 44, i * 44))
                elif self.matrix[i][j] == 'plastic_tube':
                    window.blit(pipe, (j * 44, i * 44))
                elif self.matrix[i][j] == 'ether':
                    window.blit(ether, (j * 44, i * 44))
                pygame.display.flip()

    def load_file(self):
        with open("maze.txt", 'r') as maze:
            for y_axe, line in enumerate(maze.readlines()):
                for x_axe, char in enumerate(line.strip()):
                    self.matrix[y_axe][x_axe] = char
                    if char == "D":
                        self.player_position = [y_axe, x_axe]

    def load_items(self):
        random_x = 0
        random_y = 0
        for art in WEAPONS_LIST:
            while self.matrix[random_y][random_x] != "-":
                random_x = randint(0, Game.X_SIZE - 1)
                random_y = randint(0, Game.Y_SIZE - 1)
            self.matrix[random_y][random_x] = art
        # pprint(self.matrix)

    def check_maze(self, new_position):
        old_y, old_x = self.old_player_position
        y_axe, x_axe = new_position

        if x_axe < 0 or y_axe < 0 or x_axe >= Game.X_SIZE or\
                y_axe >= Game.Y_SIZE:
            print("can not move, try again")
            self.player_position = [old_y, old_x]
            print(self.player_position)
        elif self.matrix[y_axe][x_axe] == "+":
            print("It's a wall, try again")
            self.player_position = [old_y, old_x]

    def update_maze(self, new_position):
        old_y, old_x = self.old_player_position
        y_axe, x_axe = new_position
        self.player.collect_item(new_position)
        self.check_win()
        self.matrix[old_y][old_x] = "-"
        self.matrix[y_axe][x_axe] = "D"
        self.old_player_position = y_axe, x_axe

    def check_win(self):
        y_axe, x_axe = self.player_position
        if not self.matrix[y_axe][x_axe] == "A":
            return

        if not self.player.has_all_items():
            result = MAX_NUMBER_ITEM - self.player.list_collect
            print("you loose, you miss ", result, "items")
            font = pygame.font.SysFont("helvetica.ttc", 15)
            message = font.render(
                "YOU LOOSE !!!", False, pygame.Color("#ff0000"))
            message_rect = message.get_rect()
            message_rect.center = rect_window.center
            window.blit(message, message_rect)
            pygame.display.flip()
            pygame.display.update()
            return exit()
        else:
            font = pygame.font.SysFont("helvetica bold.ttc", 30)
            message = font.render(
                "YOU WIN !!!", False, pygame.Color("#ff0000"))
            message_rect = message.get_rect()
            message_rect.center = rect_window.center
            window.blit(message, message_rect)
            pygame.display.flip()
            # pygame.display.update()
            print("YOU WIN !!!")
            # return exit()


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.init()
        self.game = game
        self.list_collect = 0

    def move_up(self):
        self.game.player_position[0] -= 1
        self.game.check_maze(self.game.player_position)
        self.game.update_maze(self.game.player_position)
        pprint(self.game.matrix)

    def move_down(self):
        self.game.player_position[0] += 1
        self.game.check_maze(self.game.player_position)
        self.game.update_maze(self.game.player_position)
        pprint(self.game.matrix)

    def move_left(self):
        self.game.player_position[1] -= 1
        self.game.check_maze(self.game.player_position)
        self.game.update_maze(self.game.player_position)
        pprint(self.game.matrix)

    def move_right(self):
        self.game.player_position[1] += 1
        self.game.check_maze(self.game.player_position)
        self.game.update_maze(self.game.player_position)
        pprint(self.game.matrix)

    def has_all_items(self):
        return self.list_collect == MAX_NUMBER_ITEM

    def collect_item(self, position_items):
        y_axe, x_axe = position_items
        if self.game.matrix[y_axe][x_axe] in WEAPONS_LIST:
            self.list_collect += 1
            # print("You have got :", self.list_collect)
            # pprint(self.game.matrix)
            self.game.matrix[y_axe][x_axe] = "-"


game = Game()
