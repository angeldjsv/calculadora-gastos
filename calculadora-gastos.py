# 1. Pedir presupuesto mensual
presupuesto = float(input("Ingresa tu presupuesto mensual: "))

# 2. Definir categorías de gasto
categorias = ["Alquiler", "Comida", "Transporte", "Entretenimiento"]

# 3. Crear lista para guardar gastos
gastos = []

# 4. Pedir gastos usando un bucle
for categoria in categorias:
    while True:
        try:
            gasto = float(input(f"Gasto en {categoria}: "))
            if gasto < 0:
                print("No puedes ingresar un número negativo, intenta de nuevo.")
                continue
            gastos.append(gasto)
            break
        except ValueError:
            print("Por favor, ingresa un número válido.")

# 5. Calcular total, promedio y restante
total_gastos = sum(gastos)
promedio_gasto = total_gastos / len(gastos)
restante = presupuesto - total_gastos

# 6. Mostrar resultados
print("\n----- Resumen de gastos -----\n")
for i in range(len(categorias)):
    print(f"{categorias[i]}: ${gastos[i]:.2f}")
print(f"\nTotal gastado: ${total_gastos:.2f}")
print(f"Promedio de gasto por categoría: ${promedio_gasto:.2f}")
print(f"Gasto restante: ${restante:.2f}")