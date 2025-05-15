print("Invertir palabra o frase")
n = input("Palabra/frase: ")
print()


# Invertir caracteres en la palabra/frase

inv1 = ""

for i in range(len(n)-1, -1, -1) :    # Esto itera desde la ultima posicion a la primera 
    inv1 += n[i]                      # Simplemente va guardando los terminos desde el ultimo hasta el primero en una lista vacia "inv1"

print("Invertido letra por letra: ", inv1)


# Invertir el orden de las palabras en la frase

p = n.split()
inv2 = ""

for j in range(len(p)-1, -1, -1) :
    inv2 += p[j] + " "

print("Invertido frase por frase: ", inv2)