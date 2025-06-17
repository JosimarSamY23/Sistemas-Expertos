import tkinter as tk
import requests

from tkinter import ttk
from PIL import Image, ImageTk
from datasets import load_dataset
from os import system
from io import BytesIO

# --- Configuración global ---
config = {
    "Ancho": 520,
    "Alto" : 760,
}

# --- Función para crear ventana con fondo ---
def crear_ventana(titulo, fondo_path):
    ventana = tk.Tk()
    ancho, alto = config["Ancho"], config["Alto"]
    sw, sh = ventana.winfo_screenwidth(), ventana.winfo_screenheight()
    x, y = (sw-ancho)//2, (sh-alto)//2
    
    ventana.title(titulo)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
    ventana.resizable(False, False)
    
    img = Image.open(fondo_path).resize((ancho, alto), Image.LANCZOS)
    bg = ImageTk.PhotoImage(img)
    lbl = tk.Label(ventana, image=bg)
    lbl.image = bg
    lbl.place(x=0, y=0, relwidth=1, relheight=1)
    
    return ventana

# --- Pantalla inicial ---
def cargarSE():
    system("CLS")
    root = crear_ventana("Poké-Expert", "imagenes/fondo_app.jpg")
    
    btn = tk.Button(root, text="¡Comenzar!", font=("Helvetica", 16, "bold"),
                    bg="#f7d23f", fg="#153a5c", bd=0,
                    command=lambda: [root.destroy(), iniciar_trivia()])
    btn.place(relx=0.5, rely=0.85, anchor="center", width=180, height=50)
    
    root.mainloop()

def iniciar_trivia():
    ds = load_dataset("lhoestq/pokemonData")["train"]
    
    tipos = sorted({p["Type1"] for p in ds if p["Type1"]} | {p["Type2"] for p in ds if p["Type2"]})
    generaciones = sorted({p["Generation"] for p in ds})
    
    root = crear_ventana("Sistema Experto Pokémon", "imagenes/fondo_app.jpg")
    cont = tk.Frame(root, bg="white", bd=0)
    cont.place(relx=0.5, rely=0.30, anchor="center")
    
    # Variables
    nombre_var = tk.StringVar()
    tipo_var   = tk.StringVar(value=tipos[0])
    gen_var    = tk.IntVar(value=generaciones[0])
    hp_var     = tk.IntVar(value=1)
    ata_var    = tk.IntVar(value=1)
    def_var    = tk.IntVar(value=1)
    vel_var    = tk.IntVar(value=1)
    
    # --- Sección de filtros ---
    lbl_title = tk.Label(cont, text="Filtros de Búsqueda", font=("Helvetica", 14, "bold"), bg="white")
    lbl_title.grid(row=0, column=0, columnspan=2, pady=(0,10))
    
    # Nombre
    tk.Label(cont, text="Nombre:", bg="white").grid(row=1, column=0, sticky="w", padx=5)
    tk.Entry(cont, textvariable=nombre_var, width=25).grid(row=1, column=1, padx=5, pady=2)
    
    # Tipo
    tk.Label(cont, text="Tipo favorito:", bg="white").grid(row=2, column=0, sticky="w", padx=5)
    ttk.Combobox(cont, textvariable=tipo_var, values=tipos, state="readonly")\
        .grid(row=2, column=1, padx=5, pady=2)
    
    # Generación
    tk.Label(cont, text="Generación:", bg="white").grid(row=3, column=0, sticky="w", padx=5)
    ttk.Combobox(cont, textvariable=gen_var, values=generaciones, state="readonly")\
        .grid(row=3, column=1, padx=5, pady=2)
        
    # HP
    tk.Label(cont, text="Vida      ≥:", bg="white").grid(row=4, column=0, sticky="w", padx=5)
    tk.Scale(cont, from_=1, to=255, orient="horizontal", variable=hp_var, length=200, bg="white")\
        .grid(row=4, column=1, padx=5, pady=2)
        
    # Velocidad
    tk.Label(cont, text="Velocidad ≥:", bg="white").grid(row=5, column=0, sticky="w", padx=5)
    tk.Scale(cont, from_=1, to=150, orient="horizontal", variable=vel_var, length=200, bg="white")\
        .grid(row=5, column=1, padx=5, pady=2)
        
    # Ataque
    tk.Label(cont, text="Ataque    ≥:", bg="white").grid(row=6, column=0, sticky="w", padx=5)
    tk.Scale(cont, from_=1, to=150, orient="horizontal", variable=ata_var, length=200, bg="white")\
        .grid(row=6, column=1, padx=5, pady=2)
        
    # Defensa
    tk.Label(cont, text="Defensa   ≥:", bg="white").grid(row=7, column=0, sticky="w", padx=5)
    tk.Scale(cont, from_=1, to=150, orient="horizontal", variable=def_var, length=200, bg="white")\
        .grid(row=7, column=1, padx=5, pady=2)
        
    # Botón Buscar
    tk.Button(cont, text="Buscar", font=("Helvetica", 12, "bold"),
            bg="#2a75bb", fg="white", bd=0,
            command=lambda: filtrar_pokemon(ds, nombre_var, tipo_var, gen_var, hp_var, vel_var, ata_var, def_var, result_frame))\
        .grid(row=9, column=0, columnspan=2, pady=15)
        
    # --- Sección de resultados desplazable ---
    result_frame = tk.Frame(root, bg="white", bd=2, relief="sunken")
    result_frame.place(relx=0.5, rely=0.58, anchor="n", width=480, height=300)
    
    canvas = tk.Canvas(result_frame, bg="white")
    scrollbar = tk.Scrollbar(result_frame, orient="vertical", command=canvas.yview)
    inner = tk.Frame(canvas, bg="white")
    
    inner.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=inner, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    root.mainloop()

