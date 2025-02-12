import numbers as np
n = int(input("Numero: "))
print()


# - - - Elemento primo menor a n - - - #

g = 0  # g será el numero primo que se encuentre 

for i in range(n) :    # Revisa todos los numeros antes de n en busca de un primo.
    c = 0    # Contador de divisores

    for k in range(2, i) :   # Va dividiendo cada numero desde 2 hasta antes de el mismo.

        if i % k == 0 :      # Si encuentra un numero con algun divisor, suma 1 a la variable c.
            c += 1 
    
    if c == 0 and i != 1 and i != 0 :   # Si en el anterior proceso, no encontro ningun divisor para el numero "i", enotnces "c" vale cero e "i" es primo (excluyendo al 0 y al 1).
        g = i  # Redefino a g como el ultimo numero primo encontrado, por lo que será el mas cercano a "n".
        
if g == 0 :   # Esto revisa que el numero no sea cero, ya que si lo es, significa que no encontro ningun numero primo. 
    print(f"- No hay elementos primos antes del {n}")
else: 
    print(f"- Elemento primo mas cercano antes del {n}: {g}")
        

# - - - Elemento primo menor a n - - - #

h = 0     # Un valor de apoyo.
m = n+1   # Ahora vamos a revisar los primos DESPUES de n, osea, los numeros mas grandes o iguales a n+1.

while h == 0:  # Mientras el valor de apoyo sea cero, el bucle sigue.
    
    c = 0    # Contador de divisores.

    for k in range(2, m) :  # Esto revisa desde 2 hasta antes del numero en busca de un primo.

        if m % k == 0 :  # Si el numero "m" que esta analizando tiene algun divisor, se suma 1 a la variable c.
            c += 1
    
    
    if c == 0 and m != 1 and m != 0 :   # Si encuentra algun numero primo, lo almacena en "h"
        h = m  # Como h ahora no vale cero, pues el bucle termina.
    else:
        c = 0  # Si no encuentra un primo, redefine el contador de primos.
        m += 1 # y le suma 1 al numero, para analizar el siguiente numero.
        
print(f"- Elemento primo mas cercano  despues de {n}: {h}")

# - - - ¿n es primo? - - - #

for i in range(2, n): # Esto simplemente revisa si el numero "n" es primo o no.
    if (n % i) == 0:  # Busca divisores desde 2 hasta el mismo, lo hay, el numero no es primo.
        print(f"- Ademas, el numero {n} no es primo")
        break
else:  # Si despues del bucle, no encontró ningun divisor para "n", entonces es primo.
    print(f"- Ademas, el numero {n} es primo.")