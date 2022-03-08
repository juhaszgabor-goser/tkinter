from tkinter import *
import math
def osszeadas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c= a + b
    mezo3.delete(0, END)
    mezo3.insert(0, str(c))

def szorzas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c= a * b
    mezo3.delete(0, END)
    mezo3.insert(0, str(c))

def osztas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c= (a/b) if b!= 0 else "Nem lehet 0-val osztani"
    mezo3.delete(0, END)
    mezo3.insert(0, str(c))

def kivonas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c= a - b
    mezo3.delete(0, END)
    mezo3.insert(0,str(c))

def negyzetre():
    a = int(mezo1.get())
    c= a*a
    mezo3.delete(0, END)
    mezo3.insert(0, str(c))

def gyokvonas():
    a = int(mezo1.get())
    c= math.sqrt(a) if a > 0 else "nem ertelmezheto"
    mezo3.delete(0, END)
    mezo3.insert(0, str(c))

def hatvanyozas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c= (a**b) if b !=0 else 0
    mezo3.delete(0, END)
    mezo3.insert(0, str(c))

foablak=Tk()
'''
cimke=Label(foablak,text="Udvozlet!", fg="red")
cimke.grid()'''
szoveg3=Label(foablak, text="Vegeredmeny:")
szoveg3.grid(row = 0, column=0)
szoveg1=Label(foablak, text="Elso szam:")
szoveg1.grid(row = 1, column=0)
mezo1=Entry(foablak,)
mezo1.grid(row = 1, column=2)
szoveg2=Label(foablak, text="Masodik szam:")
szoveg2.grid(row = 2, column=0)
mezo2=Entry(foablak)
mezo2.grid(row = 2, column=2)
gomb4=Button(foablak,text="osszeadas", command=osszeadas)
gomb4.grid(row = 3, column = 1)
gomb5=Button(foablak,text="kivonas", command=kivonas)
gomb5.grid(row = 4, column = 1)
gomb6=Button(foablak,text="szorzas", command=szorzas)
gomb6.grid(row = 5, column = 1)
gomb7=Button(foablak,text="osztas", command=osztas)
gomb7.grid(row = 6, column = 1)
'''
gomb8=Button(foablak,text="negyzetre", command=negyzetre)
gomb8.grid(side=RIGHT)
gomb9=Button(foablak,text="gyokvonas", command=gyokvonas)
gomb9.grid(side=RIGHT)
gomb10=Button(foablak,text="hatvanyozas", command=hatvanyozas)
gomb10.grid(side=RIGHT)
'''

can1= Canvas(foablak, width=300, height = 300, bg = "white")
photo = PhotoImage(file="Z9WQLSrsQKH3uBbiXq.gif")
#photo2 = PhotoImage(file="")
item=can1.create_image(120,120, image=photo)
can1.grid(row = 7, column = 1)


mezo3=Entry(foablak,width =25, justify="center")
mezo3.grid( row = 0, column = 1)
gomb3=Button(foablak,text="Kilepes", fg="black", command=foablak.destroy)
gomb3.grid(row = 8, column = 3)



foablak.mainloop()