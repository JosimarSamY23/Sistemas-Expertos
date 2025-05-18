import base_datos as db
import tkinter as tk

import threading
import pistas
import pygame
import historias
import random
import time
import os

from PIL import Image, ImageTk

def iniciar_juego():
    global root
    root = crear_ventana(600, 680, "Clue Samu", "imagenes/App/Fondo_app.jpg","ventana")
    
    boton = tk.Button(root, text="Comenzar", font=("Arial", 14, "bold"), bg="#5D3A00", fg="#F5DEB3", state=tk.DISABLED,
                activebackground="#3A1F1F", activeforeground="#FFD700", bd=0, relief="flat", padx=10, pady=10, width=28,
                command=lambda: [
                    pygame.mixer.music.stop(),
                    boton.place_forget(),
                    reproducir_sonido("audios/grito.mp3",0, None, False, True),
                    ventana_principal()
                ])
    boton.place(relx=0.5, y=580, anchor="center")
    reproducir_sonido("audios/Intro_1.mp3", 0, boton, False, True)
    
    def ventana_principal():
        global asesino, victima, lugar, arma, lista_pistas
        lista_personajes, lista_lugares, lista_armas = db.obtener_datos()
        
        lista_pistas = [0,0,0,0,0]
        asesino = random.choice(lista_personajes)
        victima = random.choice(lista_personajes)
        
        while asesino == victima:
            victima = random.choice(lista_personajes)
            
        lista_personajes = [
            tuple(list(p) + [1 if p[1] == asesino[1] else 0, 1 if p[1] == victima[1] else 0])
            for p in lista_personajes
        ]
        
        lugar = random.choice(lista_lugares)
        arma  = random.choice(lista_armas)
        
        lista_lugares = marcar_elemento(lista_lugares, lugar)
        lista_armas   = marcar_elemento(lista_armas, arma)
        
        # COMPONENTES
        historia = historias.generar_historia(asesino, victima, lugar, arma)
        label_principal = tk.Label(root, text=historia, font=("Arial", 12), bg="#D3D3D3", wraplength=550, justify="center", border=5)
        label_principal.pack(pady=20)
        
        root.label_principal = label_principal
        
        btn_personajes = tk.Button(root, text="Ver personajes", font=("Arial",14), bg="#5D3A00", fg="#F5DEB3", width=22, relief="flat", pady=10,
                bd=0, activebackground="#3A1F1F", activeforeground="#FFD700",
                command=lambda: [
                    habilitar_botones(False, btn_personajes, btn_lugares, btn_armas, btn_volver),
                    grid_clases(lista_personajes, root)
                ])
        btn_personajes.pack(pady=50)
        
        btn_lugares = tk.Button(root, text="Ver lugares", font=("Arial",14), bg="#5D3A00", fg="#F5DEB3", width=22, relief="flat", pady=10,
                bd=0, activebackground="#3A1F1F", activeforeground="#FFD700",
                command=lambda: [
                    habilitar_botones(False, btn_personajes, btn_lugares, btn_armas, btn_volver),
                    grid_clases(lista_lugares, root)
                ])
        btn_lugares.pack(pady=50)
        
        btn_armas = tk.Button(root, text="Ver armas", font=("Arial",14), bg="#5D3A00", fg="#F5DEB3", width=22, relief="flat", pady=10,
                bd=0, activebackground="#3A1F1F", activeforeground="#FFD700",
                command=lambda: [
                    habilitar_botones(False, btn_personajes, btn_lugares, btn_armas, btn_volver),
                    grid_clases(lista_armas, root)
                ])
        btn_armas.pack(pady=50)
        
        btn_volver = tk.Button(root, text="Volver", font=("Arial",14), bg="#5D3A00", fg="#F5DEB3", width=22, relief="flat", pady=10,
                bd=0, activebackground="#3A1F1F", activeforeground="#FFD700",
                command=lambda: [
                    habilitar_botones(True, btn_personajes, btn_lugares, btn_armas, btn_volver),
                    ocultar_grid(root)
                ])
        btn_volver.place_forget()
    
    def habilitar_botones(habilitar, btn1, btn2, btn3, btn4):
        if not habilitar:
            btn1.pack_forget()
            btn2.pack_forget()
            btn3.pack_forget()
            btn4.place(x=180, y=600)
        else:
            btn1.pack(pady=15)
            btn2.pack(pady=15)
            btn3.pack(pady=15)
            btn4.place_forget()
            
    def ocultar_grid(root):
        if hasattr(root, 'frame_clases'):
            root.frame_clases.pack_forget()
        
    def grid_clases(lista, root):
        frame_clases = tk.Frame(root, bg="#D3D3D3", pady=5)
        frame_clases.pack()
        root.frame_clases = frame_clases
        
        imagenes = []
        botones  = []
        
        for i, _clase in enumerate(lista):
            fondo = _clase[3]
            if victima[1] == _clase[1]:
                fondo = "imagenes/App/M"+str(i)+".png"
            
            imagen = Image.open(fondo)
            imagen = imagen.resize((150, 150))
            imagen_tk = ImageTk.PhotoImage(imagen)
            
            # Añadimos la imagen a la lista
            imagenes.append(imagen_tk)
            
            contenedor = tk.Frame(frame_clases, bg="#D3D3D3", padx=5, pady=5)
            contenedor.grid(row=i//3, column=i%3)
            
            etiqueta_imagen = tk.Label(contenedor, image=imagen_tk, bg="#D3D3D3", border=3)
            etiqueta_imagen.pack()
            
            etiqueta_nombre = tk.Label(contenedor, text=_clase[1], bg="#D3D3D3", font=("Arial",12))
            etiqueta_nombre.pack()
            
            btn_aceptar = tk.Button(contenedor, text="Ver", bg="#D3D3D3", border=3, width=10,
                        command=lambda clase = _clase:
                            crear_ventana(500,500,clase[1],clase[3],"emergente", clase)
                        )
            btn_aceptar.pack()
            
            # CLASE PERSONAJES
            if len(_clase) == 6:
                if _clase[1] == victima[1]:
                    etiqueta_imagen.configure(bg="#A4532E")
            # CLASE LUGARES Y ARMAS
            elif _clase[4] == 1:
                etiqueta_imagen.configure(bg="#A4532E")
                
            botones.append(btn_aceptar)
        
        root.imagenes_clases = imagenes
    root.mainloop()

def marcar_elemento(lista, elemento_objetivo):
    return [
        tuple(list(elem) + [1 if elem[1] == elemento_objetivo[1] else 0])
        for elem in lista
    ]

def reproducir_sonido(ruta, tiempo_espera, elemento, loop=False, terminar=False):
    def reproducir():
        time.sleep(tiempo_espera)
        pygame.mixer.init()
        pygame.mixer.music.load(ruta)
        pygame.mixer.music.play(-1 if loop else 0)
        
        if terminar:
            while pygame.mixer.music.get_busy():
                continue
            
            if elemento != None:
                elemento.config(state=tk.NORMAL)
                
    threading.Thread(target=reproducir).start()

def crear_ventana(ancho, alto, titulo, fondo_ventana, tipo, clase=None):
    if tipo == "ventana":
        ventana = tk.Tk()
    else:
        ventana = tk.Toplevel()
    
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto  = ventana.winfo_screenheight()
    
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2)  - (alto // 2)
    
    ventana.title(titulo)
    ventana.geometry(f'{ancho}x{alto}+{x}+{y}')
    ventana.resizable(False,False)
    
    if "#" not in fondo_ventana:
        fondo = cambiar_imagen(fondo_ventana, ancho, alto)
        
        fondo_label = tk.Label(ventana, image=fondo)
        fondo_label.image = fondo
        fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
    else:
        ventana.configure(bg=fondo_ventana)
    
    def stop_music():
            pygame.mixer.music.stop()
    
    if tipo == "emergente":
        lugares  = ["Habitación", "Cocina", "Biblioteca", "Baño", "Sótano"]
        personas = ["Samuel", "Catty", "Foxy", "Rene","Angela"]
        armas    = ["Pistola","Grillete","Espada","Cuerda","Candelabro"]
        
        label = tk.Label(ventana, text=f"Encuentra al culpable", font=("Arial",14), bg="lightgray", wraplength=ancho-50, justify="center", state=tk.NORMAL)
        label.pack(pady=15)
        
        if clase[1] in personas and clase[len(clase)-1] == 0:
            label.configure(text=f"{historias.obtener_cuartada(clase[1],lugar[1])}")
            
            btn_culpable = tk.Button(ventana, text="Culpable", background="red", font=("Arial", 14, "bold"), bg="#5D3A00", fg="#F5DEB3",
                        activebackground="#3A1F1F", activeforeground="#FFD700", bd=0, relief="flat", padx=10, pady=10,
                        command=lambda: [
                            ventana.destroy(),
                            fin_juego(clase)])
            
            btn_culpable.place(relx=0.5, y=alto-70, anchor="center")
            
        if clase[1] in lugares:
            index = lugares.index(clase[1])
            
            if lista_pistas[index] == 1:
                texto = ""
                for i in range(len(personas)):
                    _texto = historias.obtener_pista(personas[i], clase[1])
                    texto += f"{personas[i]}: {_texto}\n\n"

                label.configure(text=texto)
            
            else:
                label.configure(text="Busca pistas")
                btn_pista = tk.Button(ventana, text="Pista", background="red", font=("Arial", 14, "bold"), bg="#5D3A00", fg="#F5DEB3",
                        activebackground="#3A1F1F", activeforeground="#FFD700", bd=0, relief="flat", padx=10, pady=10,
                        command=lambda: [pista(index), ventana.destroy()])
            
                btn_pista.place(relx=0.5, y=alto-70, anchor="center")
            
            ruta = "audios/Lugares/"+str(clase[1])+"/"+str(clase[1])+str(random.randint(1,5))+".mp3"
            reproducir_audio(ruta)
        
        if clase[1] in armas:
            ruta = "audios/Armas/"+str(clase[1])+".mp3"
            label.pack_forget()
            
            btn_sonido = tk.Button(ventana, text="Sonido", background="red", font=("Arial", 14, "bold"), bg="#5D3A00", fg="#F5DEB3",
                        activebackground="#3A1F1F", activeforeground="#FFD700", bd=0, relief="flat", padx=10, pady=10,
                        command=lambda: reproducir_audio(ruta))
            
            btn_sonido.place(relx=0.5, y=alto-70, anchor="center")
        
        def reproducir_audio(ruta):
            pygame.mixer.init()
            pygame.mixer.music.load(ruta)
            pygame.mixer.music.play()
        
        def pista(index):
            try:
                minijuego = random.randint(1,2)
                if minijuego == 1:
                    valor_pista = pistas.Avinina_numero()
                    
                else:
                    valor_pista = pistas.pregunta_cultura_general()
                    
                lista_pistas[index] = valor_pista
            except:
                print
        
    if tipo == "ventana":
        return ventana

def cambiar_imagen(fondo_ventana, ancho, alto):
    imagen = Image.open(fondo_ventana)
    imagen = imagen.resize((ancho, alto), Image.LANCZOS)
    fondo  = ImageTk.PhotoImage(imagen)
    
    return fondo

def fin_juego(persona):
    def ocultar_elementos():
        widgets = root.winfo_children()
        
        for widget in widgets:
            widget.pack_forget()
            widget.grid_forget()
            widget.place_forget()
            
    if persona[len(persona)-2] == 1:
        ocultar_elementos()
        historia = historias.historia_final_buena(asesino,arma,lugar)
        fondo = cambiar_imagen("imagenes/App/Fin_bueno.png", 600, 680)
        
        reproducir_sonido("audios/Ganar.mp3", 0, None, False, True)
    else:
        ocultar_elementos()
        historia = historias.historia_final_mala(asesino,arma,lugar)
        sonido = "audios/Armas/"+str(arma[1])+".mp3"
        reproducir_sonido(sonido, 0, None, False, True)
        reproducir_sonido("audios/Perder.mp3", 2, None, False, True)
        
        fondo = cambiar_imagen("imagenes/App/Fin_malo.png", 600, 680)
    
    fondo_label = tk.Label(root, image=fondo)
    fondo_label.image = fondo
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    fondo = cambiar_imagen(asesino[3], 300, 300)
        
    etiqueta_imagen = tk.Label(root, image=fondo)
    etiqueta_imagen.image = fondo
    etiqueta_imagen.place(relx=0.5, rely=0.5, anchor="center")
    
    label_historia = tk.Label(root, text=historia, font=("Arial", 12), bg="#D3D3D3", wraplength=550, justify="center")
    label_historia.place(relx=0.5, y=525, anchor="center")
    
    boton = tk.Button(root, text="Reiniciar", font=("Arial", 14, "bold"), bg="#5D3A00", fg="#F5DEB3",
                activebackground="#3A1F1F", activeforeground="#FFD700", bd=0, relief="flat", padx=10, pady=10, width=28,
                command = lambda: [
                    root.destroy(),
                    iniciar_juego()])
    boton.place(relx=0.5, y=620, anchor="center")

# ------------------------------------------------------
if __name__ == "__main__":
    os.system("cls")
    
    if not os.path.exists("Clue.db"):
        db.crear_database()
        
    iniciar_juego()
# ------------------------------------------------------