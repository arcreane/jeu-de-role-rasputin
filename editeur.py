import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog as fd
import csv
import os

# --- definition des listes pour sauver les choix du createur ---
tmp1 = []
tmp2 = []
tmp3 = []
tmp4 = []
tmp5 = []
tmp6 = []

titre = []
choix1 = []
goto1 = []
choix2 = []
goto2 = []
monstre_histoire = []
nomar = []
descriptionar = []
boostar = []
cheminar = []
attaque = []
defense = []
agilite = []
chance = []

nommon = []
pvmon = []
degatsmon = []
imgmon = []
numero_tmp = []
nommon_tmp = []
pvmon_tmp = []
degatsmon_tmp = []
imgmon_tmp = []

listefinale = []
# --- Fin liste histoire ---

monstres = []  # liste pour afficher les differents monstres disponible dans les dialogues

root = tk.Tk()
root.geometry("1080x720")
root.resizable(0, 0)
root.title("DualCent Editeur")
root.configure(background="#2e2b2a")

icone = tk.PhotoImage(file="./51mF9jwGkEL.png")

root.iconphoto(True, icone)

# --- Images utilisées ---
photo_armes = tk.PhotoImage(file="./Webp.net-resizeimage.png", master=root)
photo_dialogues = tk.PhotoImage(file="./modifier_dialogues.png", master=root)
photo_accessoires = tk.PhotoImage(file="./modifier_monstre.png", master=root)
photo_stats = tk.PhotoImage(file="./modifier_stats.png", master=root)
interrogation = tk.PhotoImage(file="./question-mark-inside-a-circle.png", master=root)


# --- Fin images ---

# --- creation menu editeur ---


