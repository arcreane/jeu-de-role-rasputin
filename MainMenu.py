import tkinter as tk
from tkinter import filedialog as fd
import pygame


def open_file_path():  # fonction qui permet de demander à l'utilisateur de choisir le fichier du jeu et qui affiche le boutton "suivant"
    filename = fd.askopenfilename()
    print(filename)
    file[0] = filename
    if len(file[0]) > 2:
        bouton_suivantfile.place(relx=0.604, rely=0.353, height=54, width=107)


def create_premier():  # fonction pour créer le premier menu
    Frame1 = tk.Frame(root)
    Frame1.place(relx=0.033, rely=0.044, relheight=0.233, relwidth=0.942)
    Frame1.configure(relief='groove')
    Frame1.configure(borderwidth="2")
    Frame1.configure(relief="groove")
    Frame1.configure(background="#80e1a7")

    label_acceuil = tk.Label(Frame1)
    label_acceuil.place(relx=0.017, rely=0.133, height=71, width=574)
    label_acceuil.configure(background="#80e1a7")
    label_acceuil.configure(disabledforeground="#a3a3a3")
    label_acceuil.configure(font="-family {Forte} -size 24 -weight bold -underline 1")
    label_acceuil.configure(foreground="#000000")
    label_acceuil.configure(highlightbackground="#f0f0f0f0f0f0")
    label_acceuil.configure(text='''Bienvenue sur DualCent''')

    Frame2 = tk.Frame(root)
    Frame2.place(relx=0.031, rely=0.289, relheight=0.567, relwidth=0.945)
    Frame2.configure(relief='groove')
    Frame2.configure(borderwidth="2")
    Frame2.configure(relief="groove")
    Frame2.configure(background="#80e1a7")

    bouton_jouer = tk.Button(Frame2, command=lambda: [create_deuxieme(), Frame1.place_forget(), Frame2.place_forget(),
                                                 label_credits.place_forget()])
    bouton_jouer.place(relx=0.083, rely=0.353, height=54, width=107)
    bouton_jouer.configure(activebackground="#ececec")
    bouton_jouer.configure(activeforeground="#000000")
    bouton_jouer.configure(background="#85b90b")
    bouton_jouer.configure(disabledforeground="#a3a3a3")
    bouton_jouer.configure(foreground="#000000")
    bouton_jouer.configure(highlightbackground="#d9d9d9")
    bouton_jouer.configure(highlightcolor="black")
    bouton_jouer.configure(pady="0")
    bouton_jouer.configure(text='''JOUER''')

    bouton_editer = tk.Button(Frame2, command=lambda : exec(open('graphicseditor.py').read()))
    bouton_editer.place(relx=0.413, rely=0.353, height=54, width=107)
    bouton_editer.configure(activebackground="#ececec")
    bouton_editer.configure(activeforeground="#000000")
    bouton_editer.configure(background="#85b90b")
    bouton_editer.configure(disabledforeground="#a3a3a3")
    bouton_editer.configure(foreground="#000000")
    bouton_editer.configure(highlightbackground="#d9d9d9")
    bouton_editer.configure(highlightcolor="black")
    bouton_editer.configure(pady="0")
    bouton_editer.configure(text='''EDITER''')

    bouton_quitter = tk.Button(Frame2, command=root.quit)
    bouton_quitter.place(relx=0.744, rely=0.353, height=54, width=107)
    bouton_quitter.configure(activebackground="#ececec")
    bouton_quitter.configure(activeforeground="#000000")
    bouton_quitter.configure(background="#85b90b")
    bouton_quitter.configure(disabledforeground="#a3a3a3")
    bouton_quitter.configure(foreground="#000000")
    bouton_quitter.configure(highlightbackground="#d9d9d9")
    bouton_quitter.configure(highlightcolor="black")
    bouton_quitter.configure(pady="0")
    bouton_quitter.configure(text='''QUITTER''')

    label_credits = tk.Label(root)
    label_credits.place(relx=0.719, rely=0.889, height=41, width=174)
    label_credits.configure(background="#bff2c7")
    label_credits.configure(disabledforeground="#a3a3a3")
    label_credits.configure(foreground="#000000")
    label_credits.configure(text='''Crée par Rasputin Team''')


