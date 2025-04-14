from tkinter import Toplevel, Label
from PIL import Image, ImageTk

import matplotlib.pyplot as plt
import base_datos as db
import networkx as nx
import tkinter as tk
import random
import os

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tipwindow = None
        self.widget.bind("<Enter>", self.showtip)
        self.widget.bind("<Leave>", self.hidetip)

    def showtip(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        
        self.tipwindow = Toplevel(self.widget)
        self.tipwindow.wm_overrideredirect(True)
        self.tipwindow.wm_geometry(f"+{x}+{y}")
        
        label = Label(self.tipwindow, text=self.text, justify="left", background="#ffffe0", relief="solid", borderwidth=1, padx=5, pady=5)
        label.pack()

    def hidetip(self, event=None):
        if self.tipwindow:
            self.tipwindow.destroy()
        self.tipwindow = None

def crear_ventana(ancho, alto, tipo_ventana=False, titulo="", fondo_ventana=None):
    if tipo_ventana: 
        ventana = Toplevel()
    else: 
        ventana = tk.Tk()
    
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto  = ventana.winfo_screenheight()
    
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2)  - (alto // 2)
    
    ventana.title(titulo)
    ventana.geometry(f'{ancho}x{alto}+{x}+{y}')
    ventana.resizable(False,False)
    
    if "#" not in fondo_ventana:
        imagen = Image.open(fondo_ventana)
        imagen = imagen.resize((ancho, alto), Image.LANCZOS)
        fondo = ImageTk.PhotoImage(imagen)
        
        fondo_label = tk.Label(ventana, image=fondo)
        fondo_label.image = fondo
        fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
        
    else:
        ventana.configure(bg=fondo_ventana)
    
    return ventana

def actualizar_imagen_aleatorio(ruta = ""):
    if len(ruta) == 0:
        carpeta = 'imgs_app/'
        imagenes = [f for f in os.listdir(carpeta) if f.lower().endswith(('.jpg'))]
        imagen_aleatoria = random.choice(imagenes)
        ruta = carpeta+imagen_aleatoria
        
    img    = Image.open(ruta).resize((250,250))
    img_tk = ImageTk.PhotoImage(img)
    
    return img_tk

def crear_grafo(animal, categoria):
    _ , preguntas = db.obtener_datos(categoria,False,True)
    
    G = nx.DiGraph()
    
    animal = list(animal)
    nombre_animal = animal[1]
    nodos = {"nombre":nombre_animal}
    
    if len(animal) > 0:
        for i in range(4,len(preguntas)+4):
            if animal[i] == 1:
                nodos[preguntas[i-4][2]] = 1
    
    for campo, valor in nodos.items():
        if valor == 1:
            G.add_edge(campo, nodos["nombre"])  # del atributo al nombre del animal
    
    plt.figure(figsize=(8, 6)) #800 x 600
    pos = nx.shell_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=4000, font_size=9, arrows=True)
    plt.title(f"Grafo de características para {nombre_animal}")
    plt.show()