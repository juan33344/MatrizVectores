import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk
import os

# Ruta absoluta del archivo de entrenamiento
archivo_entrenamiento = os.path.join(os.path.dirname(__file__), "entrena_chatbot.txt")

def cargar_pares(archivo):
    pares = []
    with open(archivo, 'r', encoding='utf-8') as f:
        for linea in f:
            if "=>" in linea:
                patron, respuesta = linea.split("=>")
                patron = patron.strip()
                respuesta = respuesta.strip().split("|")
                pares.append([patron, respuesta])
    return pares

pares = cargar_pares(archivo_entrenamiento)
chatbot = Chat(pares, reflections)

def respuesta_chatbot(texto):
    return chatbot.respond(texto)

def enviar(event=None): 
    mensaje = entrada_texto.get()
    ventana_conversacion.insert(tk.END, "Tú: " + mensaje + "\n")
    respuesta = respuesta_chatbot(mensaje)
    if respuesta:
        ventana_conversacion.insert(tk.END, "Chatbot: " + respuesta + "\n")
    else:
        ventana_conversacion.insert(tk.END, "Chatbot: Lo siento, no entiendo eso.\n")
    entrada_texto.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Chatbot con NLTK y Archivo de Entrenamiento")

ventana_conversacion = tk.Text(ventana, bd=1, bg="light gray", width=50, height=20)
ventana_conversacion.grid(row=0, column=0, columnspan=2)

entrada_texto = tk.Entry(ventana, bd=1, width=40)
entrada_texto.grid(row=1, column=0)

entrada_texto.bind("<Return>", enviar)

boton_enviar = tk.Button(ventana, text="Enviar", command=enviar)
boton_enviar.grid(row=1, column=1)

ventana.mainloop()

