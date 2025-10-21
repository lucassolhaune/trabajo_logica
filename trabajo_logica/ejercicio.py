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

        # Si comen más, aumentar 25%        a -> alimento
        if comen_mas == 1:
            for a in receta:
                receta[a]["cantidad"] *= 1.25
                #receta = receta * 1.25 -> no se puede multiplicar un dict con un float

        comida_prioritaria = "pollo"

        totales = {}
        costos = {}
        costo_total = 0

        # Calcular totales y costos
        for comida, datos in receta.items():
            total_kg = (personas * datos["cantidad"]) / 1000

            # Redondear diferente según el tipo
            if comida == comida_prioritaria:
                total_kg = math.ceil(total_kg)     # al kilo entero
            else:
                total_kg = math.ceil(total_kg * 10) / 10  # a décimas

            totales[comida] = total_kg
            costos[comida] = total_kg * datos["precio"]
            costo_total += costos[comida]

        # Mostrar el resultado
        texto = f"Para {personas} personas:\n\n"
        for comida in receta:
            texto += f"{comida}: {totales[comida]} kg → ${costos[comida]:.0f}\n"
        texto += f"\nCosto total: ${costo_total:.0f}\n"
        texto += f"Comen más: {'Sí' if comen_mas else 'No'}"

        messagebox.showinfo("Resultado", texto)

    except:
        messagebox.showerror("Error", "Ingresá un número válido.")


# Interfaz
ventana = tk.Tk()
ventana.title("Calculadora de comida")
ventana.geometry("300x300")

tk.Label(ventana, text="Cantidad de personas:").pack()
entry_personas = tk.Entry(ventana)
entry_personas.pack()

variable_comen_mas = tk.IntVar()
tk.Checkbutton(ventana, text="Comen más de lo normal", variable=variable_comen_mas).pack(pady=5)

tk.Button(ventana, text="Calcular", command=calcular).pack(pady=10)

ventana.mainloop()