def create_deuxieme():  # fonction pour créer la premiere fenetre apres le main menu
    global Frame3, bouton_suivantfile

    Frame3 = tk.Frame(root)
    Frame3.place(relx=0.031, rely=0.289, relheight=0.567, relwidth=0.945)
    Frame3.configure(relief='groove')
    Frame3.configure(borderwidth="2")
    Frame3.configure(relief="groove")
    Frame3.configure(background="#80e1a7")

    bouton_selectionfile = tk.Button(Frame3, command=open_file_path)
    bouton_selectionfile.place(relx=0.404, rely=0.353, height=54, width=107)
    bouton_selectionfile.configure(activebackground="#ececec")
    bouton_selectionfile.configure(activeforeground="#000000")
    bouton_selectionfile.configure(background="#85b90b")
    bouton_selectionfile.configure(disabledforeground="#a3a3a3")
    bouton_selectionfile.configure(foreground="#000000")
    bouton_selectionfile.configure(highlightbackground="#d9d9d9")
    bouton_selectionfile.configure(highlightcolor="black")
    bouton_selectionfile.configure(pady="0")
    bouton_selectionfile.configure(text='''Choisir un fichier :''')

    bouton_suivantfile = tk.Button(Frame3, command=create_troisieme)
    bouton_suivantfile.configure(activebackground="#ececec")
    bouton_suivantfile.configure(activeforeground="#000000")
    bouton_suivantfile.configure(background="#85b90b")
    bouton_suivantfile.configure(disabledforeground="#a3a3a3")
    bouton_suivantfile.configure(foreground="#000000")
    bouton_suivantfile.configure(highlightbackground="#d9d9d9")
    bouton_suivantfile.configure(highlightcolor="black")
    bouton_suivantfile.configure(pady="0")
    bouton_suivantfile.configure(text='''Suivant''')

    bouton_retour = tk.Button(Frame3, command=lambda: [Frame3.place_forget(), create_premier()])
    bouton_retour.place(relx=0.204, rely=0.353, height=54, width=107)
    bouton_retour.configure(activebackground="#ececec")
    bouton_retour.configure(activeforeground="#000000")
    bouton_retour.configure(background="#85b90b")
    bouton_retour.configure(disabledforeground="#a3a3a3")
    bouton_retour.configure(font="-family {Segoe UI} -size 12")
    bouton_retour.configure(foreground="#000000")
    bouton_retour.configure(highlightbackground="#d9d9d9")
    bouton_retour.configure(highlightcolor="black")
    bouton_retour.configure(pady="0")
    bouton_retour.configure(text='''Retour''')