def create_menu_editor():
    global nom_entree, sauvenom_bouton, adddialogues_bouton, addarmes_bouton, addmonstres_bouton, addstats_bouton

    def save_nom():  # fonction qui permet de sauvegarder le nom de l'histoire dans une variable s'il y en a un
        global nom_histoire
        special_characters = "!@#$%^&*()-+?_=,<>/"

        if len(nom_entree.get()) == 0:  # verification nom histoire vide
            messagebox.showinfo("Attention !", "Attention, merci de spécifier \nle nom de votre histoire !")
        elif nom_entree.get().isspace():  # verification nom histoire n'est pas que des espaces
            messagebox.showinfo("Attention !", "Attention, le nom de votre histoire\nne doit pas etre vide !")
        elif any(c in special_characters for c in
                 nom_entree.get()):  # verification nom histoire ne contient pas de caracteres speciaux
            messagebox.showinfo("Attention !",
                                "Attention, le nom de votre histoire\nne doit pas contenir des \ncaractères spéciaux !")
        elif len(nom_entree.get()) > 0:  # sinon on enregistre le nom, et les boutons de l'editeur deviennent utilisable
            nom_histoire = str(nom_entree.get()).strip()
            sauvenom_bouton.configure(state="disabled")
            nom_entree.configure(state="disabled")
            adddialogues_bouton.configure(state="normal")
            addarmes_bouton.configure(state="normal")
            addstats_bouton.configure(state="normal")
            addmonstres_bouton.configure(state="normal")
            print(nom_histoire)

        dossier_histoire = ("histoires")
        CHECK_FOLDER = os.path.isdir(dossier_histoire)
        if not CHECK_FOLDER:
            os.makedirs(dossier_histoire)
            print("created folder : ", dossier_histoire)

        else:
            print(dossier_histoire, "folder already exists.")

    titre_label = tk.Label(root, text='''Bienvenue dans l'éditeur :''', background="#fc9403",
                           disabledforeground="#a3a3a3",
                           font="-family {Segoe UI} -size 24 -weight bold -underline 1", foreground="#000000",
                           compound="center")
    titre_label.place(relx=0.046, rely=0.083, height=101, width=975)

    Frame1 = tk.Frame(root, relief='groove', borderwidth="2", background="#fc9403")
    Frame1.place(relx=0.046, rely=0.264, relheight=0.632, relwidth=0.904)

    adddialogues_bouton = tk.Button(Frame1, text='''5) Dialogues''', activebackground="#ececec",
                                    activeforeground="#000000", image=photo_dialogues, compound="left",
                                    background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000",
                                    highlightbackground="#d9d9d9", highlightcolor="black", pady="0", state="disabled",
                                    command=lambda: [titre_label.place_forget(), Frame1.place_forget(),
                                                     create_histoire_window()])
    adddialogues_bouton.place(relx=0.768, rely=0.396, height=104, width=187)

    addarmes_bouton = tk.Button(Frame1, text='''4) Armes''', activebackground="#ececec",
                                activeforeground="#000000", image=photo_armes, state="disabled",
                                background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000",
                                highlightbackground="#d9d9d9", highlightcolor="black", pady=0, compound="left",
                                command=lambda: [titre_label.place_forget(), Frame1.place_forget(),
                                                 create_armes_window()])
    addarmes_bouton.place(relx=0.523, rely=0.396, height=104, width=187)

    addmonstres_bouton = tk.Button(Frame1, text='''3) Monstres''', activebackground="#ececec",
                                   activeforeground="#000000", image=photo_accessoires, compound="left",
                                   background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000",
                                   highlightbackground="#d9d9d9", highlightcolor="black", pady=0, state="disabled",
                                   command=lambda: [titre_label.place_forget(), Frame1.place_forget(),
                                                    create_monstrewindow()])
    addmonstres_bouton.place(relx=0.277, rely=0.396, height=104, width=187)

    addstats_bouton = tk.Button(Frame1, text='''2) Stats''', activebackground="#ececec",
                                activeforeground="#000000", image=photo_stats, compound="left",
                                background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000",
                                highlightbackground="#d9d9d9", highlightcolor="black", pady=0, state="disabled",
                                command=lambda: [titre_label.place_forget(), Frame1.place_forget(),
                                                 create_statswindow()])
    addstats_bouton.place(relx=0.041, rely=0.396, height=104, width=187)

    nom_entree = tk.Entry(Frame1, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                          foreground="#000000",
                          insertbackground="black")
    nom_entree.place(relx=0.205, rely=0.198, height=30, relwidth=0.27)

    nomhistoire_label = tk.Label(Frame1, text='''1) Entrez le nom de votre histoire :''', background="#fc9403",
                                 disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 13 -underline 1",
                                 foreground="#000000")
    nomhistoire_label.place(relx=0.369, rely=0.044, height=41, width=264)

    sauvenom_bouton = tk.Button(Frame1, text='''Save''', activebackground="#ececec", activeforeground="#000000",
                                background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000",
                                highlightbackground="#d9d9d9", highlightcolor="black", pady=0, command=save_nom)
    sauvenom_bouton.place(relx=0.543, rely=0.198, height=34, width=267)

    retour_bouton = tk.Button(Frame1, text='''Retour''', activebackground="#ececec", activeforeground="#000000",
                              background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000",
                              highlightbackground="#d9d9d9", highlightcolor="black", pady=0,
                              command=root.quit)
    retour_bouton.place(relx=0.389, rely=0.769, height=44, width=227)


# --- fin creation menu editeur ---

# --- creation de la fenetre pour ajouter les dialogues et pour dire les differents choix et s'il y a des monstres


