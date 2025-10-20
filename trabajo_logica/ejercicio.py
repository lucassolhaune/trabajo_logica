                                        ####LUCAS SOLHAUNE, LOGICA Y ESTRUCTURA DE DATOS#### 
import tkinter as tk
from tkinter import messagebox
import math

def calcular():
    try:
        personas = int(entry_personas.get())

        if personas <= 0 and personas >= 50: #Pongo un limte de 50 personas como max.
            messagebox.showerror("Error", "Por favor ingresá un número mayor que 0.")
            return

        comen_mas = variable_comen_mas.get()

        # Cantidades base por persona (en gramos)
        receta = {
            "pollo": {"cantidad": 200, "precio": 3500}, # gramos por persona, precio por kilo
            "arroz": {"cantidad": 100, "precio": 1200},
            "cebolla": {"cantidad": 30, "precio": 1000},
            "condimentos": {"cantidad": 10, "precio": 800}
        }

        # Si comen más, aumentar un 25% las cantidades
        if comen_mas == 1:
            for alimento in receta:
                receta[alimento]["cantidad"] *= 1.25

        # Comida prioritaria (pollo), mas cara
        comida_prioritaria = "pollo"

        # Calcular cantidades totales en kilos y redondear hacia arriba
        totales = {}
        for comida, datos in receta.items():
            total_kg = (personas * datos["cantidad"]) / 1000
            totales[comida] = math.ceil(total_kg) if comida == comida_prioritaria else math.ceil(total_kg * 10) / 10  # prioritaria redondea a 1 kg, el resto a décimas

        # Calcular costos
        costos = {}
        for comida, datos in receta.items():
            costos[comida] = totales[comida] * datos["precio"]

        costo_total = sum(costos.values())

        # Mostrar resultado
        texto = f"Para {personas} personas:\n\n"
        for comida in receta:
            texto += f"{comida.capitalize()}: {totales[comida]} kg → ${costos[comida]:.2f}\n"
        texto += f"\nCosto total: ${costo_total:.2f}\n"
        texto += f"Comen más de lo normal: {'Sí' if comen_mas else 'No'}"

        messagebox.showinfo("Resultado", texto)

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un número válido (entero).")

#Interfaz usuario
ventana = tk.Tk()
ventana.title("Calculadora de Comida - Arroz con Pollo")
ventana.geometry("350x350")

tk.Label(ventana, text="Cantidad de personas:").pack(pady=5)
entry_personas = tk.Entry(ventana)
entry_personas.pack(pady=5)

variable_comen_mas = tk.IntVar()
tk.Checkbutton(ventana, text="Alguien come más de lo normal", variable=variable_comen_mas).pack(pady=5)

tk.Button(ventana, text="Calcular", command=calcular, bg="lightblue").pack(pady=15)

ventana.mainloop()
