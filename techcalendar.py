import tkinter as tk

class Calendar:
    def __init__(self, master):
        self.master = master
        self.master.title("Calendario de soporte técnico")
        
        # Creamos una variable para almacenar las citas
        self.citas = []
        
        # Creamos los elementos de la interfaz
        self.crear_interfaz()
        
    def crear_interfaz(self):
        # Creamos un botón para agregar citas
        agregar_btn = tk.Button(self.master, text="Agregar cita", command=self.agregar_cita)
        agregar_btn.pack(pady=10)
        
        # Creamos un marco para mostrar las citas
        citas_frame = tk.Frame(self.master)
        citas_frame.pack()
        
        # Creamos una etiqueta para mostrar las citas
        self.citas_lbl = tk.Label(citas_frame, text="No hay citas")
        self.citas_lbl.pack()
        
    def agregar_cita(self):
        # Creamos una ventana emergente para agregar una cita
        agregar_window = tk.Toplevel(self.master)
        agregar_window.title("Agregar cita")
        
        # Creamos los elementos de la ventana emergente
        tk.Label(agregar_window, text="Cliente:").grid(row=0, column=0, padx=10, pady=10)
        cliente_entry = tk.Entry(agregar_window)
        cliente_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(agregar_window, text="Fecha:").grid(row=1, column=0, padx=10, pady=10)
        fecha_entry = tk.Entry(agregar_window)
        fecha_entry.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(agregar_window, text="Hora:").grid(row=2, column=0, padx=10, pady=10)
        hora_entry = tk.Entry(agregar_window)
        hora_entry.grid(row=2, column=1, padx=10, pady=10)
        
        agregar_btn = tk.Button(agregar_window, text="Agregar", command=lambda: self.guardar_cita(cliente_entry.get(), fecha_entry.get(), hora_entry.get(), agregar_window))
        agregar_btn.grid(row=3, column=1, padx=10, pady=10)
        
    def guardar_cita(self, cliente, fecha, hora, agregar_window):
        # Guardamos la cita en la lista de citas
        self.citas.append({"cliente": cliente, "fecha": fecha, "hora": hora})
        
        # Cerramos la ventana emergente
        agregar_window.destroy()
        
        # Actualizamos la etiqueta de citas
        self.actualizar_citas_lbl()
        
    def actualizar_citas_lbl(self):
        # Actualizamos la etiqueta de citas con las citas guardadas
        if len(self.citas) == 0:
            self.citas_lbl.configure(text="No hay citas")
        else:
            citas_text = ""
            for cita in self.citas:
                citas_text += f"{cita['cliente']}: {cita['fecha']} a las {cita['hora']}\n"
            self.citas_lbl.configure(text=citas_text)
        
root = tk.Tk()
calendario = Calendar(root)
root.mainloop()
