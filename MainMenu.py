import tkinter as tk
from tkinter import filedialog as fd
import pygame


def open_file_path():  # fonction qui permet de demander à l'utilisateur de choisir le fichier du jeu
    filename = fd.askopenfilename()
    print(filename)
    file[0] = filename


def create_premier(): # fonction pour créer le premier menu
    Frame1 = tk.Frame(root)
    Frame1.place(relx=0.033, rely=0.044, relheight=0.233, relwidth=0.942)
    Frame1.configure(relief='groove')
    Frame1.configure(borderwidth="2")
    Frame1.configure(relief="groove")
    Frame1.configure(background="#80e1a7")

    Label1 = tk.Label(Frame1)
    Label1.place(relx=0.017, rely=0.133, height=71, width=574)
    Label1.configure(background="#80e1a7")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(font="-family {Forte} -size 24 -weight bold -underline 1")
    Label1.configure(foreground="#000000")
    Label1.configure(highlightbackground="#f0f0f0f0f0f0")
    Label1.configure(text='''Bienvenue sur DualCent''')

    Frame2 = tk.Frame(root)
    Frame2.place(relx=0.031, rely=0.289, relheight=0.567, relwidth=0.945)
    Frame2.configure(relief='groove')
    Frame2.configure(borderwidth="2")
    Frame2.configure(relief="groove")
    Frame2.configure(background="#80e1a7")

    Button1 = tk.Button(Frame2, command=lambda: [create_deuxieme(), Frame1.place_forget(), Frame2.place_forget(),
                                                 Label2.place_forget()])
    Button1.place(relx=0.083, rely=0.353, height=54, width=107)
    Button1.configure(activebackground="#ececec")
    Button1.configure(activeforeground="#000000")
    Button1.configure(background="#85b90b")
    Button1.configure(disabledforeground="#a3a3a3")
    Button1.configure(foreground="#000000")
    Button1.configure(highlightbackground="#d9d9d9")
    Button1.configure(highlightcolor="black")
    Button1.configure(pady="0")
    Button1.configure(text='''JOUER''')

    Button2 = tk.Button(Frame2)
    Button2.place(relx=0.413, rely=0.353, height=54, width=107)
    Button2.configure(activebackground="#ececec")
    Button2.configure(activeforeground="#000000")
    Button2.configure(background="#85b90b")
    Button2.configure(disabledforeground="#a3a3a3")
    Button2.configure(foreground="#000000")
    Button2.configure(highlightbackground="#d9d9d9")
    Button2.configure(highlightcolor="black")
    Button2.configure(pady="0")
    Button2.configure(text='''EDITER''')

    Button3 = tk.Button(Frame2, command=root.quit)
    Button3.place(relx=0.744, rely=0.353, height=54, width=107)
    Button3.configure(activebackground="#ececec")
    Button3.configure(activeforeground="#000000")
    Button3.configure(background="#85b90b")
    Button3.configure(disabledforeground="#a3a3a3")
    Button3.configure(foreground="#000000")
    Button3.configure(highlightbackground="#d9d9d9")
    Button3.configure(highlightcolor="black")
    Button3.configure(pady="0")
    Button3.configure(text='''QUITTER''')

    Label2 = tk.Label(root)
    Label2.place(relx=0.719, rely=0.889, height=41, width=174)
    Label2.configure(background="#bff2c7")
    Label2.configure(disabledforeground="#a3a3a3")
    Label2.configure(foreground="#000000")
    Label2.configure(text='''Crée par Rasputin Team''')


def create_deuxieme():  # fonction pour créer la premiere fenetre apres le main menu
    global Frame3

    Frame3 = tk.Frame(root)
    Frame3.place(relx=0.031, rely=0.289, relheight=0.567, relwidth=0.945)
    Frame3.configure(relief='groove')
    Frame3.configure(borderwidth="2")
    Frame3.configure(relief="groove")
    Frame3.configure(background="#80e1a7")

    Button4 = tk.Button(Frame3, command=open_file_path)
    Button4.place(relx=0.404, rely=0.353, height=54, width=107)
    Button4.configure(activebackground="#ececec")
    Button4.configure(activeforeground="#000000")
    Button4.configure(background="#85b90b")
    Button4.configure(disabledforeground="#a3a3a3")
    Button4.configure(foreground="#000000")
    Button4.configure(highlightbackground="#d9d9d9")
    Button4.configure(highlightcolor="black")
    Button4.configure(pady="0")
    Button4.configure(text='''Choisir un fichier :''')

    Button6 = tk.Button(Frame3, command=create_troisieme)
    Button6.place(relx=0.404, rely=0.653, height=54, width=107)
    Button6.configure(activebackground="#ececec")
    Button6.configure(activeforeground="#000000")
    Button6.configure(background="#85b90b")
    Button6.configure(disabledforeground="#a3a3a3")
    Button6.configure(foreground="#000000")
    Button6.configure(highlightbackground="#d9d9d9")
    Button6.configure(highlightcolor="black")
    Button6.configure(pady="0")
    Button6.configure(text='''Suivant''')


