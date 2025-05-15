import numpy as np
import pygame
import time
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

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
    def submit():
        try:
            global R, H, h0, a, c, g

            R = float(entry_R.get())
            H = float(entry_H.get())
            h0 = float(entry_h0.get())
            a = float(entry_a.get())
            c = float(entry_c.get())
            g = float(entry_g.get())

            if h0 > H:
                tk.messagebox.showerror("Error", f"Altura inicial (h0) debe ser menor o igual a la altura del tanque (H = {H} m).")
                return

            root.destroy()  # Cierra la ventana si los valores son válidos
        except ValueError:
            tk.messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

    root = tk.Tk()
    root.title("Parámetros del Tanque")

    # Configuración de la ventana principal
    root.configure(bg="#2e2e2e")
    root.geometry("450x380")  # Ajustar el tamaño para mejorar el espacio
    root.resizable(False, False)

    # Estilo de fuentes
    label_font = ("Helvetica", 10, "bold")
    entry_font = ("Helvetica", 12)

    # Etiquetas y campos de entrada
    tk.Label(root, text="Radio de la base del tanque (R) en metros:", fg="white", bg="#2e2e2e", font=label_font).grid(row=0, column=0, padx=5, pady=10, sticky="e")
    entry_R = tk.Entry(root, font=entry_font, bg="#424242", fg="white", insertbackground="white", bd=0, relief="sunken")
    entry_R.grid(row=0, column=1, padx=(20, 40), pady=10)  # Aumentar el espacio a la derecha

    tk.Label(root, text="Altura total del tanque (H) en metros:", fg="white", bg="#2e2e2e", font=label_font).grid(row=1, column=0, padx=5, pady=10, sticky="e")
    entry_H = tk.Entry(root, font=entry_font, bg="#424242", fg="white", insertbackground="white", bd=0, relief="sunken")
    entry_H.grid(row=1, column=1, padx=(20, 40), pady=10)  # Aumentar el espacio a la derecha

    tk.Label(root, text="Altura inicial del líquido (h₀) en metros:", fg="white", bg="#2e2e2e", font=label_font).grid(row=2, column=0, padx=5, pady=10, sticky="e")
    entry_h0 = tk.Entry(root, font=entry_font, bg="#424242", fg="white", insertbackground="white", bd=0, relief="sunken")
    entry_h0.grid(row=2, column=1, padx=(20, 40), pady=10)  # Aumentar el espacio a la derecha

    tk.Label(root, text="Área de salida (a) en m²:", fg="white", bg="#2e2e2e", font=label_font).grid(row=3, column=0, padx=5, pady=10, sticky="e")
    entry_a = tk.Entry(root, font=entry_font, bg="#424242", fg="white", insertbackground="white", bd=0, relief="sunken")
    entry_a.grid(row=3, column=1, padx=(20, 40), pady=10)  # Aumentar el espacio a la derecha

    tk.Label(root, text="Coeficiente de descarga (c):", fg="white", bg="#2e2e2e", font=label_font).grid(row=4, column=0, padx=5, pady=10, sticky="e")
    entry_c = tk.Entry(root, font=entry_font, bg="#424242", fg="white", insertbackground="white", bd=0, relief="sunken")
    entry_c.grid(row=4, column=1, padx=(20, 40), pady=10)  # Aumentar el espacio a la derecha

    tk.Label(root, text="Gravedad (g) en m/s²:", fg="white", bg="#2e2e2e", font=label_font).grid(row=5, column=0, padx=5, pady=10, sticky="e")
    entry_g = tk.Entry(root, font=entry_font, bg="#424242", fg="white", insertbackground="white", bd=0, relief="sunken")
    entry_g.grid(row=5, column=1, padx=(20, 40), pady=10)  # Aumentar el espacio a la derecha

    # Botón de envío
    tk.Button(root, text="Aceptar", command=submit, font=("Helvetica", 12, "bold"), bg="#5a57a7", fg="white", relief="raised", padx=20, pady=5).grid(row=6, column=0, columnspan=2, pady=15)

    root.mainloop()

    return R, H, h0, a, c, g

