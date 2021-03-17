import pygame
print("Bienvenue dans le jeu dont vous etes le hero ! /n Vous etes actuellement en train de jouer le jeu cree par:", name)
a= position x gauche objet
b= position x droite objet
c= position y haut objet
d=position y bas objet
def leftclick():
for event in pygame.event.get()
    if event.type == MOUSEBUTTONDOWN: #récupération des évenements lié à un clic de souris
        if event.button == 1: # parmis ceux précédent je prend le clic gauche
           x,y = pygame.mouse.get_pos()
           if b>x>a and d>y>c :
               return True
           else:
               return False
