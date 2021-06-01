import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk
import csv
import random

liste_herotouche = ["Ouch, cela a du faire mal", "Bravo !", "Vous avez une force surhumaine !", "C'est génial, continuez comme ca !"]
liste_monstretouche = ["Aie, vous avez du prendre cher !", "Ce monstre est très puissant", "Cette attaque est meurtrière", "Le monstre vous a bien eu !"]

image_monstre = []

titre = []
choix1 = []
choix2 = []
goto1 = []
goto2 = []

Attack = 0
Defense = 0
Agilite = 0
Luck = 0
PvHero = 100
PvMonstre = []
DegatsMonstre = []
nom_monstre = []
armes = []
degats_armes = []
monstre_index = []

pvmonstre_attaque = ""


def get_data(histoire):
    global titre, image_monstre, monstre_index, choix1, choix2, goto1, goto2, Attack, Defense, Agilite, Luck, PvMonstre, DegatsMonstre, nom_monstre, armes, degats_armes, PvHero, PvMonstre

    f = open(histoire, "rt", encoding='utf-8-sig')

    reader = csv.reader(f, delimiter=";")

    for row in reader:
        if row[0] == 'titre':
            titre = row[1:]
        elif row[0] == 'choix1':
            choix1 = row[1:]
        elif row[0] == 'choix2':
            choix2 = row[1:]
        elif row[0] == 'goto1':
            goto1 = row[1:]
        elif row[0] == 'goto2':
            goto2 = row[1:]
        elif row[0] == 'attaque':
            Attack = row[1]
        elif row[0] == 'defense':
            Defense = row[1]
        elif row[0] == 'agilite':
            Agilite = row[1]
        elif row[0] == 'chance':
            Luck = row[1]
        elif row[0] == 'pvmon':
            PvMonstre = row[1:]
        elif row[0] == 'degatsmon':
            DegatsMonstre = row[1:]
        elif row[0] == 'imgmon':
            image_monstre = row[1:]
        elif row[0] == 'nommon':
            nom_monstre = row[1:]
        elif row[0] == 'nom_arme':
            armes = row[1:]
        elif row[0] == 'boost_arme':
            degats_armes = row[1:]
        elif row[0] == 'monstre_histoire':
            monstre_index = row[1:]
    # fermeture du fichier csv

    for i in range(len(titre)):
        titre[i] = titre[i].replace("\\n", "\n")

    f.close()


root = tk.Tk()
root.geometry("1080x720")
root.resizable(0, 0)
root.title("Game")
root.configure(background="#2e2b2a")


def clean_window():  # fonction pour clear les widgets présents sur la fenetre principale
    for widget in root.winfo_children():
        widget.destroy()


def open_file_path():  # fonction qui permet de demander à l'utilisateur de choisir le fichier du jeu et qui affiche le boutton "suivant"
    filename = fd.askopenfilename()
    print(filename)
    file[0] = filename
    if len(file[0]) > 2:
        bouton_suivantfile.configure(state="normal")
        get_data(file[0])


def create_selection_window():  # fonction pour créer lafenetre pour choisir son fichier histoire
    global Frame3, bouton_suivantfile

    index = 0

    Frame3 = tk.Frame(root, relief='groove', borderwidth="2", background="#80e1a7")
    Frame3.place(relx=0.083, rely=0.25, relheight=0.66, relwidth=0.806)

    selection_label = tk.Label(root, background="#2e2b2a", disabledforeground="#a3a3a3", foreground="#80ffff",
                               text='''Sélectionnez votre fichier jeu''',
                               font="-family {Forte} -size 25 -weight bold -underline 1")
    selection_label.place(x=90, y=40, height=101, width=863)

    bouton_selectionfile = tk.Button(Frame3, text='''Choisir un fichier :''', command=open_file_path,
                                     activebackground="#ececec", activeforeground="#000000", background="#85b90b",
                                     disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                     highlightcolor="black", pady="0", font="-family {Segoe UI} -size 12")
    bouton_selectionfile.place(relx=0.39, rely=0.379, height=94, width=177)

    bouton_suivantfile = tk.Button(Frame3, text='''Suivant''', activebackground="#ececec",
                                   activeforeground="#000000", background="#85b90b", disabledforeground="#a3a3a3",
                                   foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                   pady="0", font="-family {Segoe UI} -size 12",
                                   command=lambda: [clean_window(), begin_game(index)])
    bouton_suivantfile.place(relx=0.711, rely=0.379, height=94, width=177)
    bouton_suivantfile.configure(state="disabled")

    bouton_retour = tk.Button(Frame3, text='''Retour''', command=root.quit,
                              activebackground="#ececec", activeforeground="#000000", background="#85b90b",
                              disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 12", foreground="#000000",
                              highlightbackground="#d9d9d9", highlightcolor="black", pady="0")
    bouton_retour.place(relx=0.08, rely=0.379, height=94, width=177)


