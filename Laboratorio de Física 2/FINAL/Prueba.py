import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import time

# Cargar la imagen
img = cv2.imread('Prueba.jpg', cv2.IMREAD_GRAYSCALE)

# Obtener las dimensiones de la imagen
img_y, img_x = img.shape

# Tamaño real de la imagen (ajuste esto al tamño real que ocupa su imagen)
real_espira_width  = 0.1  # Por ejemplo, 10 cm de ancho
real_espira_height = 0.1  # Por ejemplo, 10 cm de alto

# Calcular el factor de escala: cuánto equivale 1 píxel en metros
scale_factor_x = real_espira_width / img_x  # Factor de escala en metros por píxel
scale_factor_y = real_espira_height / img_y  # Factor de escala en metros por píxel

# Preprocesamiento: umbral para obtener una imagen binaria
_, img_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

# Encontrar los contornos de la curva
contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Extraer coordenadas de los contornos y aplicar el factor de escala
x_values = []
y_values = []

for contour in contours:
    for point in contour:
        # Escalar las coordenadas por el factor de escala
        x_values.append(point[0][0] * scale_factor_x)  # Coordenada X
        y_values.append(point[0][1] * scale_factor_y)  # Coordenada Y

def MagneticField(x, y, wire, I=1): # Cambie el valor de I por el valor de la corriente real
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

Calidad = 100
x = np.linspace(-real_espira_width/10 , real_espira_width  + real_espira_width/10,  Calidad)
y = np.linspace(-real_espira_height/10, real_espira_height + real_espira_height/10, Calidad)

[x, y] = np.meshgrid(x, y)

sum_Bs = np.zeros_like(x)

# Iterar sobre los contornos y calcular el campo magnético solo entre puntos vecinos
for contour in contours:
    for i in range(len(contour) - 1):
        # Tomar puntos consecutivos del contorno
        wire = [(contour[i][0][0]  *  scale_factor_x, - (contour[i][0][1]  *  scale_factor_y) + real_espira_height ),
                (contour[i+1][0][0] * scale_factor_x, - (contour[i+1][0][1] * scale_factor_y) + real_espira_height )]
        B = MagneticField(x, y, wire)
        sum_Bs += B  # Sumar el campo magnético calculado para este par de puntos
        
        progress = i + 1
        percentage = (progress / (len(contour) - 1)) * 100
        print(f"Progreso: {progress}/{(len(contour)-1)} ({percentage:.2f}%)", end='\r')


# Visualización del campo magnético
fig, ax = plt.subplots(1, 1, figsize=(6, 6))
im = ax.pcolormesh(x, y, np.log10(np.abs(sum_Bs)), vmin=-5, vmax=-3, cmap="jet")
plt.title("Campo Magnético en un Trébol", fontweight='bold') 
ax.set_xlim(-real_espira_width/10 , real_espira_width  + real_espira_width/10)
ax.set_xlabel(r"$x$ [m]")
ax.set_ylim(-real_espira_height/10, real_espira_height + real_espira_height/10)
ax.set_ylabel(r"$y$ [m]")

divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.01)
cb = fig.colorbar(im, ax=ax, orientation="vertical", cax=cax)
cb.set_label("$\log(B)$", labelpad=5)


plt.show()

