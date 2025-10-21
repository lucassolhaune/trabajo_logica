#### LUCAS SOLHAUNE - LÓGICA Y ESTRUCTURA DE DATOS ####
import tkinter as tk
from tkinter import messagebox
import math

def calcular():
    try:
        personas = int(entry_personas.get())

        # Límite de personas
        if personas <= 0 or personas > 50:
            messagebox.showerror("Error", "Ingresá un número entre 1 y 50.")
            return

        comen_mas = variable_comen_mas.get()

        # Receta base (gramos por persona)
        receta = {
            "pollo": {"cantidad": 200, "precio": 3500},
            "arroz": {"cantidad": 100, "precio": 1200},
            "cebolla": {"cantidad": 30, "precio": 1000},
            "condimentos": {"cantidad": 10, "precio": 800}
        }

        # Si comen más, aumentar 25%
        if comen_mas == 1:
            for alimento in receta:
                receta[alimento]["cantidad"] *= 1.25

        comida_prioritaria = "pollo"
        totales = {}
        costos = {}
        costo_total = 0

        # Calcular totales y costos
        for comida in receta:
            cantidad = receta[comida]["cantidad"]
            precio = receta[comida]["precio"]

            total_kg = (personas * cantidad) / 1000  # de gramos a kilos

            # Redondear según el tipo
            if comida == comida_prioritaria:
                # Si es poca cantidad (menos de 1 kg), redondea a decimal
                if total_kg < 1:
                    total_kg = round(total_kg, 1)
                else:
                    total_kg = math.ceil(total_kg)   # si es más, al kilo entero
            else:
                # Los demás redondean a una décima
                total_kg = math.ceil(total_kg * 10) / 10  

            totales[comida] = total_kg
            costos[comida] = total_kg * precio
            costo_total += costos[comida]

        # Mostrar el resultado
        texto = "Para " + str(personas) + " personas:\n"

        for comida in receta:
            precio_kilo = receta[comida]["precio"]
            kilos = totales[comida]
            costo = costos[comida]

            texto += (
                comida.capitalize() + ": " + str(kilos) + " kg x $" + str(precio_kilo) + " = $" + str(int(costo)) + "\n")

        texto += "\nCosto total: $" + str(int(costo_total)) + "\n"

        if comen_mas:
            texto += "Comen más: Sí (se aumentó un 25%)"
        else:
            texto += "Comen más: No"

        messagebox.showinfo("Resultado", texto)

    except ValueError:
        messagebox.showerror("Error", "Ingresá un número válido.")


# Interfaz
ventana = tk.Tk()
ventana.title("Calculadora de comida")
ventana.geometry("300x300")

tk.Label(ventana, text="Cantidad de personas:").pack()
entry_personas = tk.Entry(ventana)
entry_personas.pack()

variable_comen_mas = tk.IntVar()
tk.Checkbutton(ventana, text=" Come o comen más de lo normal", variable=variable_comen_mas).pack(pady=5)

tk.Button(ventana, text="Calcular", command=calcular).pack(pady=10)

ventana.mainloop()