def create_troisieme():  # fonction pour créer la dexieme fenetre apres le main menu (statistiques)
    Frame3.destroy()

    global Scale1, Scale2, Scale3, Scale4, Frame5, monTexte, Label4
    monTexte = tk.StringVar()
    monTexte.set("Il vous reste 30 points !")

    Frame4 = tk.Frame(root)
    Frame4.place(relx=0.017, rely=0.022, relheight=0.167, relwidth=0.958)
    Frame4.configure(relief='groove')
    Frame4.configure(borderwidth="2")
    Frame4.configure(relief="groove")
    Frame4.configure(background="#40cc58")

    Label3 = tk.Label(Frame4)
    Label3.place(relx=0.016, rely=0.12, height=54, width=304)
    Label3.configure(background="#40cc58")
    Label3.configure(disabledforeground="#a3a3a3")
    Label3.configure(font="-family {Segoe UI} -size 14 -underline 1")
    Label3.configure(foreground="#000000")
    Label3.configure(text='''Choisissez vos caractéristiques :''')

    Label4 = tk.Label(Frame4, textvariable=monTexte)
    Label4.place(relx=0.538, rely=0.12, height=54, width=264)
    Label4.configure(background="#40cc58")
    Label4.configure(disabledforeground="#a3a3a3")
    Label4.configure(font="-family {Segoe UI} -size 14")
    Label4.configure(foreground="#000000")

    Labelframe1 = tk.LabelFrame(root)
    Labelframe1.place(relx=0.016, rely=0.2, relheight=0.189, relwidth=0.781)
    Labelframe1.configure(relief='groove')
    Labelframe1.configure(foreground="black")
    Labelframe1.configure(text='''Attaque''')
    Labelframe1.configure(background="#40cc58")

    Scale1 = tk.Scale(Labelframe1, from_=0.0, to=30, command=update_text)
    Scale1.place(relx=0.016, rely=0.271, relheight=0.580, relwidth=0.962)
    Scale1.configure(activebackground="#ececec")
    Scale1.configure(background="#55a25f")
    Scale1.configure(foreground="#000000")
    Scale1.configure(highlightbackground="#55a25f")
    Scale1.configure(highlightcolor="black")
    Scale1.configure(length="586")
    Scale1.configure(orient="horizontal")
    Scale1.configure(troughcolor="#55a25f")

    Labelframe2 = tk.LabelFrame(root)
    Labelframe2.place(relx=0.016, rely=0.4, relheight=0.189, relwidth=0.781)
    Labelframe2.configure(relief='groove')
    Labelframe2.configure(foreground="black")
    Labelframe2.configure(text='''Défense''')
    Labelframe2.configure(background="#40cc58")

    Scale2 = tk.Scale(Labelframe2, from_=0.0, to=30, command=update_text)
    Scale2.place(relx=0.016, rely=0.271, relheight=0.580, relwidth=0.962)
    Scale2.configure(activebackground="#ececec")
    Scale2.configure(background="#55a25f")
    Scale2.configure(foreground="#000000")
    Scale2.configure(highlightbackground="#55a25f")
    Scale2.configure(highlightcolor="black")
    Scale2.configure(length="586")
    Scale2.configure(orient="horizontal")
    Scale2.configure(troughcolor="#55a25f")

    Labelframe3 = tk.LabelFrame(root)
    Labelframe3.place(relx=0.016, rely=0.6, relheight=0.189, relwidth=0.781)
    Labelframe3.configure(relief='groove')
    Labelframe3.configure(foreground="black")
    Labelframe3.configure(text='''Agilité''')
    Labelframe3.configure(background="#40cc58")

    Scale3 = tk.Scale(Labelframe3, from_=0.0, to=30, command=update_text)
    Scale3.place(relx=0.016, rely=0.271, relheight=0.580, relwidth=0.962)
    Scale3.configure(activebackground="#ececec")
    Scale3.configure(background="#55a25f")
    Scale3.configure(foreground="#000000")
    Scale3.configure(highlightbackground="#55a25f")
    Scale3.configure(highlightcolor="black")
    Scale3.configure(length="586")
    Scale3.configure(orient="horizontal")
    Scale3.configure(troughcolor="#55a25f")

    Labelframe4 = tk.LabelFrame(root)
    Labelframe4.place(relx=0.016, rely=0.8, relheight=0.189, relwidth=0.781)
    Labelframe4.configure(relief='groove')
    Labelframe4.configure(foreground="black")
    Labelframe4.configure(text='''Chance''')
    Labelframe4.configure(background="#40cc58")

    Scale4 = tk.Scale(Labelframe4, from_=0.0, to=30, command=update_text)
    Scale4.place(relx=0.016, rely=0.271, relheight=0.580, relwidth=0.962)
    Scale4.configure(activebackground="#ececec")
    Scale4.configure(background="#55a25f")
    Scale4.configure(foreground="#000000")
    Scale4.configure(highlightbackground="#55a25f")
    Scale4.configure(highlightcolor="black")
    Scale4.configure(length="586")
    Scale4.configure(orient="horizontal")
    Scale4.configure(troughcolor="#55a25f")

    Frame5 = tk.Frame(root)
    Frame5.place(relx=0.813, rely=0.2, relheight=0.789, relwidth=0.164)
    Frame5.configure(relief='groove')
    Frame5.configure(borderwidth="2")
    Frame5.configure(relief="groove")
    Frame5.configure(background="#40cc58")


