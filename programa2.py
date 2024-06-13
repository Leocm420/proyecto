import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import random

class Vuelo:
    def __init__(self, origen, destino, fecha_ida):
        self.origen = origen
        self.destino = destino
        self.fecha_ida = fecha_ida
        self.asientos = self.generar_asientos()
        self.asientos_disponibles = list(self.asientos.keys())

    def generar_asientos(self):
        sectores = 'ABCDEF'
        asientos = {}
        for sector in sectores:
            for i in range(1, 13):
                asientos[f"{sector}{i}"] = None
        return asientos

    def asignar_asiento(self):
        if not self.asientos_disponibles:
            raise Exception("No hay asientos disponibles.")
        asiento = random.choice(self.asientos_disponibles)
        self.asientos_disponibles.remove(asiento)
        return asiento

class Boleto:
    def __init__(self, vuelo, cantidad_personas):
        self.vuelo = vuelo
        self.cantidad_personas = cantidad_personas
        self.asientos = self.asignar_asientos()

    def asignar_asientos(self):
        asientos_asignados = []
        for _ in range(self.cantidad_personas):
            asiento = self.vuelo.asignar_asiento()
            asientos_asignados.append(asiento)
        return asientos_asignados

def comprar_boleto(origen, destino, fecha_ida, tipo_viaje, cantidad_personas):
    vuelo = Vuelo(origen, destino, fecha_ida)
    boleto = Boleto(vuelo, cantidad_personas)
    if tipo_viaje == "Ida y Vuelta":
        vuelta = Vuelo(destino, origen, fecha_ida)
        boleto_vuelta = Boleto(vuelta, cantidad_personas)
        boleto.asientos.extend(boleto_vuelta.asientos)
    return boleto

def realizar_compra():
    origen = origen_var.get()
    destino = destino_var.get()
    fecha_ida = fecha_var.get()
    tipo_viaje = tipo_viaje_var.get()
    cantidad_personas = int(cantidad_var.get())

    if origen == destino:
        messagebox.showerror("Error", "El origen y destino no pueden ser iguales.")
        return

    try:
        boleto = comprar_boleto(origen, destino, fecha_ida, tipo_viaje, cantidad_personas)
        asientos = ', '.join(boleto.asientos)
        messagebox.showinfo("Boleto Comprado", f"Origen: {origen}\nDestino: {destino}\nFecha Ida: {fecha_ida}\nTipo de Viaje: {tipo_viaje}\nAsientos asignados: {asientos}")
        
        # Abrir ventana de selección de asientos
        ventana_seleccion = SeleccionarVentana(app, boleto.asientos)
        ventana_seleccion.grab_set()
    except Exception as e:
        messagebox.showerror("Error", str(e))

class SeleccionarVentana(tk.Toplevel):
    def __init__(self, parent, asientos_asignados):
        super().__init__(parent)
        self.title("Seleccionar Asientos")
        self.geometry("550x650")
        
        # Sectores y colores
        self.sectores = ["Oro", "Plata", "Bronce"]
        self.sector_colors = {"Oro": "gold", "Plata": "silver", "Bronce": "brown"}
        self.asientos = {}
        
        # Crear grilla de asientos
        self.crear_asientos(asientos_asignados)

    def crear_asientos(self, asientos_asignados):
        sector_assignment = ["Oro"] * 24 + ["Plata"] * 24 + ["Bronce"] * 24

        for fila in range(12):
            for columna in range(7): 
                if columna == 3: 
                    label = tk.Label(self, text=" ", width=5, height=2, bg="gray")
                    label.grid(row=fila, column=columna, padx=5, pady=5)
                else:
                    if columna < 3:
                        letra = chr(65 + columna)
                    else:
                        letra = chr(65 + columna - 1)

                    numero = fila + 1
                    asiento_id = f"{letra}{numero}"
                    sector = sector_assignment.pop(0)
                    
                    bg_color = "red" if asiento_id in asientos_asignados else self.sector_colors[sector]
                    estado_asiento = "X" if asiento_id in asientos_asignados else asiento_id
                    btn = tk.Button(self, text=estado_asiento, width=5, height=2, 
                                    bg=bg_color,
                                    state=tk.DISABLED if asiento_id in asientos_asignados else tk.NORMAL)
                    btn.grid(row=fila, column=columna, padx=5, pady=5)
                    
                    self.asientos[asiento_id] = {
                        "button": btn,
                        "ocupado": asiento_id in asientos_asignados,
                        "sector": sector
                    }

        for i, sector in enumerate(self.sectores):
            etiqueta = tk.Label(self, text=sector, font=("Arial", 12, "bold"), bg=self.sector_colors[sector])
            etiqueta.grid(row=12, column=i*2, columnspan=2, pady=10, padx=5)

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

        paises = ["BOGOTÁ","CALI","CARTAGENA","MEDELLIN","SANTA MARTA"]

        ttk.Label(self, text="Departamento de Origen:").grid(column=0, row=0, padx=10, pady=10)
        origen_combobox = ttk.Combobox(self, textvariable=origen_var, values=paises)
        origen_combobox.grid(column=1, row=0, padx=10, pady=10)

        ttk.Label(self, text="Departamento de Destino:").grid(column=0, row=1, padx=10, pady=10)
        destino_combobox = ttk.Combobox(self, textvariable=destino_var, values=paises)
        destino_combobox.grid(column=1, row=1, padx=10, pady=10)

        ttk.Label(self, text="Fecha de Ida:").grid(column=0, row=2, padx=10, pady=10)
        fecha_entry = DateEntry(self, textvariable=fecha_var, date_pattern='yyyy-mm-dd')
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

if __name__ == "__main__":
    app = AvionApp()
    app.mainloop()
