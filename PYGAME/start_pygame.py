from pygame.locals import *
from POO_P3_pygame import Game, Player
from constants import MAX_NUMBER_ITEM, WEAPONS_LIST

from ressource import *

pygame.init()


window_title = "Save MacGyver"

window = pygame.display.set_mode(windows_surface)


pygame.display.set_caption(window_title)
game = Game()
user = Player(game)
