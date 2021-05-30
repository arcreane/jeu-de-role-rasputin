import tkinter as tk
import random
from tkinter import ttk
import csv

image_monstre = ""

Attack = 0
Defense = 0
Agilite = 0
Luck = 0
PvHero = 100
PvMonstre = 0
DegatsMonstre = 0
nom_monstre = ""
armes = []
degats_armes = []

f = open("../projet info/histoires/histoire.csv", "rt", encoding='utf-8-sig')

reader = csv.reader(f, delimiter=";")

for row in reader:
    if row[0] == 'attaque':
        Attack = row[1]
    elif row[0] == 'defense':
        Defense = row[1]
    elif row[0] == 'agilite':
        Agilite = row[1]
    elif row[0] == 'chance':
        Luck = row[1]
    elif row[0] == 'pvmon':
        PvMonstre = row[1]
    elif row[0] == 'degatsmon':
        DegatsMonstre = row[1]
    elif row[0] == 'imgmon':
        image_monstre = row[2]
    elif row[0] == 'nommon':
        nom_monstre = row[1]
    elif row[0] == 'nom_arme':
        armes = row[1:]
    elif row[0] == 'boost_arme':
        degats_armes = row[1:]
# fermeture du fichier csv
f.close()


master = tk.Tk()
master.configure(bg='#92f7cb')  # couleur de fond d'ecran
master.geometry("1080x720")  # taille par defaut


def Attaquer(arme):
    global PvMonstre, PvHero, Luck, Agilite, DegatsMonstre
    Toucher = random.randint(1, 200)  # Chance que tu touche le monstre + Chance que tu l'esquive

    #print(ToucherHero, ToucherMonstre)
    print(Toucher)

    index = armes.index(arme)

    if Toucher > (70 + int(Luck) + int(Attack) + int(Agilite) - int(Defense)):
        PvMonstre = (int(PvMonstre) - int(degats_armes[index]))
        Scale2.set(PvMonstre)
    if int(PvMonstre) < 1:
        print("tu gagnes")
    if Toucher < (70 + int(Agilite) + int(Luck) - int(Defense) + int(Attack)):
        PvHero = (int(PvHero) - int(DegatsMonstre))
        Scale1.set(PvHero)
    if int(PvHero) < 1:
        # fin du jeu
        print("t es mort")

    Label2.configure(text="pv monstre :" + str(PvMonstre) + "\npv hero :" + str(PvHero))

    return PvMonstre, PvHero


def Fuir():
    global PvMonstre, PvHero, Luck, Agilite, DegatsHero, DegatsMonstre, titre, titre_label, pv_label
    Partir = random.randint(1, 200)
    ToucherMonstre = random.randint(1, 200)

    if (Partir < 130 - int(Luck)):  # Chance de fuir
        print("fuir")
    else:
        if (ToucherMonstre < 65 - (int(Agilite) + int(Luck))):
            PvHero = int(PvHero) - int(DegatsMonstre)
            print("impossible")
    Label2.configure(text="pv monstre :" + str(PvMonstre) + "\npv hero :" + str(PvHero))

    return PvMonstre, PvHero