def create_troisieme():  # fonction pour créer la dexieme fenetre apres le main menu (statistiques)
    Frame3.destroy()

    global scale_attaque, scale_defense, scale_agilite, scale_chance, Frame5, monTexte, label_update
    monTexte = tk.StringVar()
    monTexte.set("Il vous reste 30 points !")

    Frame4 = tk.Frame(root)
    Frame4.place(relx=0.017, rely=0.022, relheight=0.167, relwidth=0.958)
    Frame4.configure(relief='groove')
    Frame4.configure(borderwidth="2")
    Frame4.configure(relief="groove")
    Frame4.configure(background="#40cc58")

    label_caracteristiques = tk.Label(Frame4)
    label_caracteristiques.place(relx=0.016, rely=0.12, height=54, width=304)
    label_caracteristiques.configure(background="#40cc58")
    label_caracteristiques.configure(disabledforeground="#a3a3a3")
    label_caracteristiques.configure(font="-family {Segoe UI} -size 14 -underline 1")
    label_caracteristiques.configure(foreground="#000000")
    label_caracteristiques.configure(text='''Choisissez vos caractéristiques :''')

    label_update = tk.Label(Frame4, textvariable=monTexte)
    label_update.place(relx=0.538, rely=0.12, height=54, width=264)
    label_update.configure(background="#40cc58")
    label_update.configure(disabledforeground="#a3a3a3")
    label_update.configure(font="-family {Segoe UI} -size 14")
    label_update.configure(foreground="#000000")

    Labelframe1 = tk.LabelFrame(root)
    Labelframe1.place(relx=0.016, rely=0.2, relheight=0.189, relwidth=0.781)
    Labelframe1.configure(relief='groove')
    Labelframe1.configure(foreground="black")
    Labelframe1.configure(text='''Attaque''')
    Labelframe1.configure(background="#40cc58")

    scale_attaque = tk.Scale(Labelframe1, from_=0.0, to=30, command=update_text)
    scale_attaque.place(relx=0.016, rely=0.271, relheight=0.580, relwidth=0.962)
    scale_attaque.configure(activebackground="#ececec")
    scale_attaque.configure(background="#55a25f")
    scale_attaque.configure(foreground="#000000")
    scale_attaque.configure(highlightbackground="#55a25f")
    scale_attaque.configure(highlightcolor="black")
    scale_attaque.configure(length="586")
    scale_attaque.configure(orient="horizontal")
    scale_attaque.configure(troughcolor="#55a25f")

    Labelframe2 = tk.LabelFrame(root)
    Labelframe2.place(relx=0.016, rely=0.4, relheight=0.189, relwidth=0.781)
    Labelframe2.configure(relief='groove')
    Labelframe2.configure(foreground="black")
    Labelframe2.configure(text='''Défense''')
    Labelframe2.configure(background="#40cc58")

    scale_defense = tk.Scale(Labelframe2, from_=0.0, to=30, command=update_text)
    scale_defense.place(relx=0.016, rely=0.271, relheight=0.580, relwidth=0.962)
    scale_defense.configure(activebackground="#ececec")
    scale_defense.configure(background="#55a25f")
    scale_defense.configure(foreground="#000000")
    scale_defense.configure(highlightbackground="#55a25f")
    scale_defense.configure(highlightcolor="black")
    scale_defense.configure(length="586")
    scale_defense.configure(orient="horizontal")
    scale_defense.configure(troughcolor="#55a25f")

    Labelframe3 = tk.LabelFrame(root)
    Labelframe3.place(relx=0.016, rely=0.6, relheight=0.189, relwidth=0.781)
    Labelframe3.configure(relief='groove')
    Labelframe3.configure(foreground="black")
    Labelframe3.configure(text='''Agilité''')
    Labelframe3.configure(background="#40cc58")

    scale_agilite = tk.Scale(Labelframe3, from_=0.0, to=30, command=update_text)
    scale_agilite.place(relx=0.016, rely=0.271, relheight=0.580, relwidth=0.962)
    scale_agilite.configure(activebackground="#ececec")
    scale_agilite.configure(background="#55a25f")
    scale_agilite.configure(foreground="#000000")
    scale_agilite.configure(highlightbackground="#55a25f")
    scale_agilite.configure(highlightcolor="black")
    scale_agilite.configure(length="586")
    scale_agilite.configure(orient="horizontal")
    scale_agilite.configure(troughcolor="#55a25f")

    Labelframe4 = tk.LabelFrame(root)
    Labelframe4.place(relx=0.016, rely=0.8, relheight=0.189, relwidth=0.781)
    Labelframe4.configure(relief='groove')
    Labelframe4.configure(foreground="black")
    Labelframe4.configure(text='''Chance''')
    Labelframe4.configure(background="#40cc58")

    scale_chance = tk.Scale(Labelframe4, from_=0.0, to=30, command=update_text)
    scale_chance.place(relx=0.016, rely=0.271, relheight=0.580, relwidth=0.962)
    scale_chance.configure(activebackground="#ececec")
    scale_chance.configure(background="#55a25f")
    scale_chance.configure(foreground="#000000")
    scale_chance.configure(highlightbackground="#55a25f")
    scale_chance.configure(highlightcolor="black")
    scale_chance.configure(length="586")
    scale_chance.configure(orient="horizontal")
    scale_chance.configure(troughcolor="#55a25f")

    Frame5 = tk.Frame(root)
    Frame5.place(relx=0.813, rely=0.2, relheight=0.789, relwidth=0.164)
    Frame5.configure(relief='groove')
    Frame5.configure(borderwidth="2")
    Frame5.configure(relief="groove")
    Frame5.configure(background="#40cc58")

    bouton_retour = tk.Button(Frame5, command=lambda: [create_deuxieme(), Frame4.place_forget(), Frame5.place_forget(), Labelframe1.place_forget(), Labelframe2.place_forget(), Labelframe3.place_forget(), Labelframe4.place_forget()])
    bouton_retour.place(relx=0.095, rely=0.817, height=44, width=87)
    bouton_retour.configure(activebackground="#ececec")
    bouton_retour.configure(activeforeground="#000000")
    bouton_retour.configure(background="#55a25f")
    bouton_retour.configure(font="-family {Segoe UI} -size 12")
    bouton_retour.configure(disabledforeground="#a3a3a3")
    bouton_retour.configure(foreground="#000000")
    bouton_retour.configure(highlightbackground="#d9d9d9")
    bouton_retour.configure(highlightcolor="black")
    bouton_retour.configure(pady="0")
    bouton_retour.configure(text='''Retour''')


