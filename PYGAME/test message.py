# font_helvetica = pygame.font.SysFont("helvetica light", 30)
    self.message = font.render(
        "TEST MESSAGE", False, pygame.Color("#ff0000"))
    message_rect = self.message.get_rect()
    message_rect.center = rect_window.center
    window.blit(self.message, message_rect)
    clock.tick(30)
    pygame.display.update()
