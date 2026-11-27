import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()  # Instanciar ventana principal
ventana.title("Saludo interactivo")
ventana.geometry("360x180")


def saludar():  # Función invocada cuando se hace clic
    nombre = entrada.get().strip()  # Leer y quitar espacios extremos
    if not nombre:  # Comprobar que exista un nombre
        messagebox.showwarning("Dato requerido", "Ingrese su nombre")
        return
    messagebox.showinfo("Saludo", f"¡Hola, {nombre}!")


ttk.Label(ventana, text="Nombre:").pack(pady=(16, 4))

entrada = ttk.Entry(ventana)  # Campo de una línea
entrada.pack(padx=20, fill="x")

ttk.Button(ventana, text="Saludar", command=saludar).pack(pady=12)

ventana.mainloop()