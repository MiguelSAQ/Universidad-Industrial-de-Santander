import numpy as np
import matplotlib.pyplot as plt

n = int(input("Numero:"))

Y = [n]

while n != 1 :
    if n%2 == 0 :
        n = n/2
        Y.append(n)
    else: 
        n = 3*n+1
        Y.append(n)

X = np.linspace(0, len(Y)-1, len(Y))

plt.scatter(X,Y, color="Blue")
plt.plot(X,Y, color="Black")
plt.grid()
plt.show()





