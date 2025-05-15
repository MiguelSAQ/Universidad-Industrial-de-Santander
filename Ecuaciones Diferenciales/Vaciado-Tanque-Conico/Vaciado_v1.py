import numpy as np
import pygame
import time
import tkinter as tk
from tkinter import simpledialog

# Función para calcular h(t)
def liquid_height(h0, a, c, H, R, g, t):
    term1 = h0 ** (5 / 2)
    term2 = (a * c * H**2 * np.sqrt(2 * g)) / (np.pi * R**2) * t
    height = (term1 - term2) ** (2 / 5) if term1 > term2 else 0
    return max(height, 0)  # Asegurar que la altura no sea negativa

# Calcular el tiempo máximo para vaciar el tanque
def calculate_emptying_time(h0, a, c, H, R, g):
    term1 = h0 ** (5 / 2)
    term2 = (a * c * H**2 * np.sqrt(2 * g)) / (np.pi * R**2)
    return term1 / term2

# Crear ventana interactiva con tkinter para ingresar parámetros
def get_user_parameters():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    while True:
        # Pedir parámetros al usuario
        R = float(simpledialog.askstring("Entrada", "Radio de la base del tanque (R) en metros:", parent=root))
        H = float(simpledialog.askstring("Entrada", "Altura total del tanque (H) en metros:", parent=root))
        h0 = float(simpledialog.askstring("Entrada", f"Altura inicial del líquido (h₀) menor o igual a {H} m:", parent=root))

        # Validar que h0 <= H
        if h0 <= H:
            break  # Si es válido, salir del bucle
        else:
            tk.messagebox.showerror("Error", f"Altura inicial (h0) debe ser menor o igual a la altura del tanque (H = {H} m).")

    a = float(simpledialog.askstring("Entrada", "Área de salida (a) en m²:", parent=root))
    c = float(simpledialog.askstring("Entrada", "Coeficiente de descarga (c):", parent=root))
    g = float(simpledialog.askstring("Entrada", "Gravedad (g) en m/s²:", parent=root))

    root.destroy()  # Cerrar la ventana
    return R, H, h0, a, c, g
# Parámetros iniciales desde la ventana interactiva
R, H, h0, a, c, g = get_user_parameters()

# Tiempo máximo para vaciar el tanque
max_time = calculate_emptying_time(h0, a, c, H, R, g)

# Configuración de Pygame
pygame.init()

# Información de la pantalla 
info = pygame.display.Info()
# Tamaño máximo de la pantalla
screen_width_max = info.current_w
screen_height_max = info.current_h

# Tamaño disponible para el tanque (restando los márgenes)
available_width = screen_width_max - 200
available_height = screen_height_max - 200

# Escala general para ajustar el tanque a la pantalla
screen_scale = 50  # Factor de escala para convertir metros a píxeles

# Dimensiones dinámicas de la ventana basadas en R y H
tank_height_px = H * screen_scale  # Altura del tanque en píxeles
tank_base_width_px = 2 * R * screen_scale  # Ancho de la base del tanque en píxeles

# Verificar si el tanque excede los límites de la pantalla (sin contar los márgenes)
scale_factor = 1  # Inicialmente no escalamos

# Ajustar la escala si es necesario
if tank_height_px > available_height:
    scale_factor = available_height / tank_height_px
elif tank_base_width_px > available_width:
    scale_factor = available_width / tank_base_width_px

# Ajustar la escala de todas las dimensiones si es necesario
tank_height_px = tank_height_px * scale_factor
tank_base_width_px = tank_base_width_px * scale_factor

# Ajustar el factor de escala global para mantener la relación
screen_scale = screen_scale * scale_factor

screen_width = max(600, tank_base_width_px + 100)  # Añadir margen horizontal
screen_height = max(800, tank_height_px + 100)  # Añadir margen vertical para cronómetro
screen = pygame.display.set_mode((int(screen_width), int(screen_height)))

pygame.display.set_caption("Vaciado de Tanque Cónico")
clock = pygame.time.Clock()

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
BLACK = (0, 0, 0)

# Fuente para el cronómetro
font = pygame.font.Font(None, 36)  # Fuente predeterminada, tamaño 36

# Coordenadas iniciales del triángulo
tank_x = (screen_width - tank_base_width_px) // 2
tank_y = (screen_height - tank_height_px) // 2

# Escala para convertir altura real del líquido a píxeles
scale = tank_height_px / H

