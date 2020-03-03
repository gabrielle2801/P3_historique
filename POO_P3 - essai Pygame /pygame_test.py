from pygame.locals import *
from POO_P3 import Game
from POO_P3 import Player
from ressource import *

pygame.init()


window_title = "Save MacGyver"

window = pygame.display.set_mode(windows_surface)

pygame.display.set_caption(window_title)
game = Game()
user = Player(game)
