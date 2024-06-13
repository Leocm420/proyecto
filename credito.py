from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk
# from tkcalendar import Calendar
from tkinter import messagebox
# import dataflight

def data_credit_card():
    window = Tk()
    window.geometry("800x600")
    window.resizable(0, 0)
    window.title("Sky-Voyage")
    window.config(bg="white")  # Removed the green background

    panel = Frame(window, width="700", height="500", bg="white", highlightbackground="black", highlightthickness=3, relief="groove", bd=4)
    panel.place(x=50, y=50)

    frame_credit_card = Frame(panel, bg="white", highlightbackground="black", highlightthickness=2)
    frame_credit_card.place(x=20, y=30, width=315, height=425)

    label_credit_card = Label(frame_credit_card, text="Datos de la tarjeta", font=10, bg="white")
    label_credit_card.place(x=100, y=10)

    frame_name_card = Frame(frame_credit_card, bg="white", highlightbackground="black", highlightthickness=2)
    frame_name_card.place(x=10, y=50, width=295, height=80)

    label_name_card = Label(frame_name_card, text="Nombre del titular", font=10, bg="white")
    label_name_card.place(x=10, y=10)

    entry_name_card = Entry(frame_name_card, font=10, bg="white", justify="center", text="Nombre del titular")
    entry_name_card.place(x=10, y=35, width=275, height=30)

    frame_number_card = Frame(frame_credit_card, bg="white", highlightbackground="black", highlightthickness=2)
    frame_number_card.place(x=10, y=150, width=295, height=80)

    label_number_card = Label(frame_number_card, text="Numero de tarjeta", font=10, bg="white")
    label_number_card.place(x=10, y=10)

    entry_number_card = Entry(frame_number_card, font=10, bg="white", justify="center", text="Nombre del titular")
    entry_number_card.place(x=10, y=35, width=275, height=30)

    frame_date_card = Frame(frame_credit_card, bg="white", highlightbackground="black", highlightthickness=2)
    frame_date_card.place(x=10, y=250, width=295, height=80)

    label_date_card = Label(frame_date_card, text="Fecha de vencimiento", font=10, bg="white")
    label_date_card.place(x=10, y=10)

    label_month_card = Label(frame_date_card, text="Mes", font=10, bg="white")
    label_month_card.place(x=10, y=35)

    entry_month_card = Entry(frame_date_card, font=10, bg="white", justify="center", text="Nombre del titular")
    entry_month_card.place(x=45, y=35, width=50, height=30)

    label_year_card = Label(frame_date_card, text="Año", font=10, bg="white")
    label_year_card.place(x=120, y=35)

    entry_year_card = Entry(frame_date_card, font=10, bg="white", justify="center", text="Nombre del titular")
    entry_year_card.place(x=155, y=35, width=50, height=30)

    frame_cvv_card = Frame(frame_credit_card, bg="white", highlightbackground="black", highlightthickness=2)
    frame_cvv_card.place(x=10, y=350, width=295, height=50)

    label_cvv_card = Label(frame_cvv_card, text="CVV", font=10, bg="white")
    label_cvv_card.place(x=10, y=10)

    entry_cvv_card = Entry(frame_cvv_card, font=10, bg="white", justify="center", text="Nombre del titular")
    entry_cvv_card.place(x=50, y=10, width=50, height=30)

    frame_resume = Frame(panel, bg="white", highlightbackground="black", highlightthickness=2)
    frame_resume.place(x=350, y=30, width=315, height=425)

    label_resume = Label(frame_resume, text="Resumen de la compra", font=10, bg="white")
    label_resume.place(x=100, y=10)

    frame_price = Frame(frame_resume, bg="white", highlightbackground="black", highlightthickness=2)
    frame_price.place(x=10, y=50, width=290, height=250)

    label_price = Label(frame_price, text="Vuelo bog - cali", font=10, bg="white")
    label_price.place(x=10, y=10)

    label_price = Label(frame_price, text="cantidad de personas: ", font=10, bg="white")
    label_price.place(x=10, y=30)

    label_price = Label(frame_price, text="precio: ", font=10, bg="white")
    label_price.place(x=10, y=50)

    label_price = Label(frame_resume, text="total: ", font=10, bg="white")
    label_price.place(x=10, y=350)

    button_buy = Button(frame_resume, text="Comprar", font=10, bg="white", highlightbackground="black", highlightthickness=2)
    button_buy.place(x=220, y=375)

    window.mainloop()

if __name__ == "__main__":
    data_credit_card()