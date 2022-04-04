from tkinter import *
import math
def szamolas():
    liter = float(mezo1.get())
    sugar = float(mezo2.get())
    magassag = float(mezo3.get())
    V= round (math.pi*pow(liter,2)*sugar)
    valami  = round (V*0.001)
    valami2 = round(m*(100/valami), 2)
    mezo4.delete(0, END)
    mezo4.insert(0,+float(magassag))
    if valami > magassag:
        belefer = True
    else: 
        belefer = False
    if belefer:
        mezo5.delete(0,END)
        mezo5.insert(0,"Belefér")
    else:
        mezo5.delete(0,END)
        mezo5.insert(0,"Nem fér bele")
    if belefer:
        szamolas = magassag/V
        mezo6.delete(0,END)
        mezo6.insert(0,+int(valami))
    if liter and sugar and magassag <=0:
        mezo4.delete(0,END)
        mezo5.delete(0,END)
        mezo6.delete(0,END)
        mezo4.insert(0,"Nem jo")
        mezo5.insert(0,"Nem jo")
        mezo6.insert(0,"nem jo")
foablak = Tk()
eleres = 'H:\\IKT\\python\\tkinter5\\'
foablak.title("Henger folyadék")
icon = PhotoImage(file = eleres+"hordo.png",)
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

gomb1=Button(foablak,text="Kiszámít", command = szamolas)
gomb1.grid(row = 4, column = 1,)

szoveg4=Label(foablak, text="Hordó (l)")
szoveg4.grid(row = 5, column=0)
mezo4=Entry(foablak,)
mezo4.grid(row = 5, column=1)

szoveg5=Label(foablak, text="Ha még férne bele:")
szoveg5.grid(row = 6, column=0)
mezo5=Entry(foablak,)
mezo5.grid(row = 6, column=1)

szoveg6=Label(foablak, text="%")
szoveg6.grid(row = 7, column=0)
mezo6=Entry(foablak,)
mezo6.grid(row = 7, column=1)

can1= Canvas(foablak, width=100, height = 100, bg = "white")
photo = PhotoImage(file=eleres+"hordo.png")
item=can1.create_image(50,50,image=photo)
can1.grid(row = 4, column = 2)
foablak.mainloop()