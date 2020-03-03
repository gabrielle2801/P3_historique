import pygame

sprites_lines = 4 * 44
sprites_columms = 7 * 44
windows_surface = (sprites_lines, sprites_columms)
window = pygame.display.set_mode(windows_surface)
rect_window = window.get_rect()
pygame.display.set_caption("Save MacGyver")

floor_image = pygame.transform.scale(
    pygame.image.load('ressource/Floor.png'), (44, 44))
wall_image = pygame.transform.scale(
    pygame.image.load('ressource/Wall3.png'), (44, 44))

player_image = pygame.transform.scale(
    pygame.image.load('ressource/MacGyver.png'), (44, 44))
guardian_image = pygame.transform.scale(
    pygame.image.load('ressource/Gardien.png'), (44, 44))
needle_image = pygame.transform.scale(
    pygame.image.load('ressource/aiguille.png'), (44, 44))
pipe_image = pygame.transform.scale(
    pygame.image.load('ressource/tube_plastique.png'), (44, 44))
ether_image = pygame.transform.scale(
    pygame.image.load('ressource/ether.png'), (44, 44))
