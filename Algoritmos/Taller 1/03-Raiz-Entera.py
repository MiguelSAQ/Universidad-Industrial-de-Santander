print("Determinar si el número tiene raíz cuadrada entera")
n = float(input("Número a revisar:"))
print()

if n < 0:                                                  # Revisa si la entrada es negativa.
    print("No tiene soluciones reales")                    # Si la entrada es negativa, no tiene soluciones reales.
elif (n)**(1/2) % 1 == 0:                                  # La condición: La raíz de "n" tiene como residuo cero.
    print(n, "tiene raíz entera y es", (n)**(1/2))         # Se cumple la condición, entonces tiene raíz entera.
else:                                                      # No cumple ninguna condición.
    print(f"{n} no tiene raíz entera y es: {(n)**(1/2)}")  # No se cumple la condición, entonces no tiene raíz entera.
