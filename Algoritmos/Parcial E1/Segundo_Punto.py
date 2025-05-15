n = int(input("Numero de la serie:"))
print()

L = []    # Lista vacia donde se almacena la serie
a = 0     # Primer elemento de la serie de Fibonacci
b = 1     # Segundo elemento de la serie de Fibonacci

for i in range(n): # Esto va crear n elementos de la serie de fibonacci empezando a contar desde 1.
    L.append(a) # Va guardando el elemento "a" en la lista
    a, b = b, b+a   # Esto define el primer elemento "a" como el segundo elemento "b", y redefine a "b" como la suma de "a" y "b".
    
R = 0      # "R" sera la sumatoria de los elementos, des el primer elemento (0) hasta el ultimo elemento hasta n.

for j in range(len(L)) :    # El rango es el tamaño de L, pues si L tiene 10 elementos, se van a sumar 10 elementos
    R += L[j]   # Se va sumando el primer elemento de la lista, luego el segundo, luego el tercero, y así hasta el elemento n
    
print(f"El {n} numero de la serie de Fibonacci es {L[len(L)-1]} y la sumatoria hasta este numero es {R}")
print(f"{n} elementos de la serie de Fibonacci = {L}")