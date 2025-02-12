import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numba import cuda, float32
import time

# Definir kernel de CUDA para actualizar la placa usando memoria compartida
@cuda.jit
def update_plate_cuda_shared(u_old, u_new, alpha, dt, dx, dy, Nx, Ny):
    shared = cuda.shared.array((34, 34), dtype=float32)  # Bloque + bordes
    tx, ty = cuda.threadIdx.x, cuda.threadIdx.y
    bx, by = cuda.blockIdx.x, cuda.blockIdx.y
    bw, bh = cuda.blockDim.x, cuda.blockDim.y

    i, j = bx * bw + tx, by * bh + ty

    if i < Nx and j < Ny:
        shared[tx + 1, ty + 1] = u_old[i, j]
        if tx == 0 and i > 0:  
            shared[0, ty + 1] = u_old[i - 1, j]
        if ty == 0 and j > 0:  
            shared[tx + 1, 0] = u_old[i, j - 1]
        if tx == bw - 1 and i < Nx - 1:  
            shared[tx + 2, ty + 1] = u_old[i + 1, j]
        if ty == bh - 1 and j < Ny - 1:  
            shared[tx + 1, ty + 2] = u_old[i, j + 1]

    cuda.syncthreads()

    if 1 <= i < Nx - 1 and 1 <= j < Ny - 1:
        u_new[i, j] = shared[tx + 1, ty + 1] + alpha * dt * (
            (shared[tx + 2, ty + 1] - 2 * shared[tx + 1, ty + 1] + shared[tx, ty + 1]) / dx**2 +
            (shared[tx + 1, ty + 2] - 2 * shared[tx + 1, ty + 1] + shared[tx + 1, ty]) / dy**2)

# Inicialización de parámetros
Lx, Ly = 1.0, 1.0          
Nx, Ny = 128, 128          
dx, dy = Lx / Nx, Ly / Ny  
alpha = 0.01               
dt = 0.001                 
T = 0.1                    
timesteps = int(T / dt)    

u_host = np.zeros((Nx, Ny), dtype=np.float32)    
u_host[Nx//4:Nx//2, Ny//4:Ny//2] = 100           

u_old = cuda.to_device(u_host)          
u_new = cuda.device_array_like(u_old)   

threads_per_block = (32, 32)             
blocks_x = 32 
blocks_y = 32 
blocks_per_grid = (blocks_x, blocks_y)   

# Configuración de la animación
fig, ax = plt.subplots()
im = ax.imshow(u_host, extent=[0, Lx, 0, Ly], origin='lower', cmap='hot', interpolation='nearest', vmin=0, vmax=100)
fig.colorbar(im, label="Temperatura (°C)")
time_text = ax.text(0.02, 0.93, '', transform=ax.transAxes, color='white', fontsize=12, bbox=dict(facecolor='black', alpha=0.7))
ax.set_title("Distribución de Calor")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")

# Función para actualizar la animación
def animate(step):
    global u_old, u_new
    update_plate_cuda_shared[blocks_per_grid, threads_per_block](
        u_old, u_new, alpha, dt, dx, dy, Nx, Ny
    )
    cuda.synchronize()
    u_old, u_new = u_new, u_old

    u_host = u_old.copy_to_host()
    im.set_array(u_host)
    time_text.set_text(f"Tiempo: {step * dt:.3f} s")
    return [im, time_text]

ani = FuncAnimation(fig, animate, frames=timesteps // 50, interval=100, blit=True)

plt.show()