from tkinter import *
import math
def terfogat():
    a = float(mezo1.get())
    b = float(mezo2.get())
    d = float(mezo3.get())
    c= math.pi*pow(a,2)*b
    valami  = c/1000
    mezo4.delete(0, END)
    mezo4.insert(0,+float("%.0f" % c))
    if valami > d:
        belefer = True
    else: 
        belefer = False
    if belefer:
        mezo5.delete(0,END)
        mezo5.insert(0,"Belefér")
    else:
        mezo5.delete(0,END)
        mezo5.insert(0,"Nem fér bele")
    szamolas = d/c
    mezo6.delete(0,END)
    mezo6.insert(0,float("ennyi % van meg"+szamolas))


foablak = Tk()
eleres = 'H:\\IKT\\python\\tkinter4\\'
foablak.title("Henger folyadék")
icon = PhotoImage(file = eleres+"img_507427.png",)
foablak.iconphoto(True, icon)
szoveg1=Label(foablak, text="Bor mennyisége literben:")
szoveg1.grid(row = 1, column=0)
mezo1=Entry(foablak,)
mezo1.grid(row = 1, column=1)
szoveg2=Label(foablak, text="Sugár (cm)")
szoveg2.grid(row = 2, column=0)
mezo2=Entry(foablak,)
mezo2.grid(row = 2, column=1)
szoveg3=Label(foablak, text="Magasság (cm)")
szoveg3.grid(row = 3, column=0)
mezo3=Entry(foablak,)
mezo3.grid(row = 3, column=1)
gomb1=Button(foablak,text="Kiszámít", command = terfogat)
gomb1.grid(row = 4, column = 1,)
szoveg4=Label(foablak, text="Hordó (l)")
szoveg4.grid(row = 5, column=0)
mezo4=Entry(foablak,)
mezo4.grid(row = 5, column=1)
szoveg4=Label(foablak, text="Ha még férne bele:")
szoveg4.grid(row = 6, column=0)
mezo5=Entry(foablak,)
mezo5.grid(row = 6, column=1)
mezo6=Entry(foablak,)
mezo6.grid(row = 6, column=1)
foablak.mainloop()