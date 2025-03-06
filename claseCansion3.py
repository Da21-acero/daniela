import tkinter as tk
from tkinter import messagebox
import re

class Cancion:
    def _init_(self, titulo, artista, duracion, genero):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion
        self.genero = genero

    def mostrar_info(self):
        return f"Título: {self.titulo}\nArtista: {self.artista}\nDuración: {self.duracion} min\nGénero: {self.genero}"


def validar_letras(valor):
    patron = re.compile("^[A-Za-zñÑ ]*$")
    return patron.match(valor) is not None

def evento_presionar_tecla(event, campo, label_validacion):
    texto = campo.get()
    if validar_letras(texto):
        label_validacion.config(text="", fg="green")
    else:
        label_validacion.config(text="Solo se permiten letras", fg="pink")

def mostrar_cancion():
    titulo = entry_titulo.get().strip()
    artista = entry_artista.get().strip()
    duracion = entry_duracion.get().strip()
    genero = entry_genero.get().strip()

    if not titulo or not artista or not duracion or not genero:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
        return

    if not validar_letras(titulo):
        messagebox.showerror("Error", "El título solo debe contener letras y espacios")
        return

    if not validar_letras(artista):
        messagebox.showerror("Error", "El artista solo debe contener letras y espacios")
        return

    if not validar_letras(genero):
        messagebox.showerror("Error", "El género solo debe contener letras y espacios")
        return

    try:
        duracion = float(duracion)
        if duracion <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "La duración debe ser un número válido y positivo")
        return

    cancion = Cancion(titulo, artista, duracion, genero)
    messagebox.showinfo("Información de la Canción", cancion.mostrar_info())


root = tk.Tk()
root.title("Registro de Canción")
root.geometry("350x350")

tk.Label(root, text="Título:").pack(pady=5)
entry_titulo = tk.Entry(root)
entry_titulo.pack()
label_validacion_titulo = tk.Label(root, text="", fg="pink")
label_validacion_titulo.pack()
entry_titulo.bind("<KeyRelease>", lambda event: evento_presionar_tecla(event, entry_titulo, label_validacion_titulo))

tk.Label(root, text="Artista:").pack(pady=5)
entry_artista = tk.Entry(root)
entry_artista.pack()
label_validacion_artista = tk.Label(root, text="", fg="pink")
label_validacion_artista.pack()
entry_artista.bind("<KeyRelease>", lambda event: evento_presionar_tecla(event, entry_artista, label_validacion_artista))

tk.Label(root, text="Duración (min):").pack(pady=5)
entry_duracion = tk.Entry(root)
entry_duracion.pack()

tk.Label(root, text="Género:").pack(pady=5)
entry_genero = tk.Entry(root)
entry_genero.pack()
label_validacion_genero = tk.Label(root, text="", fg="pink")
label_validacion_genero.pack()
entry_genero.bind("<KeyRelease>", lambda event: evento_presionar_tecla(event, entry_genero, label_validacion_genero))

btn_mostrar = tk.Button(root, text="Mostrar Canción", command=mostrar_cancion)
btn_mostrar.pack(pady=10)

root.mainloop()