print("Encontrar la media de números pares")
n = int(input("¿Hasta qué número?: "))
print()

if n < 2:
    print("Inserte un número válido (mayor o igual a 2)")
    quit()

# - - - - - Con listas - - - - - #

L = []  # Se define una lista vacía.

for i in range(1, n + 1):    # Itera entre 1 y n+1 (para tener en cuenta el último elemento).
    if i % 2 == 0:           # La condición: Si el residuo al dividir por 2 es cero, el número es par.
        L.append(i)          # Si se cumple la condición, el número es par y se guarda en la lista.
prom1 = sum(L) / len(L)      # Se suman los elementos de la lista y se divide por el número de elementos de la lista.

print(f"Números pares hasta {n} = ", L)
print()
print("Promedio con listas:", prom1)

# - - - - - Sin listas - - - - - #

suma1 = 0
cantidad1 = 0

for i in range(1, n + 1):    # Itera entre 1 y n+1 (para tener en cuenta el último elemento).
    if i % 2 == 0:           # La condición: Si el residuo al dividir por 2 es cero, el número es par.
        suma1 += i           # Si "i" cumple la condición, se suma el número "i".
        cantidad1 += 1       # Un contador que va sumando 1 cada vez que "i" cumple la condición.
prom2 = suma1 / cantidad1    # La suma de todas las "i" sobre el número de "i" que cumplieron la condición.
print("Promedio sin listas:", prom2)