import base_datos as db
import tkinter as tk
import unicodedata
import ventana
import random
import os

from tkinter import messagebox, ttk
from PIL import Image, ImageTk

def iniciar_juego():
    root = ventana.crear_ventana(500, 620, False, "Adivina el Animal", "imgs_app/Fondo_app.png")
    
    boton = tk.Button(root, text="¡Comenzar!", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white",
        activebackground="#45a049", bd=0, relief="flat", padx=10, pady=10, command=lambda:siguiente_ventana(root))  
    boton.place(x=180, y=520)
    
    root.mainloop()
    
def siguiente_ventana(ventana_anterior):
    global contador_preguntas, contador_categoria, pregunta_actual, lista_preguntas, lista_animales
    global label_pregunta, label_img, btn_si, btn_no, btn_omitir
    
    ventana_anterior.destroy()
    root = ventana.crear_ventana(500, 620, False, "Pensando en un animal", "imgs_app/Fondo_app.png")
    
    contador_preguntas = 1
    contador_categoria = 0
    
    lista_animales  = []
    lista_preguntas = ["Mamiferos","Reptiles","Anfibios","Peces","Aves","Insectos","Aracnidos"]
    pregunta_actual = "¿Tu animal pertenece a la categoría "+str(lista_preguntas[contador_preguntas-1]).lower()+"?"
    
    # ------------- COMPONENTES -------------
    label_pregunta = tk.Label(root, text=f"Pregunta {contador_preguntas}\n {pregunta_actual}", font=("Arial", 12), bg="#D3D3D3")
    label_pregunta.pack(pady=20)
    
    img_tk = ventana.actualizar_imagen_aleatorio()
    label_img = tk.Label(root, image=img_tk)
    label_img.image = img_tk
    label_img.pack(pady=10)
    
    btn_si = tk.Button(root, text="Si", font=("Arial", 14), bg="#E91E63", fg="white", width=22, relief="flat",
                        command=lambda:realizar_validacion(1,root))
    btn_si.pack(pady=10)
        
    btn_no = tk.Button(root, text="No", font=("Arial", 14), bg="#00BCD4", fg="white", width=22, relief="flat",
                        command=lambda:realizar_validacion(0,root))
    btn_no.pack(pady=10)
        
    btn_omitir = tk.Button(root, text="Omitir", font=("Arial", 14), bg="#673AB7", fg="white", width=22, relief="flat",
                        command=lambda:realizar_validacion(2,root))
    btn_omitir.pack(pady=10)
    # ------------- COMPONENTES -------------
    
    root.mainloop()

