print("Cambio de base 10 a una base cualquiera (b)")
n = int(input("Número (n) en base 10: "))  # Número en base 10.
b = int(input("Nueva base (b) para n: "))  # Nueva base.
print()

Res = 0  # Residuo.
i = 0    # Exponente del 10.
Num = 0  # Número en base "b".

while n != 0:           # Mientras "n" sea diferente de cero.
    Res = n % b         # El residuo tras dividir el número "n" por la base "b".
    n = n // b          # La división entera tras dividir el número "n" por la base "b".
    Num += Res * 10**i  # Se va construyendo el número multiplicando el residuo por su posición (10^0, 10^1, ..., 10^n).
    i += 1              # Se va sumando 1 a "i" para cambiar el exponente de 10 en el paso anterior.

print(Num)
