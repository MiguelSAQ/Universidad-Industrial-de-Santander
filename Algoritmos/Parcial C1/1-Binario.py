print("Base 10 (decimal) a base 2 (binario)")
n = m = int(input("Número a convertir en binario: "))
print()

i, Num = 0, 0  # "i" es el número de cifras y el exponente de 10, mientras que "Num" es el número en binario

while n != 0:               # Mientras que n sea diferente de cero: 
    Num += (n % 2) * 10**i  # Multiplica el residuo de "n" entre "2" por 10^i y lo va sumando.
     # La función de 10**i es "armar" el número, almacenando el residuo en las unidades (10^0), decenas (10^1), centenas (10^2)...
    n //= 2                 # Redefine n como la división entera de n entre 2.
    i += 1                  # Aumenta en uno el valor de i.

# Imprimir los resultados:
print(f"{m} en binario es {Num} y tiene {i} cifras")
