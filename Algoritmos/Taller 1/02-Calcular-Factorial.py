print("Calcular el factorial de un número")
n = int(input("Número: "))
print()

fact = 1  # El primer elemento del factorial.

for i in range(1, n + 1):  # Se itera desde 1 hasta el número "n" dado.
    fact *= i              # Multiplica los números consecutivos desde 1 hasta "n" por cada ciclo de "i".
print(n, "! =", fact)      # Imprime el resultado.