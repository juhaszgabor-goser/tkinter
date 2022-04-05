from tkinter import *

abl1 = Tk()

def ujablak():
    abl2 = Toplevel(abl1)
    uzenet2 = Message(abl2, text ="Készítette: Gipsz Jakab\nPiripócs\n2009.06.04", width = 150)
    gomb2 = Button(abl2,text = "kilép", command=abl2.destroy)
    uzenet2.pack()
    gomb2.pack()
    abl2.mainloop()

szoveg1 = Label(abl1,text = "Kattints a Névjegy gombra!")
szoveg1.pack()
gomb1 = Button(abl1,text = "Névjegy", command=ujablak)
gomb1.pack()

abl1.mainloop()