from POO_P3 import game


class Player():

    def __init__(self, game):
        self.game = game
        self.list_collect = 0
        self.article = 3
        self.player_position = game.player_position
        self.new_position = (0, 0)
        self.move()

    def move(self):
        running = True
        x_axe, y_axe = self.new_position
        # self.player_position = self.game.x_axe, self.game.y_axe
        # 0,0
        while running:
            option = str(
                input("press a key u->up, d->down, r->right, l->left "))
            if option == "d":
                x_axe += 1
                new_position = (x_axe, y_axe)
                self.game.update_maze(new_position)
                pprint(self.game.matrix)

                # if self.game.can_i_move_to(x_axe, y_axe):

            elif option == "u":
                # if self.game.can_i_move_to(x_axe, y_axe):
                x_axe -= 1
                new_position = (x_axe, y_axe)
                self.game.update_maze(new_position)
                pprint(self.game.matrix)

            elif option == "r":
                # if self.game.can_i_move_to(x_axe, y_axe):
                y_axe += 1
                new_position = (x_axe, y_axe)
                self.game.update_maze(new_position)
                pprint(self.game.matrix)

            elif option == "l":
                # if self.game.can_i_move_to(x_axe, y_axe):
                y_axe -= 1
                new_position = (x_axe, y_axe)
                self.game.update_maze(new_position)
                pprint(self.game.matrix)

            elif option == "q":
                return exit()
            # else: raise exception (other letters or wall)