def reinit():  # fonction pour reinitialiser les statistiques si l'utilisateur veut d'autres choses
    scale_attaque.config(state="normal", takefocus=0)
    scale_agilite.config(state="normal", takefocus=0)
    scale_defense.config(state="normal", takefocus=0)
    scale_chance.config(state="normal", takefocus=0)
    scale_attaque.set(0)
    scale_agilite.set(0)
    scale_defense.set(0)
    scale_chance.set(0)
    bouton_suivantcara.place_forget()
    bouton_reinitcara.place_forget()
    label_update.configure(background="#40cc58")
    label_update.configure(foreground="#000000")


def update_text(var):  # fonction pour update le nombre de points restants
    global bouton_suivantcara, bouton_reinitcara

    bouton_suivantcara = tk.Button(Frame5)

    attaque = scale_attaque.get()
    defense = scale_defense.get()
    agilite = scale_agilite.get()
    chance = scale_chance.get()
    point_iu = 30 - attaque - defense - agilite - chance

    if point_iu == 0:  # s'il n'y a plus de points disponibles

        scale_attaque.config(state="disabled", takefocus=0)
        scale_defense.config(state="disabled", takefocus=0)
        scale_agilite.config(state="disabled", takefocus=0)
        scale_chance.config(state="disabled", takefocus=0)


        bouton_suivantcara.place(relx=0.095, rely=0.197, height=44, width=87)
        bouton_suivantcara.configure(activebackground="#ececec")
        bouton_suivantcara.configure(activeforeground="#000000")
        bouton_suivantcara.configure(background="#55a25f")
        bouton_suivantcara.configure(disabledforeground="#a3a3a3")
        bouton_suivantcara.configure(font="-family {Segoe UI} -size 12")
        bouton_suivantcara.configure(foreground="#000000")
        bouton_suivantcara.configure(highlightbackground="#d9d9d9")
        bouton_suivantcara.configure(highlightcolor="black")
        bouton_suivantcara.configure(pady="0")
        bouton_suivantcara.configure(text='''Suivant''')

        bouton_reinitcara = tk.Button(Frame5, command=reinit)
        bouton_reinitcara.place(relx=0.095, rely=0.507, height=44, width=87)
        bouton_reinitcara.configure(activebackground="#ececec")
        bouton_reinitcara.configure(activeforeground="#000000")
        bouton_reinitcara.configure(background="#55a25f")
        bouton_reinitcara.configure(disabledforeground="#a3a3a3")
        bouton_reinitcara.configure(font="-family {Segoe UI} -size 12")
        bouton_reinitcara.configure(foreground="#000000")
        bouton_reinitcara.configure(highlightbackground="#d9d9d9")
        bouton_reinitcara.configure(highlightcolor="black")
        bouton_reinitcara.configure(pady="0")
        bouton_reinitcara.configure(text='''Réinitialiser''')

        label_update.configure(background="#ff0000")
        label_update.configure(foreground="#ffffff")

    if 1 < point_iu:  # afficher le nombre de points restants avec un S
        monTexte.set("Il vous reste " + str(point_iu) + " points !")

    if point_iu <= 1:  # afficher le nombre de point restant sans S
        monTexte.set("Il vous reste " + str(point_iu) + " point !")

    if point_iu < 0:  # si la personne arrive à depasser le nombre de points max
        monTexte.set("Attention, trop de points")

        label_update.configure(background="#ff0000")
        label_update.configure(foreground="#ffffff")

        scale_attaque.config(state="disabled", takefocus=0)
        scale_defense.config(state="disabled", takefocus=0)
        scale_agilite.config(state="disabled", takefocus=0)
        scale_chance.config(state="disabled", takefocus=0)

        bouton_reinitcara = tk.Button(Frame5, command=reinit)
        bouton_reinitcara.place(relx=0.095, rely=0.507, height=44, width=87)
        bouton_reinitcara.configure(activebackground="#ececec")
        bouton_reinitcara.configure(activeforeground="#000000")
        bouton_reinitcara.configure(background="#55a25f")
        bouton_reinitcara.configure(disabledforeground="#a3a3a3")
        bouton_reinitcara.configure(font="-family {Segoe UI} -size 12")
        bouton_reinitcara.configure(foreground="#000000")
        bouton_reinitcara.configure(highlightbackground="#d9d9d9")
        bouton_reinitcara.configure(highlightcolor="black")
        bouton_reinitcara.configure(pady="0")
        bouton_reinitcara.configure(text='''Réinitialiser''')