# --- Lógica de filtrado ---
def filtrar_pokemon(ds, nombre_var, tipo_var, gen_var, hp_var, vel_var, ata_var, def_var, container):
    
    nombre = nombre_var.get().lower()
    tipo   = tipo_var.get()
    gen    = gen_var.get()
    hp     = hp_var.get()
    vel    = vel_var.get()
    ata    = ata_var.get()
    defe   = def_var.get()
    
    # Limpiar resultados previos
    for widget in container.winfo_children():
        widget.destroy()
        
    # Filtrar Pokémon
    filtrados = [
        p for p in ds
        if (nombre in p["Name"].lower())
        and (p["Type1"] == tipo or p["Type2"] == tipo)
        and p["Generation"] == gen
        and p["HP"] >= hp
        and p["Speed"] >= vel
        and p["Attack"] >= ata
        and p["Defense"] >= defe
    ]
    
    if filtrados:
        encabezado = "{:<3} {:<15} {:<7} {:<7} {:<7} {:<7}".format("#", "Nombre", "HP", "Vel", "Ata", "Def")
        tk.Label(container, text=encabezado, font=("Courier New", 10, "bold"), bg="white", anchor="w").pack(fill="x", padx=5)
        tk.Label(container, text="─" * 55, bg="white", anchor="w").pack(fill="x", padx=5)
        
        for i, p in enumerate(filtrados[:10], start=1):
            texto = "{:<3} {:<16} {:<7} {:<7} {:<7} {:<7}".format(i, p['Name'], p['HP'], p['Speed'], p['Attack'], p['Defense'])
            tk.Label(container, text=texto, bg="white", anchor="w", font=("Courier New", 10)).pack(fill="x", padx=0, pady=1)
        
        # Si hay solo 1 Pokémon, buscar su carta
        if len(filtrados) == 1:
            nombre_pokemon = filtrados[0]['Name'].lower()
            ds_card = load_dataset("TheFusion21/PokemonCards")["train"]
            carta = next((c for c in ds_card if c["name"].lower() == nombre_pokemon), None)
            
            if carta:
                def mostrar_carta():
                    # Crear ventana emergente
                    win = tk.Toplevel()
                    win.title(f"Carta de {carta['name']}")
                    win.geometry("350x520")
                    win.resizable(False, False)
                    
                    ancho, alto = 350, 520
                    sw = win.winfo_screenwidth()
                    sh = win.winfo_screenheight()
                    
                    x = (sw - ancho) // 2
                    y = (sh - alto) // 2
                    win.geometry(f"{ancho}x{alto}+{x}+{y}")
                    
                    url = carta["image_url"]
                    response = requests.get(url)
                    img = Image.open(BytesIO(response.content))
                    img = img.resize((320, 445), Image.LANCZOS)
                    img_tk = ImageTk.PhotoImage(img)
                    
                    lbl_img = tk.Label(win, image=img_tk)
                    lbl_img.image = img_tk
                    lbl_img.pack(pady=10)
                    
                    # Botón cerrar
                    tk.Button(win, text="Cerrar", command=win.destroy).pack(pady=10)
                
                tk.Button(container, text="Ver carta del Pokémon", bg="#ffcc00", fg="black",
                        font=("Helvetica", 10, "bold"), command=mostrar_carta)\
                        .pack(pady=10)
            else:
                tk.Label(container, text="No se encontró carta para este Pokémon", bg="white", fg="gray").pack(pady=5)
    else:
        tk.Label(container, text="— Ningún Pokémon encontrado —", bg="white", fg="gray").pack(pady=10)


# --- Inicio de la app ---
if __name__ == "__main__":
    cargarSE()