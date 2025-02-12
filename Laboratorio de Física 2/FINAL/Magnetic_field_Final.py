import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import time

# Definir la función en coordenadas polares
def polar_function(phi):
    return  np.cos(8*phi)

# Definir la función en coordenadas cartesianas 
def cartesian_coordinates(phi):
    x = polar_function(phi) * np.cos(phi)
    y = polar_function(phi) * np.sin(phi)
    return x, y

phi_values = np.linspace(0, 2 * np.pi, 150)
x_values, y_values = cartesian_coordinates(phi_values)

# Definir la Ley de Biot y Savart
def MagneticField(x, y, wire, I=50):
    mu0 = 4 * np.pi * 10**(-7)
    c = mu0 * I / (4 * np.pi)
    xA, yA = wire[0][0], wire[0][1]
    xB, yB = wire[1][0], wire[1][1]
    r1 = np.sqrt((x - xA)**2 + (y - yA)**2)
    r2 = np.sqrt((x - xB)**2 + (y - yB)**2)
    L = np.sqrt((xB - xA)**2 + (yB - yA)**2)
    CosTheta1 = (r2**2 - r1**2 - L**2) / (2 * L * r1)
    CosTheta2 = (r2**2 - r1**2 + L**2) / (2 * L * r2)
    distance = np.sqrt(2 * r1**2 * r2**2 + 2 * r1**2 * L**2 + 2 * r2**2 * L**2 - r1**4 - r2**4 - L**4) / (2 * L)
    Bfield = c * (CosTheta2 - CosTheta1) / distance
    return Bfield

X_tamaño = Y_tamaño = 2

x = np.linspace(-X_tamaño, X_tamaño, 250)
y = np.linspace(-Y_tamaño, Y_tamaño, 250)

[x, y] = np.meshgrid(x, y)



sum_Bs=0
B=0
for i in range(len(x_values)-1):
    wire=[(x_values[i],y_values[i]),(x_values[i+1],y_values[i+1])]
    B=MagneticField(x, y, wire)
    sum_Bs=sum_Bs+B
    
    progress = i + 1
    percentage = (progress / (len(x_values)-1)) * 100
    print(f"Progreso: {progress}/{(len(x_values)-1)} ({percentage:.2f}%)", end='\r')



fig, ax = plt.subplots(1, 1, figsize=(6, 6))
im = ax.pcolormesh(x, y, np.log10(np.abs(sum_Bs)), vmin=-8, vmax=-2, cmap="jet")
ax.set_xlim(-X_tamaño, X_tamaño)
ax.set_xlabel(r"$x$ [m]")
ax.set_ylim(-Y_tamaño, Y_tamaño)
ax.set_ylabel(r"$y$ [m]")

divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.01)
cb = fig.colorbar(im, ax=ax, orientation="vertical", cax=cax)
cb.set_label("$\log(B)$", labelpad=5)

plt.show()

