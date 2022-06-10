from tkinter import *
from tkinter import messagebox

from main import main


def Ui():
    app = Tk()
    app.title("Hair saloon simulator")
    app.geometry('300x110')
    app.resizable(width=False, height=False)
    lbl = Label(app, text="Number of Customers:", font=("Arial Bold", 10))
    lbl2 = Label(app, text="Number of Hairdressers:", font=("Arial Bold", 10))
    lbl3 = Label(app, text="Number of Secondary Hairdressers:", font=("Arial Bold", 10))
    lbl.grid(column=0, row=0)
    lbl2.grid(column=0, row=1)
    lbl3.grid(column=0, row=2)
    txt = Entry(app, width=10)
    txt.grid(column=1, row=0)
    txt2 = Entry(app, width=10)
    txt2.grid(column=1, row=1)
    txt3 = Entry(app, width=10)
    txt3.grid(column=1, row=2)

    def clicked():
            customers = int(txt.get())
            hairdressers = int(txt2.get())
            secondaryHairdressers = int(txt3.get())
            messagebox.showinfo('Hair saloon simulator', 'Simulation complete')
            app.destroy()
            main(customers,hairdressers,secondaryHairdressers)

    button3 = Button(app, text="Run Simulation", bg="white", fg="red", command=clicked, height=1, width=12).place(x=100, y =70)

    app.mainloop()
