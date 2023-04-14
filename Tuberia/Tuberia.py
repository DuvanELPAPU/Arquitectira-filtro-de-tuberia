from PIL import Image, ImageEnhance, ImageTk     #libreria para la manipulacion de imagenes
import tkinter as tk            #libreria para la creacion de la interfaz
from tkinter import filedialog

# Funcion para cambiar a escala de gris
def escala_grises(imagen):
    return imagen.convert('L')

# Funcion para aumentar el brillo
def brillo(imagen, valor):
    return ImageEnhance.Brightness(imagen).enhance(valor)

# Lista de las funciones (Tuberia de filtros)
tuberia = [
    escala_grises,
    lambda imagen: brillo(imagen, 1.5),
    # Espacio para mas filtros
]

# Funcion que aplica la tuberia de filtros
def aplicar_filtro(imagen, tuberia):
    for filtro in tuberia:
        imagen = filtro(imagen)
    return imagen

# Creamos la interfaz
ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Aplicar filtros de escala de gris y brillo")

# Agregamos un botón para seleccionar la imagen
def seleccionar_imagen():
    ruta_imagen = filedialog.askopenfilename()   #ruta de la imagen
    imagen_original = Image.open(ruta_imagen)
    imagen_original = imagen_original.resize((int(imagen_original.width/2), int(imagen_original.height/2))) # Escalar la imagen y aplicar Variable 
    imagen_convertida = aplicar_filtro(imagen_original, tuberia) #Eplicar la tuberia de filtros atraves del boton
    imagen_tk = ImageTk.PhotoImage(imagen_convertida) #Instancia para mostrar la imagen 
    imagen_label.config(image=imagen_tk)  #Interacion entre librerias 
    imagen_label.image = imagen_tk

boton_seleccionar = tk.Button(ventana, text="Seleccione una imagen", command=seleccionar_imagen)
boton_seleccionar.pack(pady=20)

# Agregamos un widget de Label para mostrar la imagen
imagen_label = tk.Label(ventana)
imagen_label.pack(expand=True, fill='both')

ventana.mainloop()    #iniciar la ventana