def realizar_validacion(atributo, contenedor):
    global contador_preguntas, contador_categoria, pregunta_actual, lista_preguntas, lista_animales
    
    if atributo == 1 and contador_categoria < 7:
        categoria = lista_preguntas[contador_categoria]
        lista_animales, lista_preguntas = db.obtener_datos(categoria)
        random.shuffle(lista_preguntas)
        
        contador_categoria += 10
        
    elif atributo in [2, 1, 0] and contador_categoria > 7:
        if atributo == 1 or atributo == 0:
            indice_atributo = lista_preguntas[0][0]
            lista_animales = [animal for animal in lista_animales if animal[indice_atributo+3] == atributo]
        
        del lista_preguntas[0]
        
    if atributo != 1 and contador_categoria < 7:
        contador_categoria += 1
    
    # POSIBLES CASOS
    if len(lista_animales) == 1 and contador_categoria > 7:
        label_pregunta.config(text=f"¡Tu animal es {lista_animales[0][1]}!")
        
        img_tk = ventana.actualizar_imagen_aleatorio(lista_animales[0][2])
        label_img.config(image=img_tk)
        label_img.image = img_tk
        
        veces_jugado = lista_animales[0][3]+1
        
        label_veces_jugado = tk.Label(contenedor, text=f"Veces jugadas: {veces_jugado}", font=("Arial", 12), bg="#D3D3D3")
        label_veces_jugado.pack(pady=10)
        
        frame_botones = tk.Frame(contenedor, bg="#D3D3D3")
        frame_botones.pack(pady=10)
        
        btn_agregar = tk.Button(frame_botones, text="+", font=("Arial", 14), bg="#673AB7", fg="white", width=10, relief="flat",
                                command=lambda:insertar_animal_comprobar1(contenedor))
        btn_agregar.pack(side=tk.LEFT)
        ventana.ToolTip(btn_agregar,"Agregar nuevo animal")
        
        btn_grafo = tk.Button(frame_botones, text="o", font=("Arial", 14), bg="#673AB7", fg="white", width=10, relief="flat",
                            command=lambda:ventana.crear_grafo(lista_animales[0],obtener_categoria(contador_categoria-10)))
        btn_grafo.pack(side=tk.RIGHT)
        ventana.ToolTip(btn_grafo,"Mostrar atributos")
        
        btn_reiniciar = tk.Button(contenedor, text="Reiniciar", font=("Arial", 14), bg="#673AB7", fg="white", width=21, relief="flat",
                                command=lambda:reiniciar_juego(contenedor))
        btn_reiniciar.pack(anchor="center")
        ventana.ToolTip(btn_reiniciar,"Jugar de nuevo")
        
        deshabilitar_botones()
        db.actualizar_valor(obtener_categoria(contador_categoria-10),lista_animales[0][1],veces_jugado)
        
        return
    
    elif len(lista_animales) == 0 and contador_categoria > 7:
        label_pregunta.config(text="No he podido acertar con el animal que me has descrito")
        
        img_tk = ventana.actualizar_imagen_aleatorio("imgs_app/gato_fin.jpg")
        label_img.config(image=img_tk)
        label_img.image = img_tk
        
        frame_botones = tk.Frame(contenedor, bg="#D3D3D3")
        frame_botones.pack(pady=10)
        
        btn_agregar = tk.Button(frame_botones, text="Agregar", font=("Arial", 14), bg="#673AB7", fg="white", width=22, relief="flat",
                                command=lambda:insertar_animal_comprobar1(contenedor))
        btn_agregar.pack()
        ventana.ToolTip(btn_agregar,"Agregar nuevo animal")
        
        btn_reiniciar = tk.Button(frame_botones, text="Reiniciar", font=("Arial", 14), bg="#8A4F33", fg="white", width=22, relief="flat",
                                command=lambda:reiniciar_juego(contenedor))
        btn_reiniciar.pack()
        ventana.ToolTip(btn_reiniciar,"Jugar de nuevo")
        
        deshabilitar_botones()
        return
    
    elif len(lista_animales) > 1 and len(lista_preguntas) == 0 and contador_categoria > 7:
        label_pregunta.config(text="He encontrado múltiples coincidencias")
        
        label_img.pack_forget()
        label_pregunta.pack_forget()
        
        deshabilitar_botones()
        actualizar_coincidencias(contenedor)
        
        return
    
    # ACTUALIZAR PREGUNTAS
    if contador_categoria < 7:
        pregunta_actual = "¿Tu animal pertenece a la categoría "+str(lista_preguntas[contador_categoria]).lower()+"?"
    else:
        pregunta_actual = lista_preguntas[0][1]
    
    img_tk = ventana.actualizar_imagen_aleatorio()
    label_img.config(image=img_tk)
    label_img.image = img_tk
    
    contador_preguntas += 1
    label_pregunta.config(text=f"Pregunta {contador_preguntas}\n {pregunta_actual}")

def insertar_animal_comprobar1(contenedor):
    contenedor.destroy()
    root = ventana.crear_ventana(500, 620, False, "Ingresar nuevo animal", "imgs_app/Fondo_app.png")
    
    label_nombre = tk.Label(root, text="Ingresa un animal", font=("Arial", 12), bg="#D3D3D3", width=32, padx=5, pady=5)
    label_nombre.place(x=100, y=50)
    
    entry_nombre = tk.Entry(root, width=32, justify="center", font=("Arial", 12),border=5.5)
    entry_nombre.place(x=100, y=82)
    
    main_frame = tk.Frame(root)
    main_frame.place(x=100, y=180)
    
    label_categoria = tk.Label(main_frame, text="Selecciona la categoría", font=("Arial", 12), bg="#D3D3D3", width=33)
    label_categoria.pack()
    
    opciones_categoria = tk.StringVar()
    opciones_categoria.set("Mamiferos")
    categorias = ["Mamiferos", "Reptiles", "Anfibios", "Peces", "Aves", "Insectos", "Aracnidos"]
    
    radiobuttons_categoria = []
    
    for categoria in categorias:
        rb = tk.Radiobutton(main_frame, text=categoria, variable=opciones_categoria, value=categoria, width=29, 
                            justify="center", font=("Arial", 12))
        rb.pack(anchor="center")
        radiobuttons_categoria.append(rb)
    
    btn_comprobar = tk.Button(root, text="Comprobar", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white",
        activebackground="#45a049", bd=0, relief="flat", padx=10, pady=10, 
        command=lambda: insertar_animal_preguntas2(entry_nombre, opciones_categoria, main_frame, btn_comprobar, 
                                                radiobuttons_categoria,label_nombre,label_categoria,root))  
    btn_comprobar.place(x=180, y=520)
    
    btn_cerrar = tk.Button(root, text="x",font=("Arial", 14, "bold"), bg="#8CC9Ad", fg="white",
        activebackground="#45a049", bd=0, relief="flat", padx=10, pady=10,command=lambda:reiniciar_juego(root))
    btn_cerrar.place(x=138,y=520)
    ventana.ToolTip(btn_cerrar,"Cerrar")
    
    btn_ayuda = tk.Button(root, text="?",font=("Arial", 14, "bold"), bg="#8CC9Ad", fg="white",
        activebackground="#45a049", bd=0, relief="flat", padx=10, pady=10, 
        command=lambda: messagebox.showinfo("Ayuda","Ingresa un nombre válido y selecciona la categoría a la que pertenece"))
    btn_ayuda.place(x=318,y=520)
    ventana.ToolTip(btn_ayuda,"Ayuda")