def create_histoire_window():  # création fenetre ajout de dialogues
    tmp1.clear()
    tmp2.clear()
    tmp3.clear()
    tmp4.clear()
    tmp5.clear()
    tmp6.clear()

    def update_entree():  # fonction qui permet d'update l'entry avec le nom de l'histoire quand on clique sur le bouton retour
        nom_entree.insert(tk.END, nom_histoire)
        sauvenom_bouton.configure(state="disabled")
        nom_entree.configure(state="disabled")
        adddialogues_bouton.configure(state="normal")
        addarmes_bouton.configure(state="normal")
        addstats_bouton.configure(state="normal")
        addmonstres_bouton.configure(state="normal")

    Frame2 = tk.Frame(root)
    Frame2.place(relx=0.031, rely=0.021, relheight=0.10, relwidth=0.945)
    Frame2.configure(relief='groove')
    Frame2.configure(borderwidth="2")
    Frame2.configure(background="#fc9403")

    title_dialogues_window = tk.Label(Frame2, text="Ajoutez vos dialogues", bg="#fc9403", font=("Arial", 25, "bold"),
                                      fg="black")
    title_dialogues_window.place(relx=0.013, rely=0.015, height=65, width=550)

    def showEntries():  # fonction pour faire les différentes listes, enregistrer toutes les listes dans une seule liste(un peu comme un dico), et ecrire cette listefinale dans le fichier csv
        global listefinale
        titre.clear()
        choix1.clear()
        choix2.clear()
        goto1.clear()
        goto2.clear()
        listefinale.clear()

        for number, ent in enumerate(tmp1):
            titre.append(ent.get())
        for number, ent in enumerate(tmp2):
            choix1.append(ent.get())
        for number, ent in enumerate(tmp3):
            goto1.append(ent.get())
        for number, ent in enumerate(tmp4):
            choix2.append(ent.get())
        for number, ent in enumerate(tmp5):
            goto2.append(ent.get())
        for number, ent in enumerate(tmp6):
            monstre_histoire.append(ent.get())

        titre.insert(0, "titre")
        choix1.insert(0, "choix1")
        goto1.insert(0, "goto1")
        choix2.insert(0, "choix2")
        goto2.insert(0, "goto2")
        monstre_histoire.insert(0, "monstre_histoire")

        listefinale = [titre, choix1, goto1, choix2, goto2, monstre_histoire]

        file = open("./histoires/" + nom_histoire + ".csv", "a+", newline='')
        with file:
            write = csv.writer(file, delimiter=';')
            write.writerows(listefinale)
        file.close()

    def add_box():  # ajout des differentes entries pour les dialogues

        next_column = len(tmp1)
        next_row = next_column + 1

        lab = tk.Label(scrollable_frame, text=str(next_column + 1))
        lab.grid(row=next_row, column=0, pady=(0, 10), padx=(0, 10), ipadx=20)

        ent1 = tk.Entry(scrollable_frame)
        ent1.grid(row=next_row, column=1, pady=(0, 10), padx=(0, 10), ipadx=24)

        ent2 = tk.Entry(scrollable_frame)
        ent2.grid(row=next_row, column=2, pady=(0, 10), padx=(0, 10), ipadx=24)

        ent3 = tk.Entry(scrollable_frame)
        ent3.grid(row=next_row, column=3, pady=(0, 10), padx=(0, 10), ipadx=24)

        ent4 = tk.Entry(scrollable_frame)
        ent4.grid(row=next_row, column=4, pady=(0, 10), padx=(0, 10), ipadx=24)

        ent5 = tk.Entry(scrollable_frame)
        ent5.grid(row=next_row, column=5, pady=(0, 10), padx=(0, 10), ipadx=24)

        ent6 = ttk.Combobox(scrollable_frame, values=monstres)
        ent6.grid(row=next_row, column=6, pady=(0, 10), padx=(0, 10), ipadx=24)

        tmp1.append(ent1)
        tmp2.append(ent2)
        tmp3.append(ent3)
        tmp4.append(ent4)
        tmp5.append(ent5)
        tmp6.append(ent6)

    add_boutton = tk.Button(Frame2, command=add_box)
    add_boutton.place(relx=0.8, rely=0.15, height=50, width=100)
    add_boutton.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9",
                          disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                          highlightcolor="black", pady="0", text="Add")

    container = tk.Frame(root)

    canvas = tk.Canvas(container)
    canvas.configure(background="#2e2b2a")
    canvas.configure(borderwidth="2")
    canvas.configure(insertbackground="black")
    canvas.configure(relief="ridge")
    canvas.configure(selectbackground="blue")
    canvas.configure(selectforeground="white")
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollbarx = tk.Scrollbar(container, orient="horizontal", command=canvas.xview)
    scrollbarx.pack(side="bottom", fill="x")
    scrollable_frame = tk.Frame(canvas)
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set, xscrollcommand=scrollbarx.set)
    container.place(relx=0.031, rely=0.188, relheight=0.777, relwidth=0.942)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    incre = 0

    def Label(n, incre):  # fonction pour afficher les titres
        writelabel = tk.Label(scrollable_frame, background="#d9d9d9", disabledforeground="#a3a3a3",
                              foreground="#000000", text=n)
        writelabel.grid(row=0, column=incre, pady=(0, 10), padx=(0, 10))
        return writelabel

    Label("id", incre)
    Label("Question ?", incre + 1)
    Label("Choix 1 ?", incre + 2)
    Label("Lien vers 1 ?", incre + 3)
    Label("Choix 2 ?", incre + 4)
    Label("Lien vers 2 ?", incre + 5)

    add_box()

    col_count, row_count = scrollable_frame.grid_size()

    scrollable_frame.grid_columnconfigure(0, minsize=20)
    for col in range(1, col_count):
        scrollable_frame.grid_columnconfigure(col, minsize=25)

    return_button = tk.Button(root, text="Sauvegarder &\nRetourner à \n la page précédente", font=("Arial", 12),
                              fg="black",
                              command=lambda: [showEntries(), return_button.place_forget(), Frame2.place_forget(),
                                               container.place_forget(), create_menu_editor(),
                                               tmp1.clear(), tmp2.clear(), tmp3.clear(),
                                               tmp4.clear(), tmp5.clear(), update_entree()])
    return_button.place(relx=0.8, rely=0.85, height=60, width=150)


