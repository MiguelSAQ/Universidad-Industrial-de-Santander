import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Función para actualizar la placa en CPU
def update_plate_cpu(u_old, u_new, alpha, dt, dx, dy, Nx, Ny):
    for i in range(1, Nx - 1):
        for j in range(1, Ny - 1):
            u_new[i, j] = u_old[i, j] + alpha * dt * (
                (u_old[i + 1, j] - 2 * u_old[i, j] + u_old[i - 1, j]) / dx**2 +
                (u_old[i, j + 1] - 2 * u_old[i, j] + u_old[i, j - 1]) / dy**2
            )

# Inicialización de parámetros
Lx, Ly = 1.0, 1.0          # Dimensiones de la placa (en metros)
Nx, Ny = 128, 128          # Número de puntos en x e y (tamaño de la placa)
dx, dy = Lx / Nx, Ly / Ny  # Tamaño de las celdas
alpha = 0.01               # Coeficiente de conductividad térmica
dt = 0.001                 # Paso temporal
T = 10                     # Tiempo total de la simulación
timesteps = int(T / dt)    # Número de pasos

# Condiciones iniciales
u_old = np.zeros((Nx, Ny), dtype=np.float32)    # Temperatura inicial (0°C en toda la placa)
u_old[Nx//4:Nx//2, Ny//4:Ny//2] = 100           # Región inicial caliente (100°C)
u_new = np.zeros_like(u_old)                    # Temperatura nueva

# Configuración de la animación
fig, ax = plt.subplots()
im = ax.imshow(u_old, extent=[0, Lx, 0, Ly], origin='lower', cmap='hot', interpolation='nearest', vmin=0, vmax=100)
fig.colorbar(im, label="Temperatura (°C)")
ax.set_title("Distribución de Calor")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")

# Añadir contador de tiempo
time_text = ax.text(0.02, 0.93, '', transform=ax.transAxes, color='white', fontsize=12, bbox=dict(facecolor='black', alpha=0.7))

# Función de actualización para la animación
def animate(step):
    global u_old, u_new
    update_plate_cpu(u_old, u_new, alpha, dt, dx, dy, Nx, Ny)
    u_old, u_new = u_new, u_old
    im.set_array(u_old)
    time_text.set_text(f"Tiempo: {step * dt:.3f} s")  # Actualizar tiempo
    return [im, time_text]

# Crear la animación
ani = FuncAnimation(fig, animate, frames=timesteps, interval=1, blit=True)

# Mostrar la animación
plt.show()