import tkinter as tk
import pygame

pygame.mixer.init()

son = pygame.mixer.Sound('./main_loop.wav')
son.play(loops=-1, maxtime=0, fade_ms=0)

def change_volume(volume):
    son.set_volume(volume)

def getValue(val):
    global var
    var = int(val) / 100
    change_volume(var)

# Création de la fenetre avec tkinter
master = tk.Tk()
master.configure(bg='#92f7cb')  # couleur de fond d'écran
master.geometry("640x480")  # taille par défaut
master.minsize(width="640", height="480")  # taille min
master.maxsize(width="1082", height="720")  # taille max

Labelframe1 = tk.LabelFrame(master)
Labelframe1.place(relx=0.016, rely=0.056, relheight=0.211, relwidth=0.959)
Labelframe1.configure(relief='groove')
Labelframe1.configure(font="-family {Segoe UI} -size 11 -underline 1")
Labelframe1.configure(foreground="black")
Labelframe1.configure(text='''volume''')
Labelframe1.configure(background="#ff8000")

Scale1 = tk.Scale(Labelframe1, from_=0.0, to=100.0, command=getValue)
Scale1.place(relx=0.017, rely=0.267, relwidth=0.959, relheight=0.0, height=42, bordermode='ignore')
Scale1.configure(activebackground="#ff8000")
Scale1.configure(background="#ff8000")
Scale1.configure(foreground="#000000")
Scale1.configure(highlightbackground="#ff8000")
Scale1.configure(highlightcolor="black")
Scale1.configure(orient="horizontal")
Scale1.configure(troughcolor="#ff8000")
Scale1.set(50)

master.mainloop()