def agignar_valor(pregunta, valor, preguntas, respuestas, animal, ventana, nombre_categoria, progress_var):
    global contador
    
    respuestas.append(valor)
    
    if contador == len(preguntas)-1:
        progress_var.set(contador+1)
        
        for i in range(3,len(respuestas)+3):
            animal[i] = respuestas[i-3]
        
        db.insertar_animal(animal,nombre_categoria)
        messagebox.showinfo("Nota", f"El animal {animal[0]} se ha guardado correctamente")
        
        ventana.destroy()
        iniciar_juego()
    
    if contador < len(preguntas)-1:
        contador += 1
        progress_var.set(contador)
        pregunta.config(text=f"{preguntas[contador][1]}")

def insertar_animal_preguntas2(entry_nombre, categoria, frame, boton, rbs_categoria, label_nombre, label_categoria, root):
    global contador
    
    nombre_animal = str(entry_nombre.get())
    nombre_categoria = categoria.get()
    
    if len(nombre_animal) > 1 and not nombre_animal.isnumeric():
        aux_bandera_animal = False
        
        animales, preguntas = db.obtener_datos(nombre_categoria,True,True)
        campos = len(preguntas)
        
        nombre_animal = quitar_acentos(str(nombre_animal).capitalize())
        
        for animal in animales:
            aux_animal = quitar_acentos(str(animal[1]).capitalize())
            if aux_animal.find(nombre_animal) != -1:
                aux_bandera_animal = True
                break
                
        if not aux_bandera_animal:
            label_nombre.pack_forget()
            label_categoria.pack_forget()
            
            entry_nombre.config(state=tk.DISABLED)
            entry_nombre.pack_forget()
            
            boton.config(state=tk.DISABLED)
            boton.pack_forget()
            
            frame.pack_forget()
            
            for rb in rbs_categoria:
                rb.pack_forget()
            
            animal = [nombre_animal, "imagenes/predeterminado.jpg", 0]
            for i in range(campos):
                animal.append(0)
            
            respuestas = []
            root.destroy()
            
            ventana_preguntas = ventana.crear_ventana(500, 620, False, "Ingresar nuevo animal", "imgs_app/Fondo_app.png")
            contador = 0
            
            label_pregunta = tk.Label(ventana_preguntas, text=f"{preguntas[contador][1]}", font=("Arial", 12), bg="#D3D3D3")
            label_pregunta.pack(pady=20)
            
            btn_si = tk.Button(ventana_preguntas, text="Si", font=("Arial", 14), bg="#E91E63", fg="white", width=22, relief="flat",
                            command=lambda: agignar_valor(label_pregunta,1,preguntas,respuestas,animal,
                                                        ventana_preguntas,nombre_categoria,progress_var))
            btn_si.pack(pady=10)
            
            btn_no = tk.Button(ventana_preguntas, text="No", font=("Arial", 14), bg="#00BCD4", fg="white", width=22, relief="flat",
                            command=lambda: agignar_valor(label_pregunta,0,preguntas,respuestas,animal,
                                                        ventana_preguntas,nombre_categoria,progress_var))
            btn_no.pack(pady=10)
            
            progress_var = tk.IntVar()
            progress = ttk.Progressbar(ventana_preguntas, orient="horizontal", length=300, mode="determinate", variable=progress_var, maximum=len(preguntas))
            progress.pack(pady=20)
            
        else:
            messagebox.showinfo("Nota", f"El animal {entry_nombre.get()} ya existe dentro de la base de conocimiento")
    else:
        messagebox.showwarning("Advertencia", "Debes ingresar un dato válido")

