from tkinter import *
from tkinter import messagebox
import mariadb
import sys
class login:
    Fenetre = Tk()
    Fenetre.title("connexion")
    Fenetre.geometry('925x500+300+200')
    Fenetre.configure(bg='#fff')
    Fenetre.resizable(False, False)

    nom = Label(Fenetre, text="nom")
    nom.grid(row=1)
    nom.pack()
    e = Entry(Fenetre, width=30)
    e.pack()
    mdp = Label(Fenetre, text="password")
    nom.grid(row=2)
    mdp.pack()
    e1 = Entry(Fenetre, width=30)
    e1.pack()
    se_connecter = Button(Fenetre, text="connecter" ,command=self.login)
    se_connecter.pack(padx=10, pady=(0, 10))
    creer_compte1 = Button(Fenetre, text="inscription", command=inscription)
    creer_compte1.pack(padx=10, pady=(0, 10))

    def login(self):
        if self.nom.get()=="" or self.password.get()=="":
            messagebox.showerror('error','entrer le nom et le mot de passe')
        else:
            try:
                conn = mariadb.connect(user="root", password="", host="localhost", database="user")
                cursor = conn.cursor()
                cursor.execute("select * from user where nom=? and password=?", (self.nom.get(), self.password.get()))
                row=cursor.fetchone()
                if row == None:
                    messagebox.showerror('error','invalid username and password')
                else:
                    frame_login=frame(fenetre)
                    frame_login.place(x=0,y=0,height=700,width=500)
                    messagebox.showinfo("welcome")

    Fenetre.mainloop()

