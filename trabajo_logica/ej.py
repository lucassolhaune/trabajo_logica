#### Lucas Solhaune - Logica y estructura de datos ###

import tkinter as tk
from tkinter import messagebox
import math

def calcular():
    try:
        personas = int(entry_personas.get())

        if personas <= 0 or personas > 50:
            messagebox.showerror("Error", "Ingresá un número entre 1 y 50.")
            return #Sale de la funcion si el numero no es valido dentro del rango que yo estableci
        
        #Verifica si el checkbox “Comen más” está marcado (1 = sí, 0 = no)
        comen_mas = var_comen_mas.get()

        #Diccionario con los ingredientes:
        #cada clave es el nombre del alimento.
        #cada valor es una lista con [gramos por persona, precio por kilo].
        receta = {
            "pollo": [200, 3500], 
            "arroz": [100, 1200],
            "cebolla": [30, 1000],
            "condimentos": [10, 800]
        }
        
        #Texto donde se acumulan los resultados para mostrar.
        texto = f"Para {personas} personas:\n"
        total = 0

        #Recorre cada alimento del diccionario receta.
        #"comida" -> nombre (pollo, arroz, etc)
        #("gramos, precio") -> Valores de la lista
        for comida, (gramos, precio) in receta.items(): #Item devuelve "clave/valor"
            if comen_mas:
                gramos *= 1.25  #si comen más, aumenta 25% por persona (seleccionando el chekbox del principio)

            #Cuenta los kilos totales que se necesitan para esa comida
            kilos = (personas * gramos) / 1000 #Paso de gramos a kilos

            #redondeos
            if comida == "pollo":
                #Con el alimento pollo =
                #Si el total es menor a 1 kg, redondea a un decimal. Ej: Si es 0.83 -> 0.8
                #Si pesa 1kg o mas redondea hacia arriba usando math.ceil(). Ej: 1.2 -> 2
                kilos = round(kilos, 1) if kilos < 1 else math.ceil(kilos)
            else:
                # Los demás ingredientes se redondean a una décima (0.1)
                kilos = math.ceil(kilos * 10) / 10
            
            #Calcula el costo total de ese alimento (kilos * precio por kilo)
            costo = kilos * precio
            total += costo #suma al costo total general

            texto += f"{comida.capitalize()}: {kilos} kg x ${precio} = ${int(costo)}\n"
            


        texto += f"\nCosto total: ${int(total)}\n" #Agrega el costo total de todo al texto
        texto += "Comen más: Sí" if comen_mas else "Comen más: No" #Indica si se aumentó la comida por “comen más” o no

        messagebox.showinfo("Resultado", texto) #Muestra todo en una ventana emergente

    except ValueError:
        #Si el usuario escribió algo que no es número entero, muestra error
        messagebox.showerror("Error", "Ingresá un número válido.")

#Interfaz usuario
ventana = tk.Tk()
ventana.title("Calculadora de comida")
ventana.geometry("400x400")

tk.Label(ventana, text="Cantidad de personas:").pack()
entry_personas = tk.Entry(ventana)
entry_personas.pack()

var_comen_mas = tk.IntVar()
tk.Checkbutton(ventana, text="Comen más de lo normal", variable=var_comen_mas).pack(pady=5)

tk.Button(ventana, text="Calcular", command=calcular).pack(pady=15)

ventana.mainloop()