def reinit():  # fonction pour reinitialiser les statistiques si l'utilisateur veut d'autres choses
    Scale1.config(state="normal", takefocus=0)
    Scale2.config(state="normal", takefocus=0)
    Scale3.config(state="normal", takefocus=0)
    Scale4.config(state="normal", takefocus=0)
    Scale1.set(0)
    Scale2.set(0)
    Scale3.set(0)
    Scale4.set(0)
    Button7.place_forget()
    Button5.place_forget()
    Label4.configure(background="#40cc58")
    Label4.configure(foreground="#000000")


def update_text(var):  # fonction pour update le nombre de points restants
    attaque = Scale1.get()
    defense = Scale2.get()
    agilite = Scale3.get()
    chance = Scale4.get()
    point_iu = 30 - attaque - defense - agilite - chance

    if point_iu == 0:
        global Button7, Button5

        Scale1.config(state="disabled", takefocus=0)
        Scale2.config(state="disabled", takefocus=0)
        Scale3.config(state="disabled", takefocus=0)
        Scale4.config(state="disabled", takefocus=0)

        Button5 = tk.Button(Frame5)
        Button5.place(relx=0.095, rely=0.197, height=44, width=87)
        Button5.configure(activebackground="#ececec")
        Button5.configure(activeforeground="#000000")
        Button5.configure(background="#55a25f")
        Button5.configure(disabledforeground="#a3a3a3")
        Button5.configure(font="-family {Segoe UI} -size 12")
        Button5.configure(foreground="#000000")
        Button5.configure(highlightbackground="#d9d9d9")
        Button5.configure(highlightcolor="black")
        Button5.configure(pady="0")
        Button5.configure(text='''Suivant''')

        Button7 = tk.Button(Frame5, command=reinit)
        Button7.place(relx=0.095, rely=0.704, height=44, width=87)
        Button7.configure(activebackground="#ececec")
        Button7.configure(activeforeground="#000000")
        Button7.configure(background="#55a25f")
        Button7.configure(disabledforeground="#a3a3a3")
        Button7.configure(font="-family {Segoe UI} -size 12")
        Button7.configure(foreground="#000000")
        Button7.configure(highlightbackground="#d9d9d9")
        Button7.configure(highlightcolor="black")
        Button7.configure(pady="0")
        Button7.configure(text='''Réinitialiser''')

        Label4.configure(background="#ff0000")
        Label4.configure(foreground="#ffffff")

    monTexte.set("Il vous reste " + str(point_iu) + " points !")


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

    Scale5 = tk.Scale(Labelframe5, from_=0.0, to=100.0, command=change_volume)
    Scale5.place(relx=0.033, rely=0.222, relheight=0.681, relwidth=0.943)
    Scale5.configure(activebackground="#ececec")
    Scale5.configure(background="#3ca253")
    Scale5.configure(foreground="#000000")
    Scale5.configure(highlightbackground="#3ca253")
    Scale5.configure(highlightcolor="#000000")
    Scale5.configure(length="566")
    Scale5.configure(orient="horizontal")
    Scale5.configure(troughcolor="#3ca253")
    Scale5.set(50)

    Button8 = tk.Button(top, command=top.destroy)
    Button8.place(relx=0.359, rely=0.813, height=64, width=177)
    Button8.configure(activebackground="#ececec")
    Button8.configure(activeforeground="#000000")
    Button8.configure(background="#3ca253")
    Button8.configure(disabledforeground="#a3a3a3")
    Button8.configure(font="-family {Segoe UI} -size 14")
    Button8.configure(foreground="#000000")
    Button8.configure(highlightbackground="#d9d9d9")
    Button8.configure(highlightcolor="black")
    Button8.configure(pady="0")
    Button8.configure(text='''Retour''')

    Label4 = tk.Label(top)
    Label4.place(relx=0.328, rely=0.021, height=51, width=204)
    Label4.configure(background="#7dffbe")
    Label4.configure(disabledforeground="#a3a3a3")
    Label4.configure(font="-family {Segoe UI} -size 14 -weight bold -underline 1")
    Label4.configure(foreground="#000000")
    Label4.configure(text='''Options :''')


file = [0]

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
file_menu.add_command(label="Quitter", command=root.quit)
file_menu.add_command(label="Options", command=create_options)
menu_bar.add_cascade(label="Fichier", menu=file_menu)
root.config(menu=menu_bar)

root.mainloop()
