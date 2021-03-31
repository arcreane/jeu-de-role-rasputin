import tkinter as tk

master = tk.Tk()
master.geometry("600x400")
master.configure(bg="grey")

title = tk.Label(master, text="Bienvenue sur le jeu", bg="cyan", font=("Arial", 20, "bold"))
title.pack(side="top", pady=50)


game = tk.Button(frame1, text="Charger sauvegarde", background="orange")
game.grid(row="0", column="0", ipady=10, padx=10, pady=10)

editor = tk.Button(frame1, text="Nouvelle Partie", background="orange")
editor.grid(row="0", column="1", ipady=10, padx=10, pady=10)

menu_bar = tk.Menu(master)
file_menu = tk.Menu(menu_bar, tearoff=0) #création du menu en haut de la page
file_menu.add_command(label="Quitter", command=master.quit)
menu_bar.add_cascade(label"Fichier", menu=file_menu)
master.config(menu=menu_bar)

master.mainloop()