# Gotas
drops = []
drop_radius = 5  # Radio de las gotas
drop_speed = 3   # Velocidad de caída (píxeles por frame)
drop_interval = 5  # Intervalo para generar gotas (frames)
frame_count = 0  # Contador de frames

# Inicialización para la animación
start_time = time.time()
running = True

while running:
    screen.fill((255, 200, 61))
    current_time = time.time() - start_time

    # Calcular la altura actual del líquido
    current_height = liquid_height(h0, a, c, H, R, g, current_time)

    # Verificar si el tanque está vacío
    if current_time >= max_time or current_height <= 1e-3:  # Umbral para evitar remanentes
        current_height = 0
        running = False

    # Calcular el radio actual del líquido
    current_radius = (tank_base_width_px / (tank_height_px * 2)) * current_height 

    # Dibujar el tanque vacío (relleno)
    pygame.draw.polygon(
        screen, (173, 216, 230), [  # Azul celeste claro
            (tank_x, tank_y), 
            (tank_x + tank_base_width_px, tank_y), 
            (tank_x + tank_base_width_px // 2, tank_y + tank_height_px)
        ]
    )

    # Dibujar el contorno del tanque
    pygame.draw.polygon(
        screen, BLACK, [
            (tank_x, tank_y), 
            (tank_x + tank_base_width_px, tank_y), 
            (tank_x + tank_base_width_px // 2, tank_y + tank_height_px)
        ], 2
    )

    # Dibujar el líquido
    if current_height > 0:  # Dibujar solo si hay líquido
        liquid_height_px = current_height * scale
        liquid_radius_px = current_radius * screen_scale
        pygame.draw.polygon(
            screen, BLUE, [
                (tank_x + tank_base_width_px // 2 - liquid_radius_px, tank_y + tank_height_px - liquid_height_px),
                (tank_x + tank_base_width_px // 2 + liquid_radius_px, tank_y + tank_height_px - liquid_height_px),
                (tank_x + tank_base_width_px // 2, tank_y + tank_height_px)
            ]
        )

    # Simular el goteo
    frame_count += 1
    if frame_count % drop_interval == 0:  # Generar una gota cada cierto número de frames
        drop_x = tank_x + tank_base_width_px // 2  # Posición x en la punta del tanque
        drop_y = tank_y + tank_height_px           # Posición y en la punta del tanque
        drops.append([drop_x, drop_y])  # Agregar la gota a la lista

    # Mover y dibujar las gotas
    for drop in drops[:]:  # Iterar sobre una copia para eliminar gotas
        drop[1] += drop_speed  # Mover la gota hacia abajo
        pygame.draw.circle(screen, (0, 100, 255), (int(drop[0]), int(drop[1])), drop_radius)  # Dibujar la gota

        # Eliminar la gota si sale de la pantalla
        if drop[1] > screen_height:
            drops.remove(drop)

    # Dibujar el cronómetro
    timer_text = font.render(f"Tiempo: {min(current_time, max_time):.2f} s", True, BLACK)
    screen.blit(timer_text, (screen_width - 200, screen_height - 50))  # Posición en la esquina inferior derecha

    # Calcular el volumen actual
    current_radius = (R / H) * current_height  # Radio en función de h(t)
    current_volume = (1 / 3) * np.pi * (current_radius**2) * current_height**2  # Fórmula del volumen

    # Dibujar el volumen restante
    volume_text = font.render(f"Volumen restante: {current_volume:.2f} m³", True, BLACK)
    screen.blit(volume_text, (screen_width - 300, screen_height - 100))  # Posición arriba del cronómetro

    # Evento de salida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

    # Mantener la pantalla abierta después de que la animación termine
while True:
    screen.fill((255, 200, 61))

    # Dibujar el tanque vacío (relleno)
    pygame.draw.polygon(
        screen, (173, 216, 230), [  # Azul celeste claro
            (tank_x, tank_y), 
            (tank_x + tank_base_width_px, tank_y), 
            (tank_x + tank_base_width_px // 2, tank_y + tank_height_px)
        ]
    )

    # Dibujar el contorno del tanque
    pygame.draw.polygon(
        screen, BLACK, [
            (tank_x, tank_y), 
            (tank_x + tank_base_width_px, tank_y), 
            (tank_x + tank_base_width_px // 2, tank_y + tank_height_px)
        ], 2
    )

    # Dibujar el cronómetro final
    final_timer_text = font.render(f"Tiempo final: {max_time:.2f} s", True, BLACK)
    screen.blit(final_timer_text, (screen_width - 300, screen_height - 50))

    # Evento de salida para salir manualmente
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.flip()

pygame.quit()