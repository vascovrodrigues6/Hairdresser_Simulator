from tkinter import *
from tkinter import messagebox


#Another execution? Volta ao primeiro ecrã
import UI


def Report(reports):
    app = Tk()

    app.title("Reports")
    app.geometry('400x270')
    app.resizable(width=False, height=False)
    lbl1 = Label(app, text="Washing queue delay:", font=("Arial Bold", 10))
    lbl2 = Label(app, text="Hairdressing queue delay:", font=("Arial Bold", 10))
    lbl3 = Label(app, text="Payment queue delay:", font=("Arial Bold", 10))
    lbl4 = Label(app, text="Average number in washing queue:", font=("Arial Bold", 10))
    lbl5 = Label(app, text="Average number in hairdressing queue:", font=("Arial Bold", 10))
    lbl6 = Label(app, text="Average number in payment queue:", font=("Arial Bold", 10))
    lbl7 = Label(app, text="Washing server utilization:", font=("Arial Bold", 10))
    lbl8 = Label(app, text="Hairdressing server utilization:", font=("Arial Bold", 10))
    lbl9 = Label(app, text="Payment server utilization:", font=("Arial Bold", 10))
    lbl10 = Label(app, text="Simulation ended in:", font=("Arial Bold", 10))

    lbl11 = Label(app, text=round(reports["average_delay_queue_washing"],2), font=("Arial Bold", 10))
    lbl12 = Label(app, text=round(reports["average_delay_queue_hairdressing"],2), font=("Arial Bold", 10))
    lbl13 = Label(app, text=round(reports["average_delay_queue_payment"],2), font=("Arial Bold", 10))
    lbl14 = Label(app, text=round(reports["average_num_in_queue_washing"],2), font=("Arial Bold", 10))
    lbl15 = Label(app, text=round(reports["average_num_in_queue_hairdressing"],2), font=("Arial Bold", 10))
    lbl16 = Label(app, text=round(reports["average_num_in_queue_payment"],2), font=("Arial Bold", 10))
    lbl17 = Label(app, text=str(round(reports["washing_server_utilization"]*100,1))+"%", font=("Arial Bold", 10))
    lbl18 = Label(app, text=str(round(reports["hairdressing_server_utilization"]*100,1))+"%", font=("Arial Bold", 10))
    lbl19 = Label(app, text=str(round(reports["payment_server_utilization"]*100,1))+"%", font=("Arial Bold", 10))
    lbl20 = Label(app, text=round(reports["time_simulation_ended"],2), font=("Arial Bold", 10))

    lbl1.grid(column=0, row=0, sticky="w")
    lbl11.grid(column=1, row=0, sticky="w")
    lbl2.grid(column=0, row=1, sticky="w")
    lbl12.grid(column=1, row=1, sticky="w")
    lbl3.grid(column=0, row=2, sticky="w")
    lbl13.grid(column=1, row=2, sticky="w")
    lbl4.grid(column=0, row=3, sticky="w")
    lbl14.grid(column=1, row=3, sticky="w")
    lbl5.grid(column=0, row=4, sticky="w")
    lbl15.grid(column=1, row=4, sticky="w")
    lbl6.grid(column=0, row=5, sticky="w")
    lbl16.grid(column=1, row=5, sticky="w")
    lbl7.grid(column=0, row=6, sticky="w")
    lbl17.grid(column=1, row=6, sticky="w")
    lbl8.grid(column=0, row=7, sticky="w")
    lbl18.grid(column=1, row=7, sticky="w")
    lbl9.grid(column=0, row=8, sticky="w")
    lbl19.grid(column=1, row=8, sticky="w")
    lbl10.grid(column=0, row=9, sticky="w")
    lbl20.grid(column=1, row=9, sticky="w")

    #app.destroy()
    #messagebox.showinfo('Report', reports)

    def clicked():
        app.destroy()
        UI.Ui()

    def clickedRepeat():
        app.destroy()
        UI.Ui()


    button3 = Button(app, text="Re-run simulation", bg="white", fg="red", command=clicked, height=1, width=15).place(x=3, y=230)
    #button4 = Button(app, text="Run 10x with same configuration", bg="white", fg="red", command=clickedRepeat, height=1, width=30).place(x=180, y=230)