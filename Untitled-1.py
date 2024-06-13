
def leer_fechas_disponibles(origen, destino, archivo='/mnt/data/Datos_Vuelos_Finales.csv'):
    fechas = []
    with open(archivo, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['origen'].lower() == origen.lower() and row['destino'].lower() == destino.lower():
                fechas.append(row['fecha'])
    return fechas

def seleccionar_fecha(origen, destino):
    fechas = leer_fechas_disponibles(origen, destino)
    if not fechas:
        messagebox.showerror("Error", "No hay vuelos disponibles para la ruta seleccionada.")
        return None
    fecha_seleccionada = tk.StringVar(value=fechas[0])
    top = tk.Toplevel(app)
    top.title("Seleccionar Fecha")
    tk.Label(top, text="Seleccione una fecha:").pack(pady=10)
    fecha_combobox = ttk.Combobox(top, textvariable=fecha_seleccionada, values=fechas)
    fecha_combobox.pack(pady=10)
    ttk.Button(top, text="Confirmar", command=top.destroy).pack(pady=10)
    top.wait_window(top)
    return fecha_seleccionada.get()

class AvionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Compra de Boletos")
        self.geometry("300x250")

        global origen_var, destino_var, fecha_var, tipo_viaje_var, cantidad_var
        origen_var = tk.StringVar()
        destino_var = tk.StringVar()
        fecha_var = tk.StringVar()
        tipo_viaje_var = tk.StringVar()
        cantidad_var = tk.StringVar()

        # Supongamos que estas son las ciudades disponibles, deberías ajustarlas según los datos reales
        ciudades = self.obtener_ciudades()

        ttk.Label(self, text="Departamento de Origen:").grid(column=0, row=0, padx=10, pady=10)
        origen_combobox = ttk.Combobox(self, textvariable=origen_var, values=ciudades)
        origen_combobox.grid(column=1, row=0, padx=10, pady=10)

        ttk.Label(self, text="Departamento de Destino:").grid(column=0, row=1, padx=10, pady=10)
        destino_combobox = ttk.Combobox(self, textvariable=destino_var, values=ciudades)
        destino_combobox.grid(column=1, row=1, padx=10, pady=10)

        ttk.Label(self, text="Fecha de Ida:").grid(column=0, row=2, padx=10, pady=10)
        fecha_entry = ttk.Entry(self, textvariable=fecha_var, state='readonly')
        fecha_entry.grid(column=1, row=2, padx=10, pady=10)

        ttk.Label(self, text="Tipo de Viaje:").grid(column=0, row=3, padx=10, pady=10)
        tipo_viaje_combobox = ttk.Combobox(self, textvariable=tipo_viaje_var, values=["Solo Ida", "Ida y Vuelta"])
        tipo_viaje_combobox.grid(column=1, row=3, padx=10, pady=10)
        tipo_viaje_combobox.current(0)

        ttk.Label(self, text="Cantidad de Personas:").grid(column=0, row=4, padx=10, pady=10)
        cantidad_combobox = ttk.Combobox(self, textvariable=cantidad_var, values=[str(i) for i in range(1, 73)])
        cantidad_combobox.grid(column=1, row=4, padx=10, pady=10)

        comprar_button = ttk.Button(self, text="Comprar Boleto", command=realizar_compra)
        comprar_button.grid(column=0, row=5, columnspan=2, padx=10, pady=10)

    def obtener_ciudades(self):
        ciudades = set()
        with open('/mnt/data/Datos_Vuelos_Finales.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                ciudades.add(row['origen'].capitalize())
                ciudades.add(row['destino'].capitalize())
        return list(ciudades)

if __name__ == "__main__":
    app = AvionApp()
    app.mainloop()


import tkinter as tk
from tkinter import ttk, messagebox
import csv

def leer_fechas_disponibles(origen, destino, archivo='Datos_Vuelos_Finales.csv'):
    fechas = []
    with open(archivo, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['origen'].lower() == origen.lower() and row['destino'].lower() == destino.lower():
                fechas.append(row['fecha'])
    return fechas


def seleccionar_fecha(origen, destino):
    fechas = leer_fechas_disponibles(origen, destino)
    if not fechas:
        messagebox.showerror("Error", "No hay vuelos disponibles para la ruta seleccionada.")
        return None
    fecha_seleccionada = tk.StringVar(value=fechas[0])
    top = tk.Toplevel(app)
    top.title("Seleccionar Fecha")
    tk.Label(top, text="Seleccione una fecha:").pack(pady=10)
    fecha_combobox = ttk.Combobox(top, textvariable=fecha_seleccionada, values=fechas)
    fecha_combobox.pack(pady=10)
    ttk.Button(top, text="Confirmar", command=top.destroy).pack(pady=10)
    top.wait_window(top)
    return fecha_seleccionada.get()


def realizar_compra():
    origen = origen_var.get()
    destino = destino_var.get()

    if origen == destino:
        messagebox.showerror("Error", "El origen y destino no pueden ser iguales.")
        return

    fecha_ida = seleccionar_fecha(origen, destino)
    if not fecha_ida:
        return

    tipo_viaje = tipo_viaje_var.get()
    cantidad_personas = int(cantidad_var.get())

    try:
        boleto = comprar_boleto(origen, destino, fecha_ida, tipo_viaje, cantidad_personas)
        asientos = ', '.join(boleto.asientos)
        messagebox.showinfo("Boleto Comprado", f"Origen: {origen}\nDestino: {destino}\nFecha Ida: {fecha_ida}\nTipo de Viaje: {tipo_viaje}\nAsientos asignados: {asientos}")

        # Abrir ventana de selección de asientos
        ventana_seleccion = SeleccionarVentana(app, boleto.asientos)
        ventana_seleccion.grab_set()
    except Exception as e:
        messagebox.showerror("Error", str(e))


class AvionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Compra de Boletos")
        self.geometry("300x250")

        global origen_var, destino_var, fecha_var, tipo_viaje_var, cantidad_var
        origen_var = tk.StringVar()
        destino_var = tk.StringVar()
        fecha_var = tk.StringVar()
        tipo_viaje_var = tk.StringVar()
        cantidad_var = tk.StringVar()

        ciudades = self.obtener_ciudades()

        ttk.Label(self, text="Departamento de Origen:").grid(column=0, row=0, padx=10, pady=10)
        origen_combobox = ttk.Combobox(self, textvariable=origen_var, values=ciudades)
        origen_combobox.grid(column=1, row=0, padx=10, pady=10)

        ttk.Label(self, text="Departamento de Destino:").grid(column=0, row=1, padx=10, pady=10)
        destino_combobox = ttk.Combobox(self, textvariable=destino_var, values=ciudades)
        destino_combobox.grid(column=1, row=1, padx=10, pady=10)

        ttk.Label(self, text="Fecha de Ida:").grid(column=0, row=2, padx=10, pady=10)
        fecha_entry = ttk.Entry(self, textvariable=fecha_var, state='readonly')
        fecha_entry.grid(column=1, row=2, padx=10, pady=10)

        ttk.Label(self, text="Tipo de Viaje:").grid(column=0, row=3, padx=10, pady=10)
        tipo_viaje_combobox = ttk.Combobox(self, textvariable=tipo_viaje_var, values=["Solo Ida", "Ida y Vuelta"])
        tipo_viaje_combobox.grid(column=1, row=3, padx=10, pady=10)
        tipo_viaje_combobox.current(0)

        ttk.Label(self, text="Cantidad de Personas:").grid(column=0, row=4, padx=10, pady=10)
        cantidad_combobox = ttk.Combobox(self, textvariable=cantidad_var, values=[str(i) for i in range(1, 73)])
        cantidad_combobox.grid(column=1, row=4, padx=10, pady=10)

        comprar_button = ttk.Button(self, text="Comprar Boleto", command=realizar_compra)
        comprar_button.grid(column=0, row=5, columnspan=2, padx=10, pady=10)

    def obtener_ciudades(self):
        ciudades = set()
        with open('Datos_Vuelos_Finales.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                ciudades.add(row['origen'].capitalize())
                ciudades.add(row['destino'].capitalize())
        return list(ciudades)