Label1 = tk.Label(master, text='''Vous avez été attaqué par un monstre :''', background="#d9d9d9", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 17 -weight bold -underline 1", foreground="#000000")
Label1.place(relx=0.037, rely=0.028, height=90, width=994)

Canvas1 = tk.Canvas(master)
Canvas1.place(relx=0.602, rely=0.222, relheight=0.351
              , relwidth=0.319)
Canvas1.configure(background="#d9d9d9")
Canvas1.configure(borderwidth="2")
Canvas1.configure(cursor="fleur")
Canvas1.configure(insertbackground="black")
Canvas1.configure(selectbackground="blue")
Canvas1.configure(selectforeground="white")

width = Canvas1.winfo_reqwidth()
height = Canvas1.winfo_reqheight()

monstre_image = tk.PhotoImage(file=image_monstre, master=master)

Canvas1.create_image(width/2, height/2, image=monstre_image)

Label3 = tk.Label(Canvas1)
Label3.place(relx=0.029, rely=0.834, height=31, width=324)
Label3.configure(background="#d9d9d9")
Label3.configure(cursor="fleur")
Label3.configure(disabledforeground="#a3a3a3")
Label3.configure(foreground="#000000")
Label3.configure(text="Monstre : " + nom_monstre)

Frame1 = tk.Frame(master)
Frame1.place(relx=0.056, rely=0.222, relheight=0.354
             , relwidth=0.419)
Frame1.configure(relief='groove')
Frame1.configure(borderwidth="2")
Frame1.configure(relief="groove")
Frame1.configure(background="#d9d9d9")

Label2 = tk.Label(Frame1)
Label2.place(relx=0.022, rely=0.039, height=231, width=426)
Label2.configure(background="#d9d9d9")
Label2.configure(disabledforeground="#a3a3a3")
Label2.configure(foreground="#000000")

Button1 = tk.Button(master, command=lambda : Attaquer(TCombobox1.get()))
Button1.place(relx=0.093, rely=0.708, height=84, width=227)
Button1.configure(activebackground="#ececec")
Button1.configure(activeforeground="#000000")
Button1.configure(background="#d9d9d9")
Button1.configure(disabledforeground="#a3a3a3")
Button1.configure(foreground="#000000")
Button1.configure(highlightbackground="#d9d9d9")
Button1.configure(highlightcolor="black")
Button1.configure(pady="0")
Button1.configure(text='''Attaquer''')

Button2 = tk.Button(master, command=Fuir)
Button2.place(relx=0.667, rely=0.708, height=84, width=227)
Button2.configure(activebackground="#ececec")
Button2.configure(activeforeground="#000000")
Button2.configure(background="#d9d9d9")
Button2.configure(disabledforeground="#a3a3a3")
Button2.configure(foreground="#000000")
Button2.configure(highlightbackground="#d9d9d9")
Button2.configure(highlightcolor="black")
Button2.configure(pady="0")
Button2.configure(text='''Fuir''')

Button3 = tk.Button(master)
Button3.place(relx=0.37, rely=0.833, height=84, width=227)
Button3.configure(activebackground="#ececec")
Button3.configure(activeforeground="#000000")
Button3.configure(background="#d9d9d9")
Button3.configure(disabledforeground="#a3a3a3")
Button3.configure(foreground="#000000")
Button3.configure(highlightbackground="#d9d9d9")
Button3.configure(highlightcolor="black")
Button3.configure(pady="0")
Button3.configure(text='''Quitter''')

TCombobox1 = ttk.Combobox(master, values=armes)
TCombobox1.place(relx=0.093, rely=0.611, relheight=0.057
                 , relwidth=0.206)
TCombobox1.configure(takefocus="")

Scale1 = tk.Scale(master, from_=0.0, to=PvHero)
Scale1.place(relx=0.056, rely=0.125, relwidth=0.414, relheight=0.0
             , height=42, bordermode='ignore')
Scale1.configure(activebackground="#ececec")
Scale1.configure(background="#d9d9d9")
Scale1.configure(foreground="#000000")
Scale1.configure(highlightbackground="#d9d9d9")
Scale1.configure(highlightcolor="black")
Scale1.configure(orient="horizontal")
Scale1.configure(troughcolor="#80f07d")
Scale1.set(PvHero)

Scale2 = tk.Scale(master, from_=0.0, to=PvMonstre)
Scale2.place(relx=0.602, rely=0.125, relwidth=0.32, relheight=0.0
             , height=42, bordermode='ignore')
Scale2.configure(activebackground="#ececec")
Scale2.configure(background="#d9d9d9")
Scale2.configure(foreground="#000000")
Scale2.configure(highlightbackground="#d9d9d9")
Scale2.configure(highlightcolor="black")
Scale2.configure(orient="horizontal")
Scale2.configure(troughcolor="#ff0000")
Scale2.set(PvMonstre)

master.mainloop()
