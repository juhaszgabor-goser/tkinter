from tkinter import *

abl1 = Tk()
abl1.title("A téglatest adatai")
abl1.minsize(width = 300,height = 100)
def ujablak():
    abl2 = Toplevel(abl1)
    abl2.title("Eredmények")
    abl2.minsize(width = 300, height = 300)

    uz1 = Label(abl2,text ="Felszín:")
    uz2 = Label(abl2,text ="Térfogat:")
    m1 = Entry(abl2)
    m2 = Entry(abl2)
    uz1.grid(row = 1)
    uz2.grid(row = 2)
    m1.grid( row = 1, column = 2)
    m2.grid(row = 2, column = 2)

    a = eval(hely1.get())
    b = eval(hely2.get())
    c = eval(hely3.get())

    felszin = 2*(a*b+a*c+b*c)
    terfogat = a*b*c

    m1.delete(0,END)
    m1.insert(0,str(felszin))
    m2.delete(0,END)
    m2.insert(0,str(terfogat))

    gomb2 = Button(abl2, text = "Kilépés", command=abl2.destroy)
    gomb2.grid(row = 3, column = 1)
    abl2.mainloop()
szoveg1 = Label(abl1, text = "a:")
szoveg2 = Label(abl1, text = "b:")
szoveg3 = Label(abl1, text = "b:")
hely1 = Entry()
hely2 = Entry()
hely3 = Entry()
szoveg1.grid(row = 1)
szoveg2.grid(row = 2)
szoveg3.grid(row = 3)
hely1.grid(row = 1, column = 2)
hely2.grid(row = 2, column = 2)
hely3.grid(row = 3, column = 2)
gomb1 = Button(abl1, text = "számítás", command=ujablak)
gomb1.grid(row = 4, column = 2)
abl1.mainloop()