from tkinter import *
ablak1 = Tk()
gyoker = 'H:\\IKT\\python\\tkinter2\\'
ablak1.geometry('450x450')
ablak1.title("IKT Tkinter")
icon = PhotoImage(file = gyoker+"img_507427.png",)
kep = PhotoImage(file = gyoker+"kep2.png", width = "300", height = "300")
kep2 = PhotoImage(file = gyoker+"kep2.png", width = "20", height = "20")
ablak1.iconphoto(True, icon)
ablak1.config(bg = 'black')
def klikk():
    print("Klikkeltem")

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

gomb = Button(ablak1,
            text = "Kattints",
            fg = "blue",
            font =("Comic Sans", 35, "bold"),
            bg = "yellow",
            relief = SUNKEN,
            bd = 10,
            command = klikk,
            padx = 12,
            pady = 12,
            image =kep2,
            compound = "bottom",
            activebackground = "blue",
            activeforeground="yellow",
            state = ACTIVE).pack()

ablak1.mainloop()
