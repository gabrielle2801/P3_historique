from random import randint
from pprint import pprint

from constants import MAX_NUMBER_ITEM, WEAPONS_LIST


class Game:

    X_SIZE = 4
    Y_SIZE = 7

    def __init__(self):

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
        running = True
        while running:
            option = str(
                input("press a key u->up, d->down, r->right, l->left "))

            if option not in ("udrlq") or option == "q":
                return exit()

            if option == "d":
                self.player.move_down()
            elif option == "u":
                self.player.move_up()
            elif option == "r":
                self.player.move_rigth()
            elif option == "l":
                self.player.move_left()

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
        pprint(self.matrix)

    def update_maze(self, new_position):
        old_y, old_x = self.old_player_position
        y_axe, x_axe = new_position
        if x_axe < 0 or y_axe < 0 or x_axe >= Game.X_SIZE or\
                y_axe >= Game.Y_SIZE:
            print("can not move, try again")
        elif self.matrix[y_axe][x_axe] in ("+"):
            print("It's a wall, try again")
        else:
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
            return exit()
        else:
            print("YOU WIN !!!")
            return exit()


class Player:

    def __init__(self, game):
        self.game = game
        self.list_collect = 0

    def move_up(self):
        self.game.player_position[0] -= 1
        self.game.update_maze(self.game.player_position)
        pprint(self.game.matrix)

    def move_down(self):
        self.game.player_position[0] += 1
        self.game.update_maze(self.game.player_position)
        pprint(self.game.matrix)

    def move_left(self):
        self.game.player_position[1] -= 1
        self.game.update_maze(self.game.player_position)
        pprint(self.game.matrix)

    def move_rigth(self):
        self.game.player_position[1] += 1
        self.game.update_maze(self.game.player_position)
        pprint(self.game.matrix)

    def has_all_items(self):
        return self.list_collect == MAX_NUMBER_ITEM

    def collect_item(self, position_items):
        y_axe, x_axe = position_items

        if self.game.matrix[y_axe][x_axe] in WEAPONS_LIST:
            self.list_collect += 1
            print("You have got :", self.list_collect)
            pprint(self.game.matrix)
            self.game.matrix[y_axe][x_axe] = "-"


game = Game()