# --- fin creation fenetre des dialogues ---

# --- creation de la fenetre pour ajouter des armes afin de combattre des monstres ---


def create_armes_window():
    tmp1.clear()
    tmp2.clear()
    tmp3.clear()
    tmp4.clear()
    tmp5.clear()
    tmp6.clear()

    def update_entree():  # fonction qui permet d'update l'entry avec le nom de l'histoire quand on clique sur le bouton retour
        nom_entree.insert(tk.END, nom_histoire)
        sauvenom_bouton.configure(state="disabled")
        nom_entree.configure(state="disabled")
        adddialogues_bouton.configure(state="normal")
        addarmes_bouton.configure(state="normal")
        addstats_bouton.configure(state="normal")
        addmonstres_bouton.configure(state="normal")

    Frame3 = tk.Frame(root)
    Frame3.place(relx=0.031, rely=0.021, relheight=0.10, relwidth=0.945)
    Frame3.configure(relief='groove')
    Frame3.configure(borderwidth="2")
    Frame3.configure(background="#fc9403")

    title_dialogues_window = tk.Label(Frame3, text="Ajoutez des armes", bg="#fc9403", font=("Arial", 25, "bold"),
                                      fg="black")
    title_dialogues_window.place(relx=0.013, rely=0.015, height=65, width=550)

    def showEntries():  # fonction pour faire les différentes listes, enregistrer toutes les listes dans une seule liste(un peu comme un dico), et ecrire cette listefinale dans le fichier csv
        global listefinale
        nomar.clear()
        descriptionar.clear()
        boostar.clear()
        cheminar.clear()
        listefinale.clear()

        for number, ent in enumerate(tmp1):
            print(number, ent.get())
            nomar.append(ent.get())
        for number, ent in enumerate(tmp2):
            print(number, ent.get())
            descriptionar.append(ent.get())
        for number, ent in enumerate(tmp3):
            print(number, ent.get())
            boostar.append(ent.get())
        for number, ent in enumerate(tmp4):
            print(number, ent.get())
            cheminar.append(ent.get())
        nomar.insert(0, "nom_arme")
        descriptionar.insert(0, "description_arme")
        boostar.insert(0, "boost_arme")
        cheminar.insert(0, "chemin_arme")

        listefinale = [nomar, descriptionar, boostar, cheminar]
        print(listefinale)

        file = open("./histoires/" + nom_histoire + ".csv", "a+", newline='')
        with file:
            write = csv.writer(file, delimiter=";")
            write.writerows(listefinale)
        file.close()

    def addBox():  # fonction pour ajouter les differetes entries a la fenetre
        global ent1, ent2, ent3, ent4, ent5, ent6

        # print("ADD")

        def openfile_path():  # fonction qui permet d'ajouter une image dans une entry et qui bloque l'entry apres
            filename = fd.askopenfilename(filetype=[("Image PNG", ".png")])
            ent6.configure(state="normal")
            ent6.delete(0, "end")
            ent6.insert(0, filename)
            ent6.configure(state="disabled")

        next_column = len(tmp1)
        next_row = next_column + 1

        lab = tk.Label(scrollable_frame, text=str(next_column + 1))
        lab.grid(row=next_row, column=0, pady=(0, 10), padx=(0, 10), ipadx=20)

        ent1 = tk.Entry(scrollable_frame)
        ent1.grid(row=next_row, column=1, pady=(0, 10), padx=(0, 10), ipadx=25)

        ent2 = tk.Entry(scrollable_frame)
        ent2.grid(row=next_row, column=2, pady=(0, 10), padx=(0, 10), ipadx=25)

        ent4 = tk.Spinbox(scrollable_frame, from_=0, to_=50)
        ent4.grid(row=next_row, column=3, pady=(0, 10), padx=(0, 10), ipadx=25)

        ent5 = tk.Button(scrollable_frame, command=openfile_path, text="image")
        ent5.grid(row=next_row, column=4, pady=(0, 10), ipadx=5)

        ent6 = tk.Entry(scrollable_frame)
        ent6.grid(row=next_row, column=5, pady=(0, 10), padx=(10, 10), ipadx=30)

        tmp1.append(ent1)
        tmp2.append(ent2)
        tmp3.append(ent4)
        tmp4.append(ent6)

    add_boutton = tk.Button(Frame3, command=addBox)
    add_boutton.place(relx=0.8, rely=0.15, height=50, width=100)
    add_boutton.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9",
                          disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                          highlightcolor="black", pady="0", text="Add")

    container = tk.Frame(root)

    canvas = tk.Canvas(container)
    canvas.configure(background="#2e2b2a")
    canvas.configure(borderwidth="2")
    canvas.configure(insertbackground="black")
    canvas.configure(relief="ridge")
    canvas.configure(selectbackground="blue")
    canvas.configure(selectforeground="white")
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollbarx = tk.Scrollbar(container, orient="horizontal", command=canvas.xview)
    scrollbarx.pack(side="bottom", fill="x")
    scrollable_frame = tk.Frame(canvas)
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set, xscrollcommand=scrollbarx.set)
    container.place(relx=0.031, rely=0.188, relheight=0.777, relwidth=0.942)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    incre = 0

    def Label(n, incre):
        writelabel = tk.Label(scrollable_frame, background="#d9d9d9", disabledforeground="#a3a3a3",
                              foreground="#000000",
                              text=n)
        writelabel.grid(row=0, column=incre, pady=(0, 10), padx=(0, 10))
        return writelabel

    Label("id", incre)
    Label("Nom de l'arme", incre + 1)
    Label("Description", incre + 2)
    Label("Combien de degats", incre + 3)
    Label("Image ?", incre + 4)
    Label("Chemin de l'image", incre + 5)

    addBox()

    col_count, row_count = scrollable_frame.grid_size()
    print(col_count)

    scrollable_frame.grid_columnconfigure(0, minsize=20)
    for col in range(1, col_count):
        scrollable_frame.grid_columnconfigure(col, minsize=25)

    return_button = tk.Button(root, text="Sauvegarder &\nRetourner à \n la page précédente", font=("Arial", 12),
                              fg="black",
                              command=lambda: [showEntries(), return_button.place_forget(), Frame3.place_forget(),
                                               container.place_forget(), create_menu_editor(),
                                               tmp1.clear(), tmp2.clear(), tmp3.clear(),
                                               tmp4.clear(), tmp5.clear(), update_entree()])
    return_button.place(relx=0.8, rely=0.85, height=60, width=150)


