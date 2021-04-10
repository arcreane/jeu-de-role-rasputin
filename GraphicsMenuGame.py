import tkinter as tk

master = tk.Tk()
master.geometry("600x400")
master.configure(bg="#b9b4b3")

frame1=tk.Frame(master, bg='#b9b4b3')
frame1.pack()

cgame = tk.Button(frame1, text="Charger sauvegarde", background="#f3a421")
cgame.grid(row="0", column="0", ipady=10, padx=10, pady=150)

ngame = tk.Button(frame1, text="Nouvelle Partie", background="#f3a421")
ngame.grid(row="0", column="1", ipady=10, padx=10, pady=150)

menu_bar = tk.Menu(master)
file_menu = tk.Menu(menu_bar, tearoff=0) #création du menu en haut de la page
file_menu.add_command(label="Quitter", command=master.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)
master.config(menu=menu_bar)

master.mainloop()
