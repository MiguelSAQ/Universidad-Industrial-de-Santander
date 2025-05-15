print("Desviación estándar de n números")
n = int(input("Cuántos números va a ingresar: "))

num = []

for i in range(1, n + 1):  
    numero = float(input(f"Número {i}: "))  
    num.append(numero)

prom = sum(num)/len(num)

std = ( sum((x - prom) ** 2 for x in num) / n ) ** (1/2)

print("La desviación estander es: ", std)