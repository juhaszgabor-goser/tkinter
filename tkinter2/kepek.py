from tkinter import *
ablak1 = Tk()
gyoker = 'H:\\IKT\\python\\tkinter2\\'
ablak1.geometry('450x450')
ablak1.title("IKT Tkinter")
icon = PhotoImage(file = gyoker+"img_507427.png")
kep = PhotoImage(file = gyoker+"kep2.png")
ablak1.iconphoto(True, icon)
ablak1.config(bg = 'black')

cimke = Label(ablak1,text="Üdvözlet!",
                    fg="#000000",
                    bg = "white",
                    font=("Arial", 45, "bold"),
                    bd = 10,
                    relief = RAISED,
                    padx = 25,
                    pady = 25,
                    image = kep,
                    compound = "center").pack()


ablak1.mainloop()