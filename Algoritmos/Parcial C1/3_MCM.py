print("Mínimo Común Múltiplo")
n = int(input("Número 1: "))
m = int(input("Número 2: "))
print()

# Este bloque encuentra el número más grande y lo almacena en la variable "g"
if n > m:
    g = n
else: 
    g = m

c = 0  # Una variable "c" de apoyo donde guardaremos el MCM.

while c == 0:  # Mientras "c" valga cero, no se ha encontrado ningún MCM, por lo que el código itera. 
    if g % n == 0 and g % m == 0:  # Si "g" es múltiplo tanto de n como de m, lo almacena en "c".
        c = g  # Ahora "c" vale "g", es decir, el MCM, por lo que el código deja de iterar.
    else:  # Si "g" no es múltiplo de n y m, aumenta el valor de "g" y sigue iterando.
        g += 1  # g aumenta en 1 para revisar el siguiente número hasta encontrar un MCM.

# Imprimir los resultados:
print(f"El mínimo común múltiplo de {n} y {m} es {g}, cuyos factores son {int(g/n)} y {int(g/m)} respectivamente, pues:")
print(f"{n} x {int(g/n)} = {g}")
print(f"{m} x {int(g/m)} = {g}")