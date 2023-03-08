import tkinter
from tkinter import messagebox
from Práctica13contra import generar_contraseña

def contraseña():
    long = int(long_entrada.get())
    mayusculas = mayusculas_var.get()
    especiales = especiales_var.get()
    contraseña = generar_contraseña(long=long, mayusculas=mayusculas, especiales=especiales)
    messagebox.showinfo("Contraseña", "Tu contraseña es: " + contraseña)
    contraseña_entrada.delete(0, tkinter.END)
    contraseña_entrada.insert(0, contraseña)

ventana = tkinter.Tk()
ventana.title('Generador de Contraseñas')
ventana.geometry("600x250")
ventana.resizable(False, False)
ventana.config(bg="light green")


long_label = tkinter.Label(ventana, text='Longitud:', bg="light green")
long_label.pack()
long_entrada = tkinter.Entry(ventana)
long_entrada.insert(0, "8")
long_entrada.pack()
mayusculas_var = tkinter.BooleanVar()
boton_mayusculas = tkinter.Checkbutton(ventana, text="Agregar mayúsculas", variable=mayusculas_var, bg="light green")
boton_mayusculas.pack()
especiales_var = tkinter.BooleanVar()
boton_especiales = tkinter.Checkbutton(ventana, text="Agregar Carácteres Especiales", variable=especiales_var, bg="light green")
boton_especiales.pack()
boton = tkinter.Button(ventana, text="Generar contraseña", command=contraseña, bg="green" , fg="White")
boton.pack()
contraseña_entrada = tkinter.Entry(ventana)
contraseña_entrada.pack()


ventana.mainloop()
