from random import randint
from pprint import pprint
from ressource import *

from pygame.locals import *


class Game(pygame.sprite.Sprite):

    X_SIZE = 4
    Y_SIZE = 7
    print(windows_surface)

    def __init__(self):
        pygame.init()
        pygame.sprite.Sprite.__init__(self)

        self.matrix = [
            [None for x in range(0, Game.X_SIZE)]
            for y in range(0, Game.Y_SIZE)
        ]

        self.player_position = None
        self.load_file()
        self.display()
        self.load_items()

        # self.collect_item()

    def load_file(self):
        with open("maze.txt", 'r') as maze:
            for y_axe, line in enumerate(maze.readlines()):
                for x_axe, char in enumerate(line.strip()):
                    self.matrix[y_axe][x_axe] = char
                    if char == "D":
                        self.player_position = (y_axe, x_axe)

        pprint("bbbb")

    def display(self):
        wall = wall_image.convert()
        floor = floor_image.convert()
        player = player_image.convert()
        gardien = gardien_image.convert()
        pprint("aaaaaa")
        for i in range(Game.Y_SIZE):
            for j in range(Game.X_SIZE):
                if self.matrix[i][j] == '+':
                    window.blit(wall, (j * 44, i * 44))
                    pygame.display.flip()
                elif self.matrix[i][j] == '-':
                    window.blit(floor, (j * 44, i * 44))
                    pygame.display.flip()
                elif self.matrix[i][j] == 'D':
                    window.blit(player, (j * 44, i * 44))
                    pygame.display.flip()
                elif self.matrix[i][j] == 'A':
                    window.blit(gardien, (j * 44, i * 44))
                    pygame.display.flip()

    def load_items(self):
        list_i = ["needle", "plastic_tube", "ether"]
        aiguille = aiguille_image.convert()
        tube = tube_image.convert()
        ether = ether_image.convert()
        random_x = 0
        random_y = 0
        for art in list_i:
            while self.matrix[random_y][random_x] != "-":
                random_x = randint(0, Game.X_SIZE - 1)
                random_y = randint(0, Game.Y_SIZE - 1)
            self.matrix[random_y][random_x] = art
            if self.matrix[random_y][random_x] == 'needle':
                window.blit(aiguille, (random_x * 44, random_y * 44))
            elif self.matrix[random_y][random_x] == 'plastic_tube':
                window.blit(tube, (random_x * 44, random_y * 44))
            elif self.matrix[random_y][random_x] == 'ether':
                window.blit(ether, (random_x * 44, random_y * 44))
            pygame.display.flip()

    def collect_item(self):
        aiguille = aiguille_image.convert()
        tube = tube_image.convert()
        ether = ether_image.convert()
        position_needle = aiguille.get_rect()
        position_pipeline = tube.get_rect()
        position_ether = ether.get_rect()

        y_axe = 0
        x_axe = 0
        list_i = ["needle", "plastic_tube", "ether"]
        self.list_collect = 0
        self.numbers = 3
        result = 0
        if self.matrix[y_axe][x_axe]\
                in list_i:
            self.list_collect += 1
            print("You have got :", self.list_collect)
            # pprint(self.game.matrix)
            self.game.matrix[y_axe][x_axe] == "-"
        elif self.matrix[y_axe][x_axe] == "A" and\
                self.list_collect < self.numbers:
            result = self.numbers - self.list_collect
            print("you loose, you miss ", result, "items")
            return exit()
        elif self.matrix[y_axe][x_axe] == "A" \
                and self.list_collect == self.numbers:
            print("YOU WIN !!!")
            return exit()

        pprint(self.matrix)

    def update_maze(self, new_position):
        old_y, old_x = self.player_position
        y_axe, x_axe = new_position
        if x_axe < 0 or y_axe < 0 or x_axe >= Game.X_SIZE or\
                y_axe >= Game.Y_SIZE:
            print("can not move, try again")
        elif self.matrix[y_axe][x_axe] in ("+"):
            print("It's a wall, try again")
        else:
            self.matrix[old_y][old_x] = "-"
            self.matrix[y_axe][x_axe] = "D"
            self.player_position = new_position


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.init()
        self.game = game

        self.floor = floor_image.convert()
        self.player = player_image.convert()
        self.position = self.player.get_rect()
        self.move()

    def move(self):
        running = True
        window.blit(self.player, self.position)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                elif event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        self.old_position = self.position
                        self.position = self.position.move(0, 44)
                        # self.game.collect_item()
                        # self.game.update_maze()
                        window.blit(self.floor, self.old_position)
                        window.blit(self.player, self.position)
                        pygame.display.update()
                    if event.key == K_UP:
                        self.old_position = self.position
                        self.position = self.position.move(0, -44)
                        # self.game.collect_item()
                        # self.game.update_maze()
                        window.blit(self.floor, self.old_position)
                        window.blit(self.player, self.position)
                        pygame.display.update()
                    if event.key == K_RIGHT:
                        self.old_position = self.position
                        self.position = self.position.move(44, 0)
                        # self.game.collect_item()
                        # self.game.update_maze()
                        window.blit(self.floor, self.old_position)
                        window.blit(self.player, self.position)
                        pygame.display.update()
                    if event.key == K_LEFT:
                        self.old_position = self.position
                        self.position = self.position.move(-44, 0)
                        # self.game.collect_item()
                        # self.game.update_maze()
                        window.blit(self.floor, self.old_position)
                        window.blit(self.player, self.position)
                        pygame.display.update()

    # def load_items(self):
        # list_i = ["needle", "plastic_tube", "ether"]
        # random_x = 0
        # random_y = 0
        # for art in list_i:
        # while self.matrix[random_y][random_x] != "-":
        # random_x = randint(0, Game.X_SIZE - 1)
        # random_y = randint(0, Game.Y_SIZE - 1)
        # self.matrix[random_y][random_x] = art
        # pprint(self.matrix)