# Función principal para ejecutar la simulación
def run_simulation():
    global R, H, h0, a, c, g
    R, H, h0, a, c, g = get_user_parameters()

    # Tiempo máximo para vaciar el tanque
    max_time = calculate_emptying_time(h0, a, c, H, R, g)

    # Configuración de Pygame
    pygame.init()

    # Información de la pantalla completa
    info = pygame.display.Info()
    screen_width = info.current_w
    screen_height = info.current_h

    # Dimensiones del tanque
    screen_scale = 50  # Factor de escala inicial
    tank_height_px = H * screen_scale
    tank_base_width_px = 2 * R * screen_scale

    # Ajustar escala para que el tanque quepa en la ventana
    scale_factor = min((screen_height - 200) / tank_height_px, (screen_width - 200) / tank_base_width_px, 1)
    tank_height_px *= scale_factor
    tank_base_width_px *= scale_factor
    screen_scale *= scale_factor

    # Crear ventana fija al tamaño completo de la pantalla
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("Vaciado de Tanque Cónico")
    clock = pygame.time.Clock()

    WHITE = (255, 255, 255)
    BLUE = (0, 100, 255)
    BLACK = (0, 0, 0)
    font = pygame.font.Font(None, 36)

    tank_x = (screen_width - tank_base_width_px) // 2
    tank_y = (screen_height - tank_height_px) // 2
    scale = tank_height_px / H

    drops = []
    drop_radius = 5
    drop_speed = 3
    drop_interval = 5
    frame_count = 0
    start_time = time.time()
    running = True

    while running:
        screen.fill((255, 200, 61))
        current_time = time.time() - start_time
        current_height = liquid_height(h0, a, c, H, R, g, current_time)

        if current_time >= max_time or current_height <= 1e-3:
            current_height = 0
            running = False

        current_radius = (tank_base_width_px / (tank_height_px * 2)) * current_height

        pygame.draw.polygon(
            screen, (173, 216, 230),
            [(tank_x, tank_y), (tank_x + tank_base_width_px, tank_y), (tank_x + tank_base_width_px // 2, tank_y + tank_height_px)]
        )
        pygame.draw.polygon(
            screen, BLACK,
            [(tank_x, tank_y), (tank_x + tank_base_width_px, tank_y), (tank_x + tank_base_width_px // 2, tank_y + tank_height_px)], 2
        )

        if current_height > 0:
            liquid_height_px = current_height * scale
            liquid_radius_px = current_radius * screen_scale
            pygame.draw.polygon(
                screen, BLUE,
                [(tank_x + tank_base_width_px // 2 - liquid_radius_px, tank_y + tank_height_px - liquid_height_px),
                 (tank_x + tank_base_width_px // 2 + liquid_radius_px, tank_y + tank_height_px - liquid_height_px),
                 (tank_x + tank_base_width_px // 2, tank_y + tank_height_px)]
            )

        frame_count += 1
        if frame_count % drop_interval == 0:
            drops.append([tank_x + tank_base_width_px // 2, tank_y + tank_height_px])

        for drop in drops[:]:
            drop[1] += drop_speed
            pygame.draw.circle(screen, (0, 100, 255), (int(drop[0]), int(drop[1])), drop_radius)
            if drop[1] > screen_height:
                drops.remove(drop)

        # Mostrar tiempo y volumen en la esquina inferior izquierda
        timer_text = font.render(f"Tiempo: {min(current_time, max_time):.2f} s", True, BLACK)
        volume_text = font.render(f"Volumen: {liquid_height(h0, a, c, H, R, g, current_time):.2f} m³", True, BLACK)
        screen.blit(timer_text, (10, screen_height - 90))
        screen.blit(volume_text, (10, screen_height - 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.flip()
        clock.tick(60)

    # Pantalla final con botón de reinicio
    while True:
        screen.fill((255, 200, 61))
        pygame.draw.polygon(
            screen, (173, 216, 230),
            [(tank_x, tank_y), (tank_x + tank_base_width_px, tank_y), (tank_x + tank_base_width_px // 2, tank_y + tank_height_px)]
        )
        pygame.draw.polygon(
            screen, BLACK,
            [(tank_x, tank_y), (tank_x + tank_base_width_px, tank_y), (tank_x + tank_base_width_px // 2, tank_y + tank_height_px)], 2
        )

        final_timer_text = font.render(f"Tiempo: {max_time:.2f} s", True, BLACK)
        final_volume_text = font.render(f"Volumen: 0 m³", True, BLACK)
        screen.blit(final_timer_text, (10, screen_height - 90))
        screen.blit(final_volume_text, (10, screen_height - 50))

        button_color = (255, 128, 0)
        button_rect = pygame.Rect(screen_width - 150, screen_height - 60, 140, 50)
        pygame.draw.rect(screen, button_color, button_rect)
        button_text = font.render("Reiniciar", True, WHITE)
        screen.blit(button_text, (screen_width - 140, screen_height - 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    run_simulation()

        pygame.display.flip()

# Ejecutar la simulación
run_simulation()