import os       #Importamos el módulo para poder realizar comandos en la consola del sistema
import random   #Importamos el módulo para generar valores aleatorios
import time     #Importamos el módulo para hacer pausas de tiempo en la consola del sistema
import tkinter as tk
import json

def pregunta_cultura_general():
    resultado = tk.IntVar(value=-1)

    # Cargar preguntas desde archivo JSON
    with open("preguntas.json", "r", encoding="utf-8") as archivo:
        preguntas = json.load(archivo)

    # Seleccionar una pregunta aleatoria
    pregunta = random.choice(preguntas)

    root = tk.Toplevel()
    pantalla_ancho = root.winfo_screenwidth()
    pantalla_alto  = root.winfo_screenheight()
    
    x = (pantalla_ancho // 2) - (600 // 2)
    y = (pantalla_alto // 2)  - (680 // 2)
    
    root.title("Pregunta de Cultura")
    root.geometry(f'{600}x{680}+{x}+{y}')

    def responder(opcion_seleccionada):
        if opcion_seleccionada == pregunta["correcta"]:
            label_resultado.config(text="¡Correcto!")
            resultado.set(1)
        else:
            label_resultado.config(text=f"Incorrecto. Era: {pregunta['correcta']}")
            resultado.set(0)

        # Desactivar botones
        for boton in botones:
            boton.config(state=tk.DISABLED)

        root.after(2000, root.destroy)

    # Widgets
    label_pregunta = tk.Label(root, text=pregunta["pregunta"], font=("Arial", 14), wraplength=500, justify="center")
    label_pregunta.pack(pady=20)

    opciones = pregunta["opciones"]
    random.shuffle(opciones)

    botones = []
    for opcion in opciones:
        b = tk.Button(root, text=opcion, font=("Arial", 12), width=30, command=lambda o=opcion: responder(o))
        b.pack(pady=5)
        botones.append(b)

    label_resultado = tk.Label(root, text="", font=("Arial", 12))
    label_resultado.pack(pady=10)

    root.grab_set()
    root.wait_window()
    return resultado.get()

def Avinina_numero():
    resultado = tk.IntVar(value=-1)
    root = tk.Toplevel()
    
    pantalla_ancho = root.winfo_screenwidth()
    pantalla_alto  = root.winfo_screenheight()
    
    x = (pantalla_ancho // 2) - (600 // 2)
    y = (pantalla_alto // 2)  - (680 // 2)
    
    root.title("Adivina el número")
    root.geometry(f'{600}x{680}+{x}+{y}')
    root.resizable(False,False)

    num = random.randint(1, 100)
    intentos_permitidos = 7
    lista_num_ingresados = []
    contador = tk.IntVar(value=1)

    def terminar(valor):
        resultado.set(valor)
        root.destroy()

    def validar_numero():
        try:
            num_usuario = int(campo_num_ingresado.get())
        except ValueError:
            label_resultado.config(text="Ingresa un número válido.")
            return

        lista_num_ingresados.append(num_usuario)

        if num_usuario == num:
            label_resultado.config(text=f"¡Correcto! El número era {num}.")
            boton.config(state=tk.DISABLED)
            terminar(1)
        elif num_usuario > num:
            label_resultado.config(text="El número es menor.")
        else:
            label_resultado.config(text="El número es mayor.")

        label_historial.config(text=f"Números ingresados: {lista_num_ingresados}")
        contador.set(contador.get() + 1)
        label_intentos.config(text=f"Intento: {contador.get()} / {intentos_permitidos}")

        if contador.get() > intentos_permitidos:
            label_resultado.config(text=f"¡Has perdido! El número era: {num}")
            boton.config(state=tk.DISABLED)
            terminar(0)

    label_principal = tk.Label(root, text=f"Adivina el número entre 1 y 100", font=("Arial", 14), bg="#D3D3D3")
    label_principal.pack(pady=20)

    campo_num_ingresado = tk.Entry(root, width=32, justify="center", font=("Arial", 12))
    campo_num_ingresado.pack(pady=10)

    label_resultado = tk.Label(root, text="", font=("Arial", 12), bg="#D3D3D3")
    label_resultado.pack(pady=10)

    label_intentos = tk.Label(root, text=f"Intento: {contador.get()} / {intentos_permitidos}", font=("Arial", 12), bg="#D3D3D3")
    label_intentos.pack()

    label_historial = tk.Label(root, text="Números ingresados: []", font=("Arial", 10), bg="#D3D3D3")
    label_historial.pack(pady=10)

    boton = tk.Button(root, text="Validar", font=("Arial", 14, "bold"), bg="#5D3A00", fg="#F5DEB3",
                    activebackground="#3A1F1F", activeforeground="#FFD700", bd=0, relief="flat", padx=10, pady=10, width=28,
                    command=validar_numero)
    boton.pack(pady=20)

    root.grab_set()       # Bloquea interacción con otras ventanas
    root.wait_window()    # Espera hasta que la ventana se cierre

    return resultado.get()


def Simon_dice():
    print
    

