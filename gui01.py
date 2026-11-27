import tkinter as tk
from tkinter import messagebox, ttk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera aplicación")
ventana.geometry("350x200")

def saludar():
    messagebox.showinfo("Saludo", "¡Bienvenido a Python!")

# crea una etiqueta que muestra un texto.
etiqueta = ttk.Label(
    ventana,
    text="Aprendiendo Tkinter"
)
etiqueta.pack(pady=20)

# crea un botón interactivo.
boton = ttk.Button(
    ventana,
    text="Saludar",
    command=saludar
)
boton.pack(pady=10)

ventana.mainloop()