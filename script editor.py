import tkinter as tk

top = tk.Tk()
tk.Label(top, text="Première question").grid(row=0, column=0)
tk.Label(top, text="Choix 1").grid(row=0, column=1)
tk.Label(top, text="Choix 2").grid(row=0, column=2)
tk.Label(top, text="Choix 3").grid(row=0, column=3)
e1=tk.Entry(top)
e1.grid(row=1, column=0)
e2=tk.Entry(top)
e2.grid(row=1, column=1)
e3=tk.Entry(top)
e3.grid(row=1, column=2)
e4=tk.Entry(top)
e4.grid(row=1, column=3)

a = e1.get()
b = e2.get()
c = e3.get()
d = e4.get()

#FOUTRE UN BOUTON SAUVEGARDER EN CSV

top.mainloop()