# FUNCIONES EXTRAS
def actualizar_coincidencias(root):
    titulo = tk.Label(root, text="Múltiples coincidencias", font=("Arial", 12), bg="#D3D3D3")
    titulo.pack(pady=20)
    
    frame_resultados = tk.Frame(root, bg="white")
    frame_resultados.pack(pady=10)
    
    imagenes_tk = []
    botones_aceptar = []
    
    for i, animal in enumerate(lista_animales):
        nombre = animal[1]
        ruta   = animal[2]
        
        try:
            imagen = Image.open(ruta)
            imagen = imagen.resize((180, 180))
            imagen_tk = ImageTk.PhotoImage(imagen)
            imagenes_tk.append(imagen_tk)
            
            contenedor = tk.Frame(frame_resultados, bg="white", padx=5, pady=5)
            contenedor.grid(row=i//2, column=i%2)
            
            etiqueta_imagen = tk.Label(contenedor, image=imagen_tk, bg="white")
            etiqueta_imagen.pack()
            
            etiqueta_nombre = tk.Label(contenedor, text=nombre, bg="white", font=("Arial",12))
            etiqueta_nombre.pack()
            
            boton_aceptar = tk.Button(contenedor, text="Si", bg="white", border=3, width=10,
                                    command=lambda n=nombre:[
                                        btn_comprobar.config(state=tk.DISABLED),
                                        mostrar_ayuda(n, root)])
            boton_aceptar.pack()
            botones_aceptar.append(boton_aceptar)
            
        except Exception as e:
            print(f"Error cargando imagen {ruta}: {e}")
            
    root.imagenes_tk = imagenes_tk
    
    frame_botones = tk.Frame(root, bg="#D3D3D3")
    frame_botones.pack(pady=10)
    
    btn_comprobar = tk.Button(frame_botones, text="Ninguno", font=("Arial", 14), bg="#673AB7", fg="white", width=21, relief="flat",
                                command=lambda:[
                                    btn_agregar.config(state=tk.NORMAL),
                                    btn_comprobar.config(state=tk.DISABLED),
                                    [b.config(state=tk.DISABLED) for b in botones_aceptar]
                                ])
    btn_comprobar.pack(side=tk.LEFT)
    
    btn_agregar = tk.Button(frame_botones, text="+", font=("Arial", 14), bg="#673AB7", fg="white", width=10, relief="flat", state=tk.DISABLED,
                                command=lambda: insertar_animal_comprobar1(root))
    btn_agregar.pack(side=tk.RIGHT)
    ventana.ToolTip(btn_agregar,"Agregar nuevo animal")

def mostrar_ayuda(nombre, ventana_anterior):
    global lista_animales
    
    ventana_anterior.destroy()
    lista_animales = [animal for animal in lista_animales if nombre == animal[1]]
    veces_jugado = lista_animales[0][3]+1
    
    root = ventana.crear_ventana(420, 320, False, "Coincidencia", lista_animales[0][2])
    
    def cerrar_ventana():
        db.actualizar_valor(obtener_categoria(contador_categoria - 10), lista_animales[0][1], veces_jugado)
        root.destroy()
        iniciar_juego()
    
    btn_grafo = tk.Button(root, text=f"Animal: {lista_animales[0][1]}\nVeces jugadas: {veces_jugado}", font=("Arial", 12), bg="#D3D3D3", border=5,
                            command=lambda:ventana.crear_grafo(lista_animales[0],obtener_categoria(contador_categoria-10)))
    btn_grafo.place(x=20, y=20)
    ventana.ToolTip(btn_grafo,"Mostrar atributos")
    
    root.protocol("WM_DELETE_WINDOW", cerrar_ventana)
    
def quitar_acentos(nombre):
    nombre_normalizado = unicodedata.normalize('NFD',nombre)
    nombre_ = ''.join(c for c in nombre_normalizado if unicodedata.category(c) != 'Mn')
    return nombre_

def deshabilitar_botones():
    btn_omitir.config(state=tk.DISABLED)
    btn_omitir.pack_forget()
    
    btn_si.config(state=tk.DISABLED)
    btn_si.pack_forget()
    
    btn_no.config(state=tk.DISABLED)
    btn_no.pack_forget()
    
def obtener_categoria(indice_categoria):
    categorias = ["Mamiferos","Reptiles","Anfibios","Peces","Aves","Insectos","Aracnidos"]
    return categorias[indice_categoria]

def reiniciar_juego(ventana_anterior):
    ventana_anterior.destroy()
    iniciar_juego()
# FIN FUNCIONES EXTRAS

if __name__ == "__main__":
    os.system("cls")
    
    if not os.path.exists("Adivina_Animal.db"):
        db.crear_database()
    
    iniciar_juego()