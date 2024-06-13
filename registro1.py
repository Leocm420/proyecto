from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style
from PIL import Image, ImageTk

def main():
    window = Tk()
    window.title("Cheik-in App")
    window.geometry("900x500")
    window.config(background="#a2cd5a")
    window.iconbitmap("icono.ico")
    style = Style(theme='flatly')

    #Configuración del estilo
    style.configure('TLabel', background = "#a2cd5a", foreground="black")
    style.configure('TEntry', padding=5)
    style.configure('TCombobox', padding=5)
    style.configure('TButton', padding=5)

    #Crear el encabezado 
    header = ttk.Label(window, text = "Realizar un vuelo", font=("Helvetica", 24), backgroun="#a2cd5a")
    header.grid(row=0, column=0, columnspan=6, pady=20)

    #Creación de los widgets
    genero_label = ttk.Label(window, text="Genero")
    genero_label.grid(row=1,column=0, padx=10, pady=5, sticky=W)
    entrada_genero = ttk.Combobox(window, values=["Masculino", "Femenino", "No definido"])
    entrada_genero.grid(row=1, column=1, padx=10, pady=5, sticky=W)

    primern_label = ttk.Label(window, text="Primer Nombre")
    primern_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
    primern_entry = ttk.Entry(window)
    primern_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

    primer_A_label = ttk.Label(window, text="Primer Apellido")
    primer_A_label.grid(row=1, column=4, padx=10, pady=5, sticky=W)
    primer_A_entry = ttk.Entry(window)
    primer_A_entry.grid(row=1, column=5, padx=10, pady=5, sticky=W)

    identi_label = ttk.Label(window, text="Identificación" )
    identi_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
    identi_entry = ttk.Entry(window)
    identi_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

    natio_label = ttk.Label(window, text="Nacionalidad" )
    natio_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
    natio_entry = ttk.Entry(window)
    natio_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

    seleccionar_vuelo_label = ttk.Button(window, text="Seleccionar vuelo", )
    seleccionar_vuelo_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
    seleccionar_vuelo_entry = ttk.Entry(window)
    seleccionar_vuelo_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

    tel_label = ttk.Label(window, text="Telefono" )
    tel_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
    tel_entry = ttk.Entry(window)
    tel_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

    correo_label = ttk.Label(window, text="Correo Electronico")
    correo_label.grid(row=3, column=4, padx=10, pady=5, sticky=W)
    correo_entry = ttk.Entry(window)
    correo_entry.grid(row=3, column=5, padx=10, pady=5, sticky=W)

    continuar_label = ttk.Button(window, text="Continuar")
    continuar_label.grid(row=4, column=2, padx=30, pady=5, sticky=W)

    window.mainloop()

if __name__ == '__main__':
    main()


