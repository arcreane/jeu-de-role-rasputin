import random
import tkinter as tk

master = tk.Tk()
master.configure(bg='#92f7cb')  # couleur de fond d'ecran
master.geometry("640x480")  # taille par defaut
master.minsize(width="640", height="480")  # taille min
master.maxsize(width="640", height="480")  # taille max

# Stats randoms pour l'instant Ã  lier avec les stats du hero de l'editeurs
Attack = 8
Defense = 7
niveauMonstre = random.randint(1, 20)
PvHero = 10 + Defense * 10
PvMonstre = niveauMonstre * 10
DegatsMonstre = niveauMonstre
DegatsHero = 5 + Attack
Agilite = 5
Luck = 10
titre = 0

def Attaquer():
    global PvMonstre,PvHero,Luck,Agilite,DegatsHero,DegatsMonstre,titre,titre_label,pv_label
    ToucherHero = random.randint(1, 200)  # Chance que tu touche le monstre + Chance que tu l'esquive
    ToucherMonstre = random.randint(1, 200)
    if titre == 1 :
       titre_label.destroy()
       pv_label.destroy()

    if (ToucherHero < (70 + Luck)):
        PvMonstre = (PvMonstre - DegatsHero)
    if PvMonstre < 1 :
        print("tu gagnes")
        #Quitter le combat
        master.destroy()
    if (ToucherMonstre < (70 - Agilite)):
        PvHero = (PvHero - DegatsMonstre)
    if PvHero < 1 :
        #fin du jeu
        print("t'es mort")
        master.destroy()

    titre = 1
    titre_label = tk.Label(master, text=PvMonstre, background="#fc9403",
                           # Affichage PV Monstre et hero ( flemme de positionner pour l'instant )
                           disabledforeground="#a3a3a3",
                           font="-family {Segoe UI} -size 24 -weight bold -underline 1", foreground="#000000",
                           compound="center")
    titre_label.pack()
    pv_label = tk.Label(master, text=PvHero, background="#fc9403",
                           disabledforeground="#a3a3a3",
                           font="-family {Segoe UI} -size 24 -weight bold -underline 1", foreground="#000000",
                           compound="center")
    pv_label.pack()

    return PvMonstre,PvHero


def Fuir():
    global PvMonstre,PvHero,Luck,Agilite,DegatsHero,DegatsMonstre,titre,titre_label,pv_label
    Partir = random.randint(1, 200)
    ToucherMonstre = random.randint(1, 200)
    if titre == 1 :
       titre_label.destroy()
       pv_label.destroy()
    if (Partir < 130 - Luck):  # Chance de fuir
        print("fuir")
    else:
        if (ToucherMonstre < 65 - (Agilite+Luck)):
            PvHero = PvHero - DegatsMonstre
            titre = 1
            titre_label = tk.Label(master, text=PvMonstre, background="#fc9403",
                                   # Affichage PV Monstre et hero ( flemme de positionner pour l'instant )
                                   disabledforeground="#a3a3a3",
                                   font="-family {Segoe UI} -size 24 -weight bold -underline 1", foreground="#000000",
                                   compound="center")
            titre_label.pack()
            pv_label = tk.Label(master, text=PvHero, background="#fc9403",
                                   disabledforeground="#a3a3a3",
                                   font="-family {Segoe UI} -size 24 -weight bold -underline 1", foreground="#000000",
                                   compound="center")
            pv_label.pack()
    return PvMonstre,PvHero


bouton_attaquer = tk.Button(master, text='''Attaquer''', command= Attaquer, activebackground="#ececec",  # Boutons choix
                            activeforeground="#000000", background="#3ca253", disabledforeground="#a3a3a3",
                            font="-family {Segoe UI} -size 14", foreground="#000000", highlightbackground="#d9d9d9",
                            highlightcolor="black", pady="0")
bouton_attaquer.pack()
bouton_Fuir = tk.Button(master, text='''Fuir''', command=Fuir, activebackground="#ececec",
                        activeforeground="#000000", background="#3ca253", disabledforeground="#a3a3a3",
                        font="-family {Segoe UI} -size 14", foreground="#000000", highlightbackground="#d9d9d9",
                        highlightcolor="black", pady="0")
bouton_Fuir.pack()

master.mainloop()
