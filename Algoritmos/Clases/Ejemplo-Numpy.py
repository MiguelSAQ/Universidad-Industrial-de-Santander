import numpy as np
import sys
import random as rnd

print("n ceros")
n = 100
A = np.zeros(n)
print(A)
print()

print("n ceros en 8 bits")
B = np.zeros(n, dtype=np.int64)
print(B)
print(sys.getsizeof(B))
print()

print("n numeros randoms en 8 bits")
for i in range(n) : 
    B[i] = rnd.randint(-127, 127)
print(B)
print()

print("Numero random de -n a n")
C = np.random.randint(-n,n)
print(C)
print()

print("Matrices")
Mat = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(Mat)
print("Escalar por matriz")
print(4 * Mat)
print("Matriz al cuadrado")
print(Mat ** 2)
print("Suma de matrices")
print(Mat + 2 * Mat)
print("Multiplicar matrices elemento a elemento")
print(Mat * Mat)
print("Multiplicacion de matrices")
print(Mat @ Mat)