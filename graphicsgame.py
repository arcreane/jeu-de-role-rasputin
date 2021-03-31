import tkinter as tk

#creation de la fenetre editor tkinter
gamepage = tk.Tk()
gamepage.configure(bg='#92cbf7') #Couleur du background en bleu clair
gamepage.geometry("1080x720") #Taille page

title=tk.Label(text="Vous etes actuellement en train de jouer", bg='#92cbf7', font=("Arial", 20, "bold"), fg="black")
title.pack(side="top", pady=50)

frame=tk.Frame(editor, bg='#fc9403')
frame.pack()

editor.mainloop()

