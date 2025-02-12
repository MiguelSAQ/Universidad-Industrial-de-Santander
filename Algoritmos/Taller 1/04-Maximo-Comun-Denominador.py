print("Encontrar el máximo común divisor entre")
n = int(input("Número 1:"))
m = int(input("Número 2:"))
print()

if n < m:       # En este bloque se almacena el número menor en "c".
    c = n       # n es menor que m.
else:
    c = m       # m es menor o igual que n.

for i in range(1, c + 1):          # El rango debe incluir "c", por eso se usa c + 1.
    if n % i == 0 and m % i == 0:  # Se verifica si "i" es divisor de ambos números.
        mcd = i                    # Se almacena el último divisor común (el mayor).

print("El máximo común divisor es:", mcd)