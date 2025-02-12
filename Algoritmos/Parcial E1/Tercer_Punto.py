n = input("Elementos a convertir:        ")    # Metemos la entrada como una cadena
print()
m = ""         # Creamos una cadena vacia

for i in range(len(n)) : # Vamos iterando desde 0 hasta el numero de elementos en la cadena "n"
    g = 10 - int(n[i])   # Convertimos el elemento "i" de la cadena "n" en un numero entero y lo restamos a 10 para convertilo a complemento 10.
    m += str(g)          # Almacenamos los elementos "g", ya convertidos en complemento 10, en la cadena vacia "m".

print(f"Elementos en complemento 10:  {m}")