def create_jeu_window():  # fonction pour creer la fenetre du jeu ou l'on peut choisir ses choix

    Button3 = tk.Button(root, text='''Quitter''', activebackground="#ececec", activeforeground="#000000",
                        background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000",
                        highlightbackground="#d9d9d9", highlightcolor="black", pady="0")
    Button3.place(relx=0.333, rely=0.917, height=44, width=347)


def begin_game(index):  # fonction du "moteur de jeu"
    Frame1 = tk.Frame(root, relief='groove', borderwidth="2", background="#d9d9d9")
    Frame1.place(relx=0.009, rely=0.014, relheight=0.354, relwidth=0.977)

    Labelframe1 = tk.LabelFrame(root, relief='groove', foreground="black", text='''Que voulez vous faire ?''',
                                background="#d9d9d9")
    Labelframe1.place(relx=0.009, rely=0.389, relheight=0.507, relwidth=0.981)

    Button3 = tk.Button(root, text='''Quitter''', activebackground="#ececec", activeforeground="#000000",
                        background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000",
                        highlightbackground="#d9d9d9", highlightcolor="black", pady="0")
    Button3.place(relx=0.333, rely=0.917, height=44, width=347)

    def debut_histoire():  # fonction pour afficher le premier titre de l'histoire avec ses choix
        Label1 = tk.Label(Frame1, background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000",
                          text=titre[0])
        Label1.place(relx=0.009, rely=0.039, height=231, width=1034)

        Label2 = tk.Label(Labelframe1, text=choix1[0], background="#d9d9d9", disabledforeground="#a3a3a3",
                          foreground="#000000", relief="groove")
        Label2.place(relx=0.009, rely=0.082, height=191, width=492, bordermode='ignore')

        Button1 = tk.Button(Labelframe1, text='''Je fais ceci :''', activebackground="#ececec",
                            activeforeground="#000000", command=lambda: choix1_reponse(index),
                            background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000",
                            highlightbackground="#d9d9d9", highlightcolor="black", pady="0")
        Button1.place(relx=0.076, rely=0.658, height=94, width=347, bordermode='ignore')

        Label3 = tk.Label(Labelframe1, text=choix2[0], background="#d9d9d9", disabledforeground="#a3a3a3",
                          foreground="#000000", relief="groove")
        Label3.place(relx=0.519, rely=0.082, height=191, width=493, bordermode='ignore')

        Button2 = tk.Button(Labelframe1, text='''Je fais cela :''', activebackground="#ececec",
                            activeforeground="#000000", command=lambda: choix2_reponse(index),
                            background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000",
                            highlightbackground="#d9d9d9", highlightcolor="black", pady="0")
        Button2.place(relx=0.595, rely=0.658, height=94, width=347, bordermode='ignore')

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
        global Label1, Label2, Label3

        Label1 = tk.Label(Frame1, background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000",
                          text=titre[index])
        Label1.place(relx=0.009, rely=0.039, height=231, width=1034)

        Label2 = tk.Label(Labelframe1, text=choix1[index], background="#d9d9d9", disabledforeground="#a3a3a3",
                          foreground="#000000", relief="groove")
        Label2.place(relx=0.009, rely=0.082, height=191, width=492, bordermode='ignore')

        Button1 = tk.Button(Labelframe1, text='''Je fais ceci :''', activebackground="#ececec",
                            activeforeground="#000000", command=lambda: choix1_reponse(index),
                            background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000",
                            highlightbackground="#d9d9d9", highlightcolor="black", pady="0")
        Button1.place(relx=0.076, rely=0.658, height=94, width=347, bordermode='ignore')

        Label3 = tk.Label(Labelframe1, text=choix2[index], background="#d9d9d9", disabledforeground="#a3a3a3",
                          foreground="#000000", relief="groove")
        Label3.place(relx=0.519, rely=0.082, height=191, width=493, bordermode='ignore')

        Button2 = tk.Button(Labelframe1, text='''Je fais cela :''', activebackground="#ececec",
                            activeforeground="#000000", command=lambda: choix2_reponse(index),
                            background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000",
                            highlightbackground="#d9d9d9", highlightcolor="black", pady="0")
        Button2.place(relx=0.595, rely=0.658, height=94, width=347, bordermode='ignore')

        if choix1[index] == '':  # s'il n'y a rien alors on enleve ce widget
            Labelframe1.place_forget()
            Label2.place_forget()
            Button1.place_forget()

        if choix2[index] == '':  # s'il n'y a rien alors on enleve ce widget
            Labelframe1.place_forget()
            Label3.place_forget()
            Button2.place_forget()

        if str(titre[index]) == "fin":  # si le titre est "fin" alors affiche un bouton pour quitter
            Label2.place_forget()
            Button1.place_forget()
            Label3.place_forget()
            Button2.place_forget()

        if len(monstre_index[
                   index]) != 0:  # s il y a un monstre à l'etape choisie, alors on affiche une nouvelle fenetre qui va servir pour l'attaque
            index_imgmon = nom_monstre.index(monstre_index[index])
            print(index_imgmon)
            create_attaque_window(index_imgmon)

    def create_attaque_window(index_touse):  # fonction pour afficher la fenetre qui sert pour l'attaque
        global PvHero, PvMonstre, pvmonstre_attaque

        attaque = tk.Toplevel(root)
        attaque.geometry("1080x720")
        attaque.resizable(0, 0)

        pvmonstre_attaque = int(PvMonstre[index_touse])

        def Attaquer(arme):  # fonction pour connaitre les pv du hero et du monstre si l'on appuie sur attaquer
            global pvmonstre_attaque, PvHero, Luck, Agilite, DegatsMonstre
            Toucher = random.randint(1, 200)  # Chance que tu touche le monstre + Chance que tu l'esquive

            index = armes.index(arme)

            if Toucher > (70 + int(Luck) + int(Attack) + int(Agilite) - int(Defense)):
                pvmonstre_attaque = (pvmonstre_attaque - int(degats_armes[index]))
                Scale2.set(pvmonstre_attaque)
                Label2.configure(text=random.choice(liste_herotouche))
                if int(pvmonstre_attaque) < 1:
                    print("tu gagnes")
            elif Toucher < (70 + int(Agilite) + int(Luck) - int(Defense) + int(Attack)):
                PvHero = (int(PvHero) - int(DegatsMonstre[index]))
                Scale1.set(PvHero)
                Label2.configure(text=random.choice(liste_monstretouche))
                if int(PvHero) < 1:
                    print("t es mort")

            #Label2.configure(text="pv monstre :" + str(pvmonstre_attaque) + "\npv hero :" + str(PvHero))

            check_life()

            return pvmonstre_attaque, PvHero

        def Fuir():  # fonction qui permet de fuir si l'on peut et si on peut pas, alors on pert des PV
            global pvmonstre_attaque, PvHero, Luck, Agilite, DegatsHero, DegatsMonstre, titre, titre_label, pv_label
            Partir = random.randint(1, 200)
            ToucherMonstre = random.randint(1, 200)

            if Partir < 130 - int(Luck):  # Chance de fuir
                print("fuir")
                Button3.place(relx=0.37, rely=0.833, height=84, width=227)
                Button3.configure(command=attaque.destroy)
                Button1.configure(state="disabled")
                Button2.configure(state="disabled")
            else:  # sinon apres une tentative de fuite qui a echouee, le personnage se fait toucher par le monstre
                if ToucherMonstre < 65 - (int(Agilite) + int(Luck)):
                    PvHero = int(PvHero) - int(DegatsMonstre[index])
                    Label2.configure(text=("Vous n'avez pas reussi a vous echapper\n" + random.choice(liste_monstretouche)))
                    print("impossible")
                    Scale1.set(PvHero)
            #Label2.configure(text="pv monstre :" + str(pvmonstre_attaque) + "\npv hero :" + str(PvHero))

            return pvmonstre_attaque, PvHero

        def check_life():  # fonction pour checker si les pv du heros ou du monstre sont nuls, et si c'est le cas, alors affiche le bouton quitter
            if int(PvHero) <= 0:
                print("perdu")
                Button3.place(relx=0.37, rely=0.833, height=84, width=227)
                Button3.configure(command=root.destroy)
                Button1.configure(state="disabled")
                Button2.configure(state="disabled")
            elif int(pvmonstre_attaque) <= 0:
                print("gagné")
                Button3.place(relx=0.37, rely=0.833, height=84, width=227)
                Button3.configure(command=attaque.destroy)
                Button1.configure(state="disabled")
                Button2.configure(state="disabled")

        Label1 = tk.Label(attaque, text='''Vous avez été attaqué par un monstre :''', background="#d9d9d9",
                          disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 17 -weight bold -underline 1",
                          foreground="#000000")
        Label1.place(relx=0.037, rely=0.028, height=90, width=994)

        monstre_image = tk.PhotoImage(master=attaque, file=image_monstre[index_touse]).zoom(2)

        Canvas1 = tk.Canvas(attaque, background="#d9d9d9", borderwidth="2", insertbackground="black",
                            selectbackground="blue",
                            selectforeground="white")
        Canvas1.place(relx=0.602, rely=0.222, height=258, width=350)

        width = Canvas1.winfo_reqwidth()
        height = Canvas1.winfo_reqheight()

        Canvas1.create_image(width / 2, height / 2, image=monstre_image)

        Label3 = tk.Label(Canvas1, text="Monstre : " + nom_monstre[index_touse], background="#d9d9d9",
                          disabledforeground="#a3a3a3",
                          foreground="#000000")
        Label3.place(relx=0.029, rely=0.834, height=31, width=324)

        Frame1 = tk.Frame(attaque, relief='groove', borderwidth="2", background="#d9d9d9")
        Frame1.place(relx=0.056, rely=0.222, relheight=0.354, relwidth=0.419)

        Label2 = tk.Label(Frame1, background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000")
        Label2.place(relx=0.022, rely=0.039, height=231, width=426)

        Button1 = tk.Button(attaque, command=lambda: Attaquer(TCombobox1.get()), text='''Attaquer''',
                            activebackground="#ececec",
                            activeforeground="#000000", background="#d9d9d9", disabledforeground="#a3a3a3",
                            foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", pady="0")
        Button1.place(relx=0.093, rely=0.708, height=84, width=227)

        Button2 = tk.Button(attaque, command=Fuir, text='''Fuir''', activebackground="#ececec",
                            activeforeground="#000000",
                            background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000",
                            highlightbackground="#d9d9d9", highlightcolor="black", pady="0")
        Button2.place(relx=0.667, rely=0.708, height=84, width=227)

        Button3 = tk.Button(attaque, text='''Quitter''', activebackground="#ececec", activeforeground="#000000",
                            background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000",
                            highlightbackground="#d9d9d9", highlightcolor="black", pady="0")

        TCombobox1 = ttk.Combobox(attaque, values=armes)
        TCombobox1.place(relx=0.093, rely=0.611, relheight=0.057, relwidth=0.206)
        TCombobox1.configure(takefocus="")

        Scale1 = tk.Scale(attaque, from_=0.0, to=PvHero, activebackground="#ececec", background="#d9d9d9",
                          foreground="#000000",
                          highlightbackground="#d9d9d9", highlightcolor="black", orient="horizontal",
                          troughcolor="#80f07d")
        Scale1.place(relx=0.056, rely=0.125, relwidth=0.414, relheight=0.0, height=42, bordermode='ignore')
        Scale1.set(PvHero)

        Scale2 = tk.Scale(attaque, from_=0.0, to=pvmonstre_attaque, activebackground="#ececec", background="#d9d9d9",
                          foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                          orient="horizontal",
                          troughcolor="#ff0000")
        Scale2.place(relx=0.602, rely=0.125, relwidth=0.32, relheight=0.0, height=42, bordermode='ignore')
        Scale2.set(pvmonstre_attaque)

        attaque.mainloop()

    debut_histoire()


file = ["0"]

create_selection_window()

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Options")
file_menu.add_separator()
file_menu.add_command(label="Quitter", command=root.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)
root.config(menu=menu_bar)

root.mainloop()
