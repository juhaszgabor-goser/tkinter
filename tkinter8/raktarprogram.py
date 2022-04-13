from tkinter import *
import math
import abc
from tkinter import messagebox
def terfogat():
    def szamit():
        #Terfogat kiszamitasa es adatok bekerese:
        a = (mezo1.get())
        b = (mezo2.get())
        if a.isalpha() or b.isalpha():
            messagebox.showerror("Nem jó","Nem jó,mivel az egyik adat az betu. Zárja be az ablakot és nyissa meg újra.")
        if a <= 0:
            messagebox.showerror("Nem jó","Nem jó,mivel az a adat az 0 vagy kisebb.Zárja be az ablakot és nyissa meg újra")
        if b <= 0:
            messagebox.showerror("Nem jó","Nem jó,mivel a b adat az 0 vagy kisebb.Zárja be az ablakot és nyissa meg újra")
        terfogat= round(math.pi*pow(a,2)*b)
        mezo4.delete(0,END)
        mezo4.insert(0, str(terfogat))
        #Felszin ablaka:
    abl3 = Toplevel(foablak)
    abl3.title("Henger terfogata")
    abl3.minsize(width = 300, height = 300)
    sz1 = Label(abl3, text = "Sugara:")
    sz2 = Label(abl3, text = "Magassága:")
    sz4 = Label(abl3, text ="Eredmény:")
    gomb1 = Button(abl3, text="Számítás", command=szamit)
    gomb2 = Button(abl3)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo4 = Entry(abl3)
    sz1.grid(row = 1)
    sz2.grid(row = 2)
    sz4.grid(row = 5)
    mezo1.grid(row = 1, column = 2)
    mezo2.grid(row = 2, column = 2)
    gomb1.grid(row = 4, column = 1)
    mezo4.grid(row = 5, column = 2)
    abl3.mainloop()
