


import customtkinter as ctk
from tkinter import ttk
from grafo import grafo
from busqueda_uniforme import BusquedaUniforme
from coordenadas import coordenadas
from utils import calcular_costo
from tkinter import messagebox

class InterfazBusqueda:
    def __init__(self, master):
        self.master = master
        self.master.title("Búsqueda Uniforme en el Mapa de Rumania")

        ciudades = list(grafo.keys())
        self.ciudad_inicio = ctk.StringVar(value="Arad")
        self.ciudad_objetivo = ctk.StringVar(value="Bucharest")

        self.canvas = ctk.CTkCanvas(master, width=600, height=300, bg="#e5e5e5", highlightthickness=0)
        self.canvas.grid(row=0, column=0)

        style = ttk.Style()
        style.theme_use("default") 
        style.configure("Treeview",
                        background="#2b2b2b",
                        foreground="white",
                        fieldbackground="#2b2b2b",
                        font=("Arial", 10))
        style.configure("Treeview.Heading",
                        background="#1f1f1f",
                        foreground="white",
                        font=("Arial", 10, "bold"))


        self.tabla = ttk.Treeview(master, columns=("Paso", "Ciudad", "Costo"), show="headings", height=15)
        self.tabla.heading("Paso", text="Paso")
        self.tabla.heading("Ciudad", text="Ciudad")
        self.tabla.heading("Costo", text="Costo acumulado")
        self.tabla.column("Paso", width=50, anchor="center")
        self.tabla.column("Ciudad", width=500, anchor="center")
        self.tabla.column("Costo", width=100, anchor="center")
        self.tabla.grid(row=0, column=1, sticky="ns")

        controles = ctk.CTkFrame(master)
        controles.grid(row=1, column=0, columnspan=2, pady=10)

        ctk.CTkLabel(controles, text="Inicio:").pack(side="left")
        self.entrada_inicio = ctk.CTkComboBox(controles, values=ciudades, variable=self.ciudad_inicio, width=140)
        self.entrada_inicio.pack(side="left")

        ctk.CTkLabel(controles, text="Objetivo:").pack(side="left")
        self.entrada_destino = ctk.CTkComboBox(controles, values=ciudades, variable=self.ciudad_objetivo, width=140)
        self.entrada_destino.pack(side="left")

        self.boton_iniciar = ctk.CTkButton(controles, text="Iniciar búsqueda", command=self.iniciar_busqueda, state="disabled")
        self.boton_iniciar.pack(side="left")

        ctk.CTkButton(controles, text="Siguiente paso", command=self.siguiente_paso).pack(side="left")
        ctk.CTkButton(controles, text="Ver archivo de ruta", command=self.mostrar_archivo_ruta).pack(side="left")

        self.ciudad_inicio.trace_add("write", self.verificar_entradas)
        self.ciudad_objetivo.trace_add("write", self.verificar_entradas)

        self.pasos = []
        self.paso_actual = 0

        self.dibujar_mapa()

    def verificar_entradas(self, *args):
        if self.ciudad_inicio.get() and self.ciudad_objetivo.get():
            self.boton_iniciar.configure(state="normal")
        else:
            self.boton_iniciar.configure(state="disabled")

    def dibujar_mapa(self):
        self.canvas.delete("all")
        for origen, adyacentes in grafo.items():
            for destino, _ in adyacentes:
                if destino in coordenadas and origen in coordenadas:
                    x1, y1 = coordenadas[origen]
                    x2, y2 = coordenadas[destino]
                    self.canvas.create_line(x1, y1, x2, y2, fill="lightgray")

        for ciudad, (x, y) in coordenadas.items():
            self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="skyblue")
            self.canvas.create_text(x, y-10, text=ciudad, font=("Arial", 8))

    def iniciar_busqueda(self):
        inicio = self.ciudad_inicio.get()
        objetivo = self.ciudad_objetivo.get()
        buscador = BusquedaUniforme(grafo)
        camino, costo = buscador.buscar(inicio, objetivo)

        self.tabla.delete(*self.tabla.get_children())
        self.dibujar_mapa()
        self.paso_actual = 0

        if camino:
            self.pasos = [
                (camino[:i+1], calcular_costo(camino[:i+1]))
                for i in range(len(camino))
            ]
            self.mostrar_paso()

    def siguiente_paso(self):
        if self.paso_actual < len(self.pasos):
            self.mostrar_paso()
            self.paso_actual += 1

    def mostrar_paso(self):
        if self.paso_actual >= len(self.pasos):
            return

        camino, costo = self.pasos[self.paso_actual]
        self.tabla.insert("", "end", values=(self.paso_actual+1, " → ".join(camino), costo))

        self.dibujar_mapa()
        for i in range(len(camino)-1):
            c1, c2 = camino[i], camino[i+1]
            if c1 in coordenadas and c2 in coordenadas:
                x1, y1 = coordenadas[c1]
                x2, y2 = coordenadas[c2]
                self.canvas.create_line(x1, y1, x2, y2, fill="red", width=2)
    
    def mostrar_archivo_ruta(self):
        try:
            with open("salida_busqueda_uniforme.txt", "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
            # Ventana emergente para mostrar el contenido del archivo
            ventana = ctk.CTkToplevel(self.master)
            ventana.title("Contenido de ruta.txt")
            ventana.geometry("800x500")

            text_area = ctk.CTkTextbox(ventana, wrap="word", width=760, height=460, corner_radius=10)
            text_area.insert("0.0", contenido)
            text_area.configure(state="disabled")  # Solo lectura
            text_area.pack(padx=20, pady=20)

        except FileNotFoundError:
            messagebox.showerror("Archivo no encontrado", "No se encontró el archivo 'salida_busqueda_uniforme.txt'.")












