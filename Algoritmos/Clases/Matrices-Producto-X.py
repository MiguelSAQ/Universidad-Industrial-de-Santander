import numpy as np

M1 = np.array([[1,0,0],[0,1,0],[0,0,1],[0,0,1]])
M2 = np.array([[1,2,3,0],[4,5,6,1],[7,8,9,0]])

n, m = M1.shape
m, p = M2.shape

R = np.zeros((n,p))

for i in range(n) :           # Fila
    for j in range(p) :       # Columna
        for k in range(m) :   # La que multiplica cada elemento de la fija por la columna
            R[i,j] += M1[i,k] * M2[k,j]

print(R)

# Filas x Columnas 