# --- fin creation fenetre pour ajouter des armes ---

# --- creation de la fenetre pour gerer les statiqtiques du joueur ---


def create_statswindow():
    def update_entree():  # fonction qui permet d'update l'entry avec le nom de l'histoire quand on clique sur le bouton retour
        nom_entree.insert(tk.END, nom_histoire)
        sauvenom_bouton.configure(state="disabled")
        nom_entree.configure(state="disabled")
        adddialogues_bouton.configure(state="normal")
        addarmes_bouton.configure(state="normal")
        addstats_bouton.configure(state="normal")
        addmonstres_bouton.configure(state="normal")

    global scale_attaque, scale_defense, scale_agilite, scale_chance, Frame5, monTexte, label_update, Frame4
    monTexte = tk.StringVar()
    monTexte.set("Il vous reste 30 points !")

    Frame4 = tk.Frame(root, relief='groove', borderwidth="2", background="#ffb44d")
    Frame4.place(relx=0.017, rely=0.022, relheight=0.167, relwidth=0.958)

    label_caracteristiques = tk.Label(Frame4, text='''Choisissez vos caractéristiques de bases:''',
                                      background="#ffb44d",
                                      disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 14 -underline 1",
                                      foreground="#000000")
    label_caracteristiques.place(relx=0.016, rely=0.25, height=54, width=350)

    label_update = tk.Label(Frame4, textvariable=monTexte, background="#ffb44d", disabledforeground="#a3a3a3",
                            font="-family {Segoe UI} -size 14", foreground="#000000")
    label_update.place(relx=0.735, rely=0.25, height=54, width=264)

    Labelframe1 = tk.LabelFrame(root, relief='groove', foreground="black", text='''Attaque''', background="#ffb44d")
    Labelframe1.place(relx=0.016, rely=0.2, relheight=0.189, relwidth=0.781)

    scale_attaque = tk.Scale(Labelframe1, from_=0.0, to=30, command=update_text, activebackground="#ececec",
                             background="#ffb44d", foreground="#000000", highlightbackground="#ffb44d",
                             highlightcolor="black", length="586", orient="horizontal", troughcolor="#ffb44d")
    scale_attaque.place(relx=0.016, rely=0.271, relheight=0.580, relwidth=0.962)

    Labelframe2 = tk.LabelFrame(root, relief='groove', foreground="black", text='''Défense''', background="#ffb44d")
    Labelframe2.place(relx=0.016, rely=0.4, relheight=0.189, relwidth=0.781)

    scale_defense = tk.Scale(Labelframe2, from_=0.0, to=30, command=update_text, activebackground="#ececec",
                             background="#ffb44d", foreground="#000000", highlightbackground="#ffb44d",
                             highlightcolor="black", length="586", orient="horizontal", troughcolor="#ffb44d")
    scale_defense.place(relx=0.016, rely=0.271, relheight=0.580, relwidth=0.962)

    Labelframe3 = tk.LabelFrame(root, relief='groove', foreground="black", text='''Agilité''', background="#ffb44d")
    Labelframe3.place(relx=0.016, rely=0.6, relheight=0.189, relwidth=0.781)

    scale_agilite = tk.Scale(Labelframe3, from_=0.0, to=30, command=update_text, activebackground="#ececec",
                             background="#ffb44d", foreground="#000000", highlightbackground="#ffb44d",
                             highlightcolor="black", length="586", orient="horizontal", troughcolor="#ffb44d")
    scale_agilite.place(relx=0.016, rely=0.271, relheight=0.580, relwidth=0.962)

    Labelframe4 = tk.LabelFrame(root, relief='groove', foreground="black", text='''Chance''', background="#ffb44d")
    Labelframe4.place(relx=0.016, rely=0.8, relheight=0.189, relwidth=0.781)

    scale_chance = tk.Scale(Labelframe4, from_=0.0, to=30, command=update_text, activebackground="#ececec",
                            background="#ffb44d", foreground="#000000", highlightbackground="#ffb44d",
                            highlightcolor="black", length="586", orient="horizontal", troughcolor="#ffb44d")
    scale_chance.place(relx=0.016, rely=0.271, relheight=0.580, relwidth=0.962)

    Frame5 = tk.Frame(root, relief='groove', borderwidth="2", background="#ffb44d")
    Frame5.place(relx=0.813, rely=0.2, relheight=0.789, relwidth=0.164)

    bouton_retour = tk.Button(Frame5, text='''Retour''',
                              command=lambda: [create_menu_editor(), update_entree(), Frame4.place_forget(),
                                               Frame5.place_forget(),
                                               Labelframe1.place_forget(), Labelframe2.place_forget(),
                                               Labelframe3.place_forget(), Labelframe4.place_forget()],
                              activebackground="#ececec", activeforeground="#000000",
                              font="-family {Segoe UI} -size 12", disabledforeground="#a3a3a3", foreground="#000000",
                              highlightbackground="#d9d9d9", highlightcolor="black", pady="0")
    bouton_retour.place(relx=0.095, rely=0.817, height=44, width=87)


