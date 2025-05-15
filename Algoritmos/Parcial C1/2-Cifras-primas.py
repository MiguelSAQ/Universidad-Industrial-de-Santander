print("Cifras Primas")
n = input("Número a analizar: ")
print()

L = []  # Lista vacía donde guardaremos las cifras primas de "n"

for i in range(len(n)):            # El código itera desde cero hasta el número de cifras de n
    c = 0                          # Contador de divisores de n[i]
    for j in range(2, int(n[i])):  # El código itera desde 2 hasta la cifra n[i] en busca de divisores.
        if int(n[i]) % j == 0:     # Si la cifra entre j tiene como residuo cero, entonces j es divisor.
            c += 1                 # Si j es divisor, entonces el contador aumenta en 1. 
    if c == 0 and int(n[i]) != 0 and int(n[i]) != 1:   # Si no hay divisores y la cifra no es cero ni uno,
        L.append(int(n[i]))                            # la cifra se guarda en la lista L.

print(f"El número {n} tiene {len(n)} cifras de las cuales {len(L)} cifras son primas y son: ")
print(f"Cifras primas = {L}")