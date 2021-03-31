import tkinter as tk

#creation de la fenetre editor tkinter
editor = tk.Tk()
editor.configure(bg='#92cbf7') #Couleur du background en bleu clair
editor.geometry("1440x1080") #Taille page
editor.minsize(width="1440", height="1080")
editor.maxsize(width="1600", height="1200")

title2=tk.Label(text="Vous etes dans l'editeur du jeu", bg='#92cbf7', font=("Arial", 20, "bold"), fg="black")
title2.pack(side="top", pady=50)
