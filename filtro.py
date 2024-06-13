from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style
from PIL import Image, ImageTk

def mostrar_detalle_vuelo():
    detalle_window = Toplevel()
    detalle_window.title("Detalle del Vuelo")
    detalle_window.geometry("600x400")
    detalle_window.config(background="#ffffff")

    # Encabezado
    header_frame = Frame(detalle_window, bg="#a2cd5a", height=50)
    header_frame.pack(fill=X)
    header_label = Label(header_frame, text="Sky-Voyage", bg="#a2cd5a", fg="white", font=("Helvetica", 18))
    header_label.pack(pady=10)

    # Información de vuelo
    info_frame = Frame(detalle_window, bg="white")
    info_frame.pack(fill=X, padx=20, pady=10)

    vuelo_label = Label(info_frame, text="Ida: Bogotá a Cartagena", bg="white", font=("Helvetica", 16))
    vuelo_label.pack(side=LEFT, padx=10, pady=10)

    # Detalle del vuelo
    detalle_frame = Frame(detalle_window, bg="white")
    detalle_frame.pack(fill=X, padx=20, pady=10)

    hora_salida_label = Label(detalle_frame, text="07:05\nBOG", bg="white", font=("Helvetica", 14))
    hora_salida_label.pack(side=LEFT, padx=10, pady=10)

    tipo_vuelo_label = Label(detalle_frame, text="------------------------\n6h 20m", bg="white", font=("Helvetica", 14))
    tipo_vuelo_label.pack(side=LEFT, padx=10, pady=10)

    hora_llegada_label = Label(detalle_frame, text="14:25\nCAR", bg="white", font=("Helvetica", 14))
    hora_llegada_label.pack(side=LEFT, padx=10, pady=10)

    precio_label = Label(detalle_frame, text="Desde\nCOP 2.290.075", bg="white", font=("Helvetica", 14))
    precio_label.pack(side=RIGHT, padx=10, pady=10)

    # Botón de selección
    seleccionar_frame = Frame(detalle_window, bg="white")
    seleccionar_frame.pack(fill=X, padx=20, pady=10)

    total_label = Label(seleccionar_frame, text="Total de la reserva\nCOP 2.290.075", bg="white", font=("Helvetica", 14))
    total_label.pack(side=LEFT, padx=10, pady=10)

    seleccionar_button = Button(seleccionar_frame, text="Seleccionar", bg="#a2cd5a", fg="white", font=("Helvetica", 14))
    seleccionar_button.pack(side=RIGHT, padx=10, pady=10)

def main():
    window = Tk()
    window.title("Sky-Voyage")
    window.geometry("1000x700")
    window.config(background="#ffffff")
    style = Style(theme='flatly')

    # Encabezado
    header_frame = Frame(window, bg="#a2cd5a", height=50)
    header_frame.pack(fill=X)
    header_label = Label(header_frame, text="Sky-Voyage", bg="#a2cd5a", fg="white", font=("Helvetica", 18))
    header_label.pack(pady=10)

    # Información de vuelo
    info_frame = Frame(window, bg="white")
    info_frame.pack(fill=X, padx=20, pady=10)

    vuelo_label = Label(info_frame, text="Ida: Bogotá a Cartagena", bg="white", font=("Helvetica", 16))
    vuelo_label.pack(side=LEFT, padx=10, pady=10)

    # Ordenar por
    ordenar_frame = Frame(window, bg="white")
    ordenar_frame.pack(fill=X, padx=20, pady=10)

    ordenar_label = Label(ordenar_frame, text="Ordenar por:", bg="white")
    ordenar_label.pack(side=LEFT, padx=10, pady=5)

    ordenar_combobox = ttk.Combobox(ordenar_frame, values=["Mejor precio", "Vuelos directos"])
    ordenar_combobox.pack(side=LEFT, padx=10, pady=5)
    ordenar_combobox.set("Mejor precio")

    # Información de vuelo detalle
    vuelo_detalle_frame = Frame(window, bg="white")
    vuelo_detalle_frame.pack(fill=X, padx=20, pady=10)

    hora_salida_label = Label(vuelo_detalle_frame, text="07:05\nBOG", bg="white", font=("Helvetica", 14))
    hora_salida_label.pack(side=LEFT, padx=10, pady=10)

    tipo_vuelo_label = Label(vuelo_detalle_frame, text="------------------------\n6h 20m", bg="white", font=("Helvetica", 14))
    tipo_vuelo_label.pack(side=LEFT, padx=10, pady=10)

    hora_llegada_label = Label(vuelo_detalle_frame, text="14:25\nCAR", bg="white", font=("Helvetica", 14))
    hora_llegada_label.pack(side=LEFT, padx=10, pady=10)

    precio_label = Label(vuelo_detalle_frame, text="Desde\nCOP 2.290.075", bg="white", font=("Helvetica", 14))
    precio_label.pack(side=RIGHT, padx=10, pady=10)

    # Opciones de tarifas
    tarifas_frame = Frame(window, bg="white")
    tarifas_frame.pack(fill=X, padx=20, pady=10)

    tarifas = [("Basic", "COP 779.975", ["1 artículo personal (bolso)", "Equipaje de mano (10 kg)", "Equipaje de bodega (23 kg)", "Reserva (no permitida)"]),
               ("Element", "COP 1.194.425", ["1 artículo personal (bolso)", "Equipaje de mano (10 kg)", "Asiento Económico (incluido)", "Reserva (no permitida)"]),
               ("Premium", "COP 2.296.925", ["1 artículo personal (bolso)", "Equipaje de mano (10 kg)", "Asiento Premium (incluido)", "Reserva (permitida)"])]

    for nombre, precio, detalles in tarifas:
        tarifa_frame = Frame(tarifas_frame, bg="#a2cd5a", borderwidth=1, relief="solid", width=25)
        tarifa_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

        nombre_label = Label(tarifa_frame, text=nombre, bg="#a2cd5a", font=("Helvetica", 14), fg="white")
        nombre_label.pack(padx=10, pady=10)

        precio_label = Label(tarifa_frame, text=precio, bg="#a2cd5a", font=("Helvetica", 12), fg="white")
        precio_label.pack(padx=10, pady=5)

        for detalle in detalles:
            detalle_label = Label(tarifa_frame, text=detalle, bg="#a2cd5a", fg="white")
            detalle_label.pack(padx=10, pady=2)

        seleccionar_button = Button(tarifa_frame, text="Seleccionar", bg="white", fg="#a2cd5a", command=mostrar_detalle_vuelo)
        seleccionar_button.pack(pady=10)

    window.mainloop()

if __name__ == '__main__':
    main()
