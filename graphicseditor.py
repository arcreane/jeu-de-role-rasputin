import tkinter as tk

#creation de la fenetre editor tkinter
editor = tk.Tk()
editor.configure(bg='#92cbf7') #Couleur du background en bleu clair
editor.geometry("1080x720") #Taille page

title2=tk.Label(text="Vous etes dans l'editeur du jeu", bg='#92cbf7', font=("Arial", 20, "bold"), fg="black")
title2.pack(side="top", pady=50)

frame1=tk.Frame(editor, bg='#fc9403')
frame1.pack()

photo_stats = tk.PhotoImage(file = r"./Plan-de-travail-6-150x150.png")
photo_items =
photo_dialogues = 

stats=tk.Button(frame1, text="Changer les valeurs des Stats", image=photo_stats, compound="top") #command=stats_edit_window
stats.grid(row="0", column="0", ipady=10, padx=10, pady=10)

items=tk.Button(frame1, text="Ajouter des items et definir l'inventaire dans votre jeu") #command=items_edit_window
items.grid(row="1", column="0", ipady=10, padx=10, pady=10)

dialogues=tk.Button(frame1, text="Ajouter les dialogues dans votre jeu") #command=dialogues_edit_window
dialogues.grid(row="2", column="0", ipady=10, padx=10, pady=10)

editor.mainloop()
