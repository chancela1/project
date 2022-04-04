from tkinter import *

from tkinter import messagebox
import mariadb
import sys

root = tk()
root.title('formulaire d''inscription')
width = 640
height = 480
screen_width = root_winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
NOM = stringVar()
MAIL = stringVar()
MDP = stringVar()
CMDP = stringVar()


def database():
    global conn, cursor
    conn = mariadb.connect(user="root", password="", host="localhost", database="user")
    cursor = conn.cursor()


def formulaire:
    database()
    if NOM.get() == "" or MAIL.get() == "" or MDP.get() == "" or CMDP.get() == "":
        lbl_result.config(text="comple the required field")
    else:
        cursor.execute("select * from `user` where `NOM`='{}'", (NOM.get()))
        if cursor.fetchone() is not None:
            lbl_result.config(text="username is already taken")
        else:
            cursor.execute("insert into `user` values(?,?,?,?)",
                           (str(NOM.get()), str(MAIL.get()), str(MDP.get()), str(CMDP.get())))
            conn.commit()
            NOM.set("")
            MAIL.set("")
            MDP.set("")
            CMDP.set("")
            lbl_result.config(text="SUCCESSFULLY")
        cursor.close()
        conn.close()

        titleframe = frame(root, height=100, width=640)
        titleframe.pack(side=TOP)
        formulaireframe = frame(root)
        formulaireframe.pack(side=TOP)
        lbl_title = label(titleframe, text=formulaire
        dinscription)
        lbl_title.pack()
        l2 = Label(formulaireframe, text="entrer votre nom et prenom")
        l2.grid(row=1)
        l2.pack()
        global l2_entry
        l2_entry = Entry(formulaireframe, width=30, textvariable=NOM)

        l2_entry.pack()
        l3 = Label(formulaireframe, text="entrer votre mail")
        l3.grid(row=2)
        l3.pack()
        global e3
        e3 = Entry(formulaireframe, width=30, textvariable=MAIL)
        e3.pack()
        l4 = Label(formulaireframe, text="entrer votre mot de passe")
        l4.grid(row=3)
        l4.pack()
        global e4
        e4 = Entry(formulaireframe, width=30, textvariable=MDP)
        e4.pack()
        l5 = Label(formulaireframe, text="entrer votre mot de passe de confirmation")
        l5.grid(row=4)
        l5.pack()
        global e5
        e5 = Entry(formulaireframe, width=30, textvariable=CMDP)
        e5.pack()
        bouton_sou = Button(formulaireframe, text="formulaire", command=formulaire)

        bouton_sou.pack(padx=10, pady=(0, 10))
        formulaireframe.pack(expand=YES)
if__name__=="__main__":
    root.mainloop()