def reinit():  # fonction pour reinitialiser les statistiques si l'utilisateur clique sur le bouton reinitialiser
    scale_attaque.config(state="normal", takefocus=0)
    scale_agilite.config(state="normal", takefocus=0)
    scale_defense.config(state="normal", takefocus=0)
    scale_chance.config(state="normal", takefocus=0)
    scale_attaque.set(0)
    scale_agilite.set(0)
    scale_defense.set(0)
    scale_chance.set(0)
    bouton_savecara.place_forget()
    bouton_reinitcara.place_forget()
    label_update.configure(background="#ffb44d")
    label_update.configure(foreground="#000000")


def update_text(var):  # fonction pour update le nombre de points restants
    global bouton_savecara, bouton_reinitcara

    bouton_savecara = tk.Button(Frame5, command=save_stats)

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

        bouton_savecara.place(relx=0.095, rely=0.197, height=44, width=87)
        bouton_savecara.configure(activebackground="#ececec")
        bouton_savecara.configure(activeforeground="#000000")
        bouton_savecara.configure(disabledforeground="#a3a3a3")
        bouton_savecara.configure(font="-family {Segoe UI} -size 12")
        bouton_savecara.configure(foreground="#000000")
        bouton_savecara.configure(highlightbackground="#d9d9d9")
        bouton_savecara.configure(highlightcolor="black")
        bouton_savecara.configure(pady="0")
        bouton_savecara.configure(text='''Save''')

        bouton_reinitcara = tk.Button(Frame5, text='''Réinitialiser''', command=reinit, activebackground="#ececec",
                                      activeforeground="#000000", disabledforeground="#a3a3a3",
                                      font="-family {Segoe UI} -size 12", foreground="#000000",
                                      highlightbackground="#d9d9d9", highlightcolor="black", pady="0")
        bouton_reinitcara.place(relx=0.095, rely=0.507, height=44, width=87)

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

        bouton_reinitcara = tk.Button(Frame5, text='''Réinitialiser''', command=reinit, activebackground="#ececec",
                                      activeforeground="#000000", disabledforeground="#a3a3a3",
                                      font="-family {Segoe UI} -size 12", foreground="#000000",
                                      highlightbackground="#d9d9d9", highlightcolor="black", pady="0")
        bouton_reinitcara.place(relx=0.095, rely=0.507, height=44, width=87)


