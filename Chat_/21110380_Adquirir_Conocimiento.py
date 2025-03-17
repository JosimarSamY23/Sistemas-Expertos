import json
import os
import tkinter as tk
from tkinter import scrolledtext, simpledialog

def cargar_conocimiento(archivo="conocimiento.json"):
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def guardar_conocimiento(conocimiento, archivo="conocimiento.json"):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(conocimiento, f, indent=4, ensure_ascii=False)

def enviar_mensaje():
    usuario = entrada.get().strip()
    usuario_evaluar = usuario.lower()
    
    print(usuario_evaluar)

    chatbox.config(state=tk.NORMAL)
    chatbox.insert(tk.END, f"Tú: {usuario}\n")
    chatbox.config(state=tk.DISABLED)
    entrada.delete(0, tk.END)
    
    if usuario_evaluar in ["salir", "adiós", "bye"]:
        chatbox.config(state=tk.NORMAL)
        chatbox.insert(tk.END, "Chatbot: Hasta luego!\n")
        chatbox.config(state=tk.DISABLED)
        root.quit()
        return
    
    elif not usuario_evaluar:
        return
    
    if usuario_evaluar in conocimiento:
        respuesta = conocimiento[usuario_evaluar]

    else:
        respuesta = "No conozco la respuesta. ¿Puedes enseñarme?"
        chatbox.config(state=tk.NORMAL)
        chatbox.insert(tk.END, f"Chatbot: {respuesta}\n")
        chatbox.config(state=tk.DISABLED)
        root.update()
        nueva_respuesta = simpledialog.askstring("Aprendizaje", "¿Cuál sería la respuesta correcta?")

        if nueva_respuesta:
            conocimiento[usuario_evaluar] = nueva_respuesta.strip()
            guardar_conocimiento(conocimiento)
            respuesta = "¡Gracias! Ahora lo recordaré."
    
    chatbox.config(state=tk.NORMAL)
    chatbox.insert(tk.END, f"Chatbot: {respuesta}\n")
    chatbox.config(state=tk.DISABLED)
    chatbox.yview(tk.END)

conocimiento = cargar_conocimiento()
root = tk.Tk()
root.title("Chatbot de Aprendizaje")

chatbox = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD, width=50, height=20)
chatbox.pack(padx=10, pady=10)

frame_input = tk.Frame(root)
frame_input.pack(padx=10, pady=5, fill=tk.X)

entrada = tk.Entry(frame_input, width=40)
entrada.pack(side=tk.LEFT, expand=True, fill=tk.X)

boton_enviar = tk.Button(frame_input, text="Enviar", command=enviar_mensaje)
boton_enviar.pack(side=tk.RIGHT)

root.mainloop()