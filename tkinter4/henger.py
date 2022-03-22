from tkinter import *
import math
def terfogat():
    a = float(mezo1.get())
    b = float(mezo2.get())
    c= math.pi*pow(a,2)*b
    mezo3.delete(0, END)
    mezo3.insert(0,str(c))
def vashenger():
    a = float(mezo1.get())
    b = float(mezo2.get())
'''    c= (math.sqrt(a)*math.pi*b)'''
    c = math.pi*b*pow(a,2)
    d = math.pi*
    mezo4.delete(0, END)
    mezo4.insert(0,str(c))
def fahenger():
    a = float(mezo1.get())
    b = float(mezo2.get())
    c= math.pi*pow(a,2)*b
    mezo5.delete(0, END)
    mezo5.insert(0,str(c))


foablak = Tk()

szoveg1=Label(foablak, text="Sugár (cm):")
szoveg1.grid(row = 1, column=0)
mezo1=Entry(foablak,)
mezo1.grid(row = 1, column=1)
szoveg2=Label(foablak, text="Magasság (cm):")
szoveg2.grid(row = 2, column=0)
mezo2=Entry(foablak,)
mezo2.grid(row = 2, column = 1)
gomb4=Button(foablak,text="terfogat", command=tlambda:[terfogat(), vashenger(), fahenger()]))
gomb4.grid(row = 3, column = 1)
szoveg3=Label(foablak,text="Térfogat:")
szoveg3.grid(row = 4, column = 0)
mezo3=Entry(foablak,)
mezo3.grid(row= 4,column = 1)
szoveg4=Label(foablak,text="Vashenger:")
szoveg4.grid(row = 5, column = 0)
mezo4=Entry(foablak,)
mezo4.grid(row= 5,column = 1)
szoveg5=Label(foablak,text="Fahenger:")
szoveg5.grid(row = 6, column = 0)
mezo5=Entry(foablak,)
mezo5.grid(row= 6,column = 1)
foablak.mainloop()