def save_stats():  # fonction pour sauvegarder les statiqtiques du joueur dans un fichier csv
    global listefinale

    listefinale.clear()

    attaque_pt = scale_attaque.get()
    defense_pt = scale_defense.get()
    agilite_pt = scale_agilite.get()
    chance_pt = scale_chance.get()

    attaque.append(attaque_pt)
    defense.append(defense_pt)
    agilite.append(agilite_pt)
    chance.append(chance_pt)
    attaque.insert(0, "attaque")
    defense.insert(0, "defense")
    agilite.insert(0, "agilite")
    chance.insert(0, "chance")

    listefinale = [attaque, defense, agilite, chance]

    file = open("./histoires/" + nom_histoire + ".csv", "a+", newline='')
    with file:
        write = csv.writer(file, delimiter=';')
        write.writerows(listefinale)
    file.close()


# --- fin creation de la fenetre pour modifier les statiqtiques ---

# --- creation de la fenetre pour ajouter des monstres ---


def create_monstrewindow():
    def update_entree():  # fonction qui permet d'update l'entry avec le nom de l'histoire quand on clique sur le bouton retour
        nom_entree.insert(tk.END, nom_histoire)
        sauvenom_bouton.configure(state="disabled")
        nom_entree.configure(state="disabled")
        adddialogues_bouton.configure(state="normal")
        addarmes_bouton.configure(state="normal")
        addstats_bouton.configure(state="normal")
        addmonstres_bouton.configure(state="normal")

    Frame1 = tk.Frame(root)
    Frame1.place(relx=0.031, rely=0.021, relheight=0.10, relwidth=0.945)
    Frame1.configure(relief='groove')
    Frame1.configure(borderwidth="2")
    Frame1.configure(relief="groove")
    Frame1.configure(background="#fc9403")

    title_dialogues_window = tk.Label(Frame1, text="Ajoutez les monstres", bg="#fc9403", font=("Arial", 25, "bold"),
                                      fg="black")
    title_dialogues_window.place(relx=0.013, rely=0.015, height=65, width=550)

    def showEntries():  # fonction pour faire les différentes listes, enregistrer toutes les listes dans une seule liste(un peu comme un dico), et ecrire cette listefinale dans le fichier csv
        global listefinale

        nommon.clear()
        pvmon.clear()
        imgmon.clear()
        degatsmon.clear()
        goto2.clear()
        listefinale.clear()

        for number, ent in enumerate(nommon_tmp):
            # print(number, ent.get())
            nommon.append(ent.get())
            monstres.append(ent.get())
        for number, ent in enumerate(pvmon_tmp):
            # print(number, ent.get())
            pvmon.append(ent.get())
        for number, ent in enumerate(degatsmon_tmp):
            # print(number, ent.get())
            degatsmon.append(ent.get())
        for number, ent in enumerate(imgmon_tmp):
            # print(number, ent.get())
            imgmon.append(ent.get())
        print(monstres)
        nommon.insert(0, "nommon")
        pvmon.insert(0, "pvmon")
        degatsmon.insert(0, "degatsmon")
        imgmon.insert(0, "imgmon")
        print(nommon, pvmon, degatsmon, imgmon)

        listefinale = [nommon, pvmon, degatsmon, imgmon]
        print(listefinale)

        file = open("./histoires/" + nom_histoire + ".csv", "a+", newline='')
        with file:
            write = csv.writer(file, delimiter=";")
            write.writerows(listefinale)
        file.close()

    def addBox():
        next_column = len(nommon_tmp)
        next_row = next_column + 1

        def openfile_path():
            filename = fd.askopenfilename(filetype=[("Image PNG", ".png")])
            ent5.configure(state="normal")
            ent5.delete(0, "end")
            ent5.insert(0, filename)
            ent5.configure(state="disabled")

        lab = tk.Label(scrollable_frame, text=str(next_column + 1))
        lab.grid(row=next_row, column=0, pady=(0, 10), padx=(0, 10), ipadx=20)

        ent1 = tk.Entry(scrollable_frame)
        ent1.grid(row=next_row, column=1, pady=(0, 10), padx=(0, 10), ipadx=25)

        ent2 = tk.Spinbox(scrollable_frame, from_=1, to_=50)
        ent2.grid(row=next_row, column=2, pady=(0, 10), padx=(0, 10), ipadx=25)

        ent3 = tk.Spinbox(scrollable_frame, from_=1, to_=50)
        ent3.grid(row=next_row, column=3, pady=(0, 10), padx=(0, 10), ipadx=25)

        ent4 = tk.Button(scrollable_frame, text="Image", command=openfile_path)
        ent4.grid(row=next_row, column=4, pady=(0, 10), padx=(0, 10), ipadx=25)

        ent5 = tk.Entry(scrollable_frame)
        ent5.grid(row=next_row, column=5, pady=(0, 10), padx=(0, 10), ipadx=30)

        nommon_tmp.append(ent1)
        pvmon_tmp.append(ent2)
        degatsmon_tmp.append(ent3)
        imgmon_tmp.append(ent5)

    add_boutton = tk.Button(Frame1, command=addBox)
    add_boutton.place(relx=0.8, rely=0.15, height=50, width=100)
    add_boutton.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9",
                          disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                          highlightcolor="black", pady="0", text="Add")

    container = tk.Frame(root)

    canvas = tk.Canvas(container)
    canvas.configure(background="#2e2b2a")
    canvas.configure(borderwidth="2")
    canvas.configure(insertbackground="black")
    canvas.configure(relief="ridge")
    canvas.configure(selectbackground="blue")
    canvas.configure(selectforeground="white")
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollbarx = tk.Scrollbar(container, orient="horizontal", command=canvas.xview)
    scrollbarx.pack(side="bottom", fill="x")
    scrollable_frame = tk.Frame(canvas)
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set, xscrollcommand=scrollbarx.set)
    container.place(relx=0.031, rely=0.188, relheight=0.777, relwidth=0.942)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    incre = 0

    def Label(n, incre):
        writelabel = tk.Label(scrollable_frame, background="#d9d9d9", disabledforeground="#a3a3a3",
                              foreground="#000000",
                              text=n)
        writelabel.grid(row=0, column=incre, pady=(0, 10), padx=(0, 10))
        return writelabel

    Label("id", incre)
    Label("Nom du monstre ?", incre + 1)
    Label("PV ?", incre + 2)
    Label("dégats infligés ?", incre + 3)
    Label("Image", incre + 4)
    Label("Chemin", incre + 5)

    addBox()

    col_count, row_count = scrollable_frame.grid_size()
    print(col_count)
    scrollable_frame.grid_columnconfigure(0, minsize=20)
    for col in range(1, col_count):
        scrollable_frame.grid_columnconfigure(col, minsize=25)

    return_button = tk.Button(root, text="Sauvegarder &\nRetourner à \n la page précédente", font=("Arial", 12),
                              fg="black",
                              command=lambda: [showEntries(), return_button.place_forget(), Frame1.place_forget(),
                                               container.place_forget(), create_menu_editor(),
                                               tmp1.clear(), tmp2.clear(), tmp3.clear(),
                                               tmp4.clear(), tmp5.clear(), update_entree()])
    return_button.place(relx=0.8, rely=0.85, height=60, width=150)


# --- fin creation fenetre pour ajouter des monstres ---


create_menu_editor()

root.mainloop()
