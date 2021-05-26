import tkinter as tk


root = tk.Tk()
root.geometry("1920x1080")
root.minsize(200,100)
root.maxsize(2000, 1100)
root.resizable(0, 0)
root.title("New Toplevel")
root.configure(background="#2e2b2a")
Frame1 = tk.Frame(root, relief='groove', borderwidth="2", background="#fc9403")
Frame1.place(relx=0.046, rely=0.264, relheight=0.632, relwidth=0.904)


#class Monstre :
    def __init__(self, niveau, PV_monstre):
        self.PV_monstre = 100 * niveau
        self.attaque = 20 * niveau


    def action_combat(self, hero):
        dégats = random.randrange(self.attaque / 2, self.attaque)
        if hero.blocage:
            print("Le Monstre vous attaque, vous perdez ",Hit,"PV.")
            format(dégats/2)
            PV_hero -= dégats/2
        else:
            print("Le Monstre vous attaque, vous perdez",Hit," PV.")
            format(dégats)
            PV_hero -= dégats

#class Hero:

    def __init__(self, nom_hero, attaque_hero, PV_hero):
        self.PV = PV_hero
        self.attaque = attaque_hero
        self.nom = nom_hero
        self.blocage = False

    def combat(self):
        attack_bouton = tk.Button(Frame1, text='''Attaquer''', activebackground="#ececec",
                                  activeforeground="#000000",
                                  background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000",
                                  highlightbackground="#d9d9d9", highlightcolor="black", pady=0, compound="left",
                                  command= attaque_ennemie)
        attack_bouton.place(relx=0.600, rely=0.8, height=104, width=187)

        defend_bouton = tk.Button(Frame1, text='''Défendre''', activebackground="#ececec",
                                  activeforeground="#000000",
                                  background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000",
                                  highlightbackground="#d9d9d9", highlightcolor="black", pady=0, compound="left",
                                  command=blocage)
        defend_bouton.place(relx=0.300, rely=0.8, height=104, width=187)
    def attaque_ennemie(self, Monstre):
        dégats = random.randrange(int(self.attaque / 2), self.attaque)
        print(f"Vous attaquez le Monstre ! {dégats} Il prend dégats")
        PV_monstre -= dégats
        print(f"Le Monstre n'a plus que {PV_monstre} PV")

    def blocage(self):
        print("Vous prenez une position défensive!")
        self.blocage = True

    def attaque_combat(self, Monstre):
        self.blocage = False

        option_action = int(input("Action: "))
        if option_action == 1:
            self.attaque_ennemie(Monstre)
        elif option_action == 2:
            self.blocage()