def create_options():  # fonction pour créer la fenetre contenant les différentes options
    def change_volume(val):  # fonction pour changer le volume du son jouer par pygame
        var = int(val) / 100
        son.set_volume(var)

    top = tk.Toplevel(root)
    top.geometry("640x480+468+138")
    top.resizable(0, 0)
    top.title("Options")
    top.configure(background="#7dffbe")

    Labelframe5 = tk.LabelFrame(top)
    Labelframe5.place(relx=0.031, rely=0.313, relheight=0.281, relwidth=0.938)
    Labelframe5.configure(relief='groove')
    Labelframe5.configure(font="-family {Segoe UI} -size 13")
    Labelframe5.configure(foreground="black")
    Labelframe5.configure(text='''Changer le volume de la musique''')
    Labelframe5.configure(background="#85a736")

    scale_volume = tk.Scale(Labelframe5, from_=0.0, to=100.0, command=change_volume)
    scale_volume.place(relx=0.033, rely=0.222, relheight=0.681, relwidth=0.943)
    scale_volume.configure(activebackground="#ececec")
    scale_volume.configure(background="#3ca253")
    scale_volume.configure(foreground="#000000")
    scale_volume.configure(highlightbackground="#3ca253")
    scale_volume.configure(highlightcolor="#000000")
    scale_volume.configure(length="566")
    scale_volume.configure(orient="horizontal")
    scale_volume.configure(troughcolor="#3ca253")
    scale_volume.set(50)

    bouton_retour = tk.Button(top, command=top.destroy)
    bouton_retour.place(relx=0.359, rely=0.813, height=64, width=177)
    bouton_retour.configure(activebackground="#ececec")
    bouton_retour.configure(activeforeground="#000000")
    bouton_retour.configure(background="#3ca253")
    bouton_retour.configure(disabledforeground="#a3a3a3")
    bouton_retour.configure(font="-family {Segoe UI} -size 14")
    bouton_retour.configure(foreground="#000000")
    bouton_retour.configure(highlightbackground="#d9d9d9")
    bouton_retour.configure(highlightcolor="black")
    bouton_retour.configure(pady="0")
    bouton_retour.configure(text='''Retour''')

    label_options = tk.Label(top)
    label_options.place(relx=0.328, rely=0.021, height=51, width=204)
    label_options.configure(background="#7dffbe")
    label_options.configure(disabledforeground="#a3a3a3")
    label_options.configure(font="-family {Segoe UI} -size 14 -weight bold -underline 1")
    label_options.configure(foreground="#000000")
    label_options.configure(text='''Options :''')


file = ["0"]

pygame.mixer.init()

son = pygame.mixer.Sound('main_loop.wav')
son.play(loops=-1, maxtime=0, fade_ms=0)
son.set_volume(0.5)

# création du main menu

root = tk.Tk()
root.geometry("640x480+468+138")
root.resizable(0, 0)
root.title("DualCent")
root.configure(background="#bff2c7")

create_premier()

# création du menu en haut de la page

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Options", command=create_options)
file_menu.add_separator()
file_menu.add_command(label="Quitter", command=root.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)
root.config(menu=menu_bar)

root.mainloop()