def  felszin():
    def szamit():
        #Felszin kiszamitasa es adatok bekerese:
        a = (mezo1.get())
        b = (mezo2.get())
        if a.isalpha() or b.isalpha():
            messagebox.showerror("Nem jó","Nem jó,mivel az egyik adat az betu. Zárja be az ablakot és nyissa meg újra.")
        felszin = round(2*(a*a)*math.pi+2*a*math.pi*b)
        if a <= 0:
            messagebox.showerror("Nem jó","Nem jó,mivel az a adat az 0 vagy kisebb.Zárja be az ablakot és nyissa meg újra")
        if b <= 0:
            messagebox.showerror("Nem jó","Nem jó,mivel a b adat az 0 vagy kisebb.Zárja be az ablakot és nyissa meg újra")
        mezo4.delete(0,END)
        mezo4.insert(0, str(felszin))
    #Felszin ablaka:
    abl3 = Toplevel(foablak)
    abl3.title("Téglatest felszíne")
    abl3.minsize(width = 300, height = 300)
    sz1 = Label(abl3, text = "Sugara:")
    sz2 = Label(abl3, text = "Magassága:")
    sz4 = Label(abl3, text ="Eredmény:")
    gomb1 = Button(abl3, text="Számítás", command=szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    sz1.grid(row = 1)
    sz2.grid(row = 2)
    sz4.grid(row = 5)
    mezo1.grid(row = 1, column = 2)
    mezo2.grid(row = 2, column = 2)
    gomb1.grid(row = 4, column = 1)
    mezo4.grid(row = 5, column = 2)
    abl3.mainloop()
def  felszin2():
    def szamit():
        #Felszin kiszamitasa es adatok bekerese:
        a = (mezo1.get())
        b = (mezo2.get())
        c = (mezo3.get())
        if a.isalpha() or b.isalpha() or c.isalpha():
            messagebox.showerror("Nem jó","Nem jó,mivel az adatok egyike az betu. Zárja be az ablakot és nyissa meg újra.")
        felszin = 2*(a*b+a*c+b*c)
        if a <= 0:
            messagebox.showerror("Nem jó","Nem jó,mivel a a adat az 0 vagy kisebb.Zárja be az ablakot és nyissa meg újra")
        if b <= 0:
            messagebox.showerror("Nem jó","Nem jó,mivel a b adat az 0 vagy kisebb.Zárja be az ablakot és nyissa meg újra")
        if c <= 0:
            messagebox.showerror("Nem jó","Nem jó,mivel a c adat az 0 vagy kisebb.Zárja be az ablakot és nyissa meg újra")
        mezo4.delete(0,END)
        mezo4.insert(0, str(felszin))
    #Felszin ablaka:
    abl3 = Toplevel(foablak)
    abl3.title("Téglatest felszíne")
    abl3.minsize(width = 300, height = 300)
    sz1 = Label(abl3, text = "a:")
    sz2 = Label(abl3, text = "b:")
    sz3 = Label(abl3, text = "c:")
    sz4 = Label(abl3, text ="Eredmény:")
    gomb1 = Button(abl3, text="Számítás", command=szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    sz1.grid(row = 1)
    sz2.grid(row = 2)
    sz3.grid(row = 3)
    sz4.grid(row = 5)
    mezo1.grid(row = 1, column = 2)
    mezo2.grid(row = 2, column = 2)
    mezo3.grid(row = 3, column = 2)
    gomb1.grid(row = 4, column = 1)
    mezo4.grid(row = 5, column = 2)
    abl3.mainloop()
def terfogat2():
    def szamit():
        #Terfogat kiszamitasa es adatok bekerese:
        a = (mezo1.get())
        b = (mezo2.get())
        c = (mezo3.get())
        if a.isalpha() or b.isalpha() or c.isalpha:
            messagebox.showerror("Nem jó","Nem jó,mivel az egyik adat az betu. Zárja be az ablakot és nyissa meg újra.")
        if a <= 0:
            messagebox.showerror("Nem jó","Nem jó,mivel az a adat az 0 vagy kisebb.Zárja be az ablakot és nyissa meg újra")
        if b <= 0:
            messagebox.showerror("Nem jó","Nem jó,mivel a b adat az 0 vagy kisebb.Zárja be az ablakot és nyissa meg újra")
        if c <= 0:
            messagebox.showerror("Nem jó","Nem jó,mivel a c adat az 0 vagy kisebb.Zárja be az ablakot és nyissa meg újra")
        terfogat = a*b*c
        mezo4.delete(0,END)
        mezo4.insert(0, str(terfogat))
        #Felszin ablaka:
    abl3 = Toplevel(foablak)
    abl3.title("Téglatest terfogata")
    abl3.minsize(width = 300, height = 300)
    sz1 = Label(abl3, text = "a:")
    sz2 = Label(abl3, text = "b:")
    sz3 = Label(abl3, text = "c:")
    sz4 = Label(abl3, text ="Eredmény:")
    gomb1 = Button(abl3, text="Számítás", command=szamit)
    gomb2 = Button(abl3)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    sz1.grid(row = 1)
    sz2.grid(row = 2)
    sz3.grid(row = 3)
    sz4.grid(row = 5)
    mezo1.grid(row = 1, column = 2)
    mezo2.grid(row = 2, column = 2)
    mezo3.grid(row = 3, column = 2)
    gomb1.grid(row = 4, column = 1)
    mezo4.grid(row = 5, column = 2)
    abl3.mainloop()
foablak = Tk()
foablak.title("A henger")
foablak.minsize(width = 300, height = 100)
menusor = Frame(foablak)
menusor.pack(side = TOP, fill = X)
menu1 = Menubutton(menusor, text ="Kilépés", underline = 0)
menu1.pack(side = LEFT)
fajl = Menu(menu1)
fajl.add_command(label = "Kilépés", command = foablak.destroy, underline = 0)
menu1.config( menu = fajl)
menu2 = Menubutton(menusor, text = "Henger", underline = 0)
menu2.pack(side=LEFT)
henger= Menu(menu2)
henger.add_command(label = "Felszíne", command = felszin,underline = 0 )
henger.add_command(label = "Térfogata", command = terfogat, underline = 0 )
menu2.config (menu = henger)
menu3 = Menubutton(menusor, text = "Teglatest", underline = 0)
menu3.pack(side=LEFT)
teglatest= Menu(menu3)
teglatest.add_command(label = "Felszíne", command = felszin2,underline = 0 )
teglatest.add_command(label = "Térfogata", command = terfogat2, underline = 0 )
menu3.config (menu = teglatest)
foablak.mainloop()
foablak.mainloop()