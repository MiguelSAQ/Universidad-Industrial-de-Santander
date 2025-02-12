n = int(input("Numero de elementos:"))

L = [0]
a = 0
b = 1

for i in range(n-1):
    a, b = b, b+a
    L.append(a)

print(L)