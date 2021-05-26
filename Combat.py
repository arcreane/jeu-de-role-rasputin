import random
import tkinter as tk

master = tk.Tk()
master.configure(bg='#92f7cb')  # couleur de fond d'ecran
master.geometry("640x480")  # taille par defaut
master.minsize(width="640", height="480")  # taille min
master.maxsize(width="640", height="480")  # taille max

# Stats randoms pour l'instant Ã  lier avec les stats du hero de l'editeurs
Attack = 10
Defense = 10
niveauMonstre = random.randint(1, 20)
PvHero = 10 + Defense * 10
PvMonstre = niveauMonstre * 20
DegatsMonstre = niveauMonstre * 2
DegatsHero = 5 + Attack
Agilite = 5
Luck = 10

def Attaquer():
    global PvMonstre,PvHero,Luck,Agilite,DegatsHero,DegatsMonstre
    ToucherHero = random.randint(1, 200)  # Chance que tu touche le monstre + Chance que tu l'esquive
    ToucherMonstre = random.randint(1, 200)

    if (ToucherHero < (80 + Luck)):
        PvMonstre = (PvMonstre - DegatsHero)
        print(PvMonstre)

    if (ToucherMonstre < (80 - Agilite)):
        PvHero = (PvHero - DegatsMonstre)

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
    global PvMonstre,PvHero,Luck,Agilite,DegatsHero,DegatsMonstre
    Partir = random.randint(1, 200)
    ToucherMonstre = random.randint(1, 200)
    if (Partir < 120 - Luck):  # Chance de fuir
        print("fuir")
    else:
        if (ToucherMonstre < 80 - Agilite):
            PvHero = PvHero - DegatsMonstre
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
