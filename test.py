import tkinter as tk
import csv

# creation des listes pour l'histoire
titre = []
choix1 = []
choix2 = []
goto1 = []
goto2 = []

# ouverture et lecture du fichier csv de l'histoire
f = open("Classeur1.csv", "rt", encoding='utf-8-sig')

csv_f = csv.DictReader(f, delimiter=";")

for col in csv_f:
    titre.append(col['titre'])
    choix1.append(col['choix1'])
    choix2.append(col['choix2'])
    goto1.append(col['goto1'])
    goto2.append(col['goto2'])

# fermeture du fichier csv
f.close()

# Création de la fenetre avec tkinter
master = tk.Tk()
master.configure(bg='#92f7cb')  # couleur de fond d'écran
master.geometry("640x480")  # taille par défaut
master.minsize(width="640", height="480")  # taille min
master.maxsize(width="640", height="480")  # taille max


def begin_game(index):  # fonction du "moteur de jeu"
    frame2 = tk.Frame(master, bg="#92f7cb")  # creer une deuxieme frame
    frame2.pack(anchor="center")

    def clearFrame():  # fonction pour enlever les widgets des frames
        for widget in frame1.winfo_children():
            widget.destroy()
        for widget in frame2.winfo_children():
            widget.destroy()

    def debut_histoire():  # fonction pour afficher le premier titre de l'histoire avec ses choix
        clearFrame()
        titre1 = tk.Label(frame2, text=titre[0], bg='#92f7cb', font=("Arial", 15, "bold"))
        titre1.pack(anchor="center")

        choix1_bouton = tk.Button(frame2, text="choix1", command=lambda: choix1_reponse(index))
        choix1_bouton.pack()

        choix1_label = tk.Label(frame2, text=choix1[0])
        choix1_label.pack()

        choix2_bouton = tk.Button(frame2, text="choix2", command=lambda: choix2_reponse(index))
        choix2_bouton.pack()

        choix2_label = tk.Label(frame2, text=choix2[0])
        choix2_label.pack()

    def choix1_reponse(index):  # fonction pour changer l'index si le choix 1 est pris
        index = int(goto1[index]) - 1
        print(index)
        choix_apres(index)
        return index

    def choix2_reponse(index):  # fonction pour changer l'index si le choix 2 est pris
        index = int(goto2[index]) - 1
        print(index)
        choix_apres(index)
        return index

    def choix_apres(index):  # fonction pour afficher les titres et choix apres la premiere fois
        clearFrame()

        titre2 = tk.Label(frame2, text=titre[index], bg='#92f7cb', font=("Arial", 15, "bold"))
        titre2.pack()

        choix1_bouton = tk.Button(frame2, text=choix1[index], command=lambda: choix1_reponse(index))
        choix1_bouton.pack()

        # choix1_label = tk.Label(frame2, text=choix1[index])
        # choix1_label.pack()

        if choix1[index] == None:  # s'il n'ya rien alors on enleve ce widget
            # choix1_label.pack_forget()
            choix1_bouton.pack_forget()

        choix2_bouton = tk.Button(frame2, text=choix2[index], command=lambda: choix2_reponse(index))
        choix2_bouton.pack()

        # choix2_label = tk.Label(frame2, text=choix2[index])
        # choix2_label.pack()

        if choix2[index] == None:  # s'il n'ya rien alors on enleve ce widget
            # choix2_label.pack_forget()
            choix2_bouton.pack_forget()

        if str(titre[index]) == "fin":  # si le titre est "fin" alors affiche un bouton pour quitter
            retour_menu = tk.Button(frame2, text="Retour au menu", command=master.quit)
            retour_menu.pack()

    debut_histoire()


index = 0

title = tk.Label(text="Bienvenue dans DualCent !", bg="#92f7cb", font=("Arial", 20, "bold"), fg="black")  # titre
title.pack(side="top", pady=50)

frame1 = tk.Frame(master, bg="#92f7cb")  # créer une premiere frame
frame1.pack()

game = tk.Button(frame1, text="Démarrer l'histoire", background="green",
                 command=lambda: begin_game(index))  # Premier bouton pour jouer
game.grid(row="0", column="0", ipady=10, padx=10, pady=10)

menu_bar = tk.Menu(master)
file_menu = tk.Menu(menu_bar, tearoff=0)  # création du menu en haut de la page
file_menu.add_command(label="Quitter", command=master.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)
master.config(menu=menu_bar)

master.mainloop()
