import pygame
print("Bienvenue dans le jeu dont vous etes le hero ! /n Vous etes actuellement en train de jouer le jeu cree par:", name)

def leftclick():
pos = pygame.mouse.get_pos()
for event in pygame.event.get()
    if event.type == MOUSEBUTTONDOWN: #récupération des évenements lié à un clic de souris
        if event.button == 1: # parmis ceux précédent je prend le clic gauche
           x,y = pygame.mouse.get_pos()
           collide = object_rect.collidepoint(x,y)
           if collide:
               return True
           else:
               return False
          
