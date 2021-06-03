import tkinter as tk
import pygame
import os


def create_premier():  # fonction pour créer le premier menu
    Frame1 = tk.Frame(root, relief='groove', borderwidth="2", background="#80e1a7")
    Frame1.place(relx=0.083, rely=0.097, relheight=0.174, relwidth=0.809)

    label_acceuil = tk.Label(Frame1, background="#80e1a7", disabledforeground="#a3a3a3",
                             font="-family {Forte} -size 24 -weight bold -underline 1", foreground="#000000",
                             highlightbackground="#f0f0f0f0f0f0", text='''Bienvenue sur DualCent''')
    label_acceuil.place(relx=0.011, rely=0.08, height=101, width=854)

    Frame2 = tk.Frame(root, relief='groove', borderwidth="2", background="#80e1a7")
    Frame2.place(relx=0.083, rely=0.333, relheight=0.479, relwidth=0.809)

    bouton_jouer = tk.Button(Frame2, text='''JOUER''',
                             command=lambda: os.system('jeu.py'), activebackground="#ececec",
                             activeforeground="#000000", background="#85b90b", disabledforeground="#a3a3a3",
                             foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", pady="0")
    bouton_jouer.place(relx=0.08, rely=0.348, height=94, width=177)

    bouton_editer = tk.Button(Frame2, text='''EDITER''', command=lambda: os.system('cmd /c python editeur.py'),
                              activebackground="#ececec", activeforeground="#000000", background="#85b90b",
                              disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                              highlightcolor="black", pady="0")
    bouton_editer.place(relx=0.389, rely=0.348, height=94, width=177)

    bouton_quitter = tk.Button(Frame2, text='''QUITTER''', command=root.quit, activebackground="#ececec",
                               activeforeground="#000000", background="#85b90b", disabledforeground="#a3a3a3",
                               foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", pady="0")
    bouton_quitter.place(relx=0.709, rely=0.348, height=94, width=177)

    bouton_tuto = tk.Button(Frame2, image=question, command=open_tuto, background="#85b90b", compound="center")
    bouton_tuto.place(relx=0.473, rely=0.650)

    label_credits = tk.Label(root, text='''Crée par Rasputin Team''', background="#2e2b2a",
                             disabledforeground="#a3a3a3", foreground="#80ffff", font="-family {Forte} -size 13")
    label_credits.place(relx=0.806, rely=0.875, height=71, width=184)


def open_tuto():  # fonction pour ouvrir une fenetre ou il y aura le tuto pour savoir comment utiliser notre programme
    tuto = tk.Toplevel()
    tuto.geometry("1080x720")
    tuto.resizable(0, 0)

    t = tk.Text(tuto)
    t.place(relwidth=1.0, relheight=1.0)

    f = open("./rasputin tuto.txt", 'r', encoding='utf-8')
    t.insert(1.0, f.read())
    t.configure(state="disabled")


def create_options():  # fonction pour créer la fenetre contenant les différentes options
    def change_volume(val):  # fonction pour changer le volume du son jouer par pygame
        var = int(val) / 100
        son.set_volume(var)

    top = tk.Toplevel(root)
    top.geometry("640x480+468+138")
    top.resizable(0, 0)
    top.title("Options")
    top.configure(background="#7dffbe")

    Labelframe5 = tk.LabelFrame(top, text='''Changer le volume de la musique''', relief='groove',
                                font="-family {Segoe UI} -size 13", foreground="black", background="#85a736")
    Labelframe5.place(relx=0.031, rely=0.313, relheight=0.281, relwidth=0.938)

    scale_volume = tk.Scale(Labelframe5, from_=0.0, to=100.0, command=change_volume, activebackground="#ececec",
                            background="#3ca253", foreground="#000000", highlightbackground="#3ca253",
                            highlightcolor="#000000", length="566", orient="horizontal", troughcolor="#3ca253")
    scale_volume.place(relx=0.033, rely=0.222, relheight=0.681, relwidth=0.943)
    scale_volume.set(50)

    bouton_retour = tk.Button(top, text='''Retour''', command=top.destroy, activebackground="#ececec",
                              activeforeground="#000000", background="#3ca253", disabledforeground="#a3a3a3",
                              font="-family {Segoe UI} -size 14", foreground="#000000", highlightbackground="#d9d9d9",
                              highlightcolor="black", pady="0")
    bouton_retour.place(relx=0.359, rely=0.813, height=64, width=177)

    label_options = tk.Label(top, text='''Options :''', background="#7dffbe", disabledforeground="#a3a3a3",
                             font="-family {Segoe UI} -size 14 -weight bold -underline 1", foreground="#000000")
    label_options.place(relx=0.328, rely=0.021, height=51, width=204)


file = ["0"]

pygame.mixer.init()

son = pygame.mixer.Sound('main_loop.wav')
son.play(loops=-1, maxtime=0, fade_ms=0)
son.set_volume(0.5)

# création du main menu

root = tk.Tk()
root.geometry("1080x720+363+127")
root.resizable(0, 0)
root.title("DualCent")
root.configure(background="#2e2b2a")

question = tk.PhotoImage(master=root, file=r"question-mark-inside-a-circle.png")

icone = tk.PhotoImage(file="./51mF9jwGkEL.png")

root.iconphoto(True, icone)

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
