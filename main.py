import pygame

pygame.init()
fenetre = pygame.display.set_mode((640, 480), pygame.RESIZABLE)

fond = pygame.image.load("./exemple/background.jpg").convert()
continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0
    fenetre.blit(fond, (0, 0))

    pygame.display.flip()
pygame.quit()
