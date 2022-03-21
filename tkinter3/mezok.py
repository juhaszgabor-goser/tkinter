from tkinter import *
foablak=Tk()
kepeleres = 'H:\\IKT\\python\\tkinter3\\'


szoveg1=Label(foablak, text="Elso mezo:")
szoveg1.grid(row = 1, column=0)
mezo1=Entry(foablak,)
mezo1.grid(row = 1, column=2)
szoveg2=Label(foablak, text="Masodik mezo:")
szoveg2.grid(row = 2, column=0)
mezo2=Entry(foablak,)
mezo2.grid(row = 2, column=2)
szoveg3=Label(foablak, text="Harmadik mezo:")
szoveg3.grid(row = 3, column=0)
mezo3=Entry(foablak,)
mezo3.grid(row = 3, column=2)
can1= Canvas(foablak, width=100, height = 100, bg = "white")
photo = PhotoImage(file=kepeleres+"kep1.png")
item=can1.create_image(50,50, image=photo)
can1.grid(row = 2, column = 3)
foablak.mainloop()