import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

# Droguerías aproximadas en el centro del municipio (coordenadas en escala 100x100)
droguerias = np.array([
    [30, 60],
    [40, 70],
    [50, 60],
    [55, 50],
    [50, 40],
    [45, 30],
    [35, 40],
    [40, 50],
    [60, 60],
    [55, 65]
])

# Simulación densidad poblacional:
# Más población concentrada en el centro, menos en periferia
personas_centro_x = np.random.normal(50, 10, 4000)
personas_centro_y = np.random.normal(50, 10, 4000)

personas_periferia_x = np.random.normal(50, 25, 1000)
personas_periferia_y = np.random.normal(50, 25, 1000)

personas_x = np.concatenate([personas_centro_x, personas_periferia_x])
personas_y = np.concatenate([personas_centro_y, personas_periferia_y])

# Crear diagrama de Voronoi
vor = Voronoi(droguerias)

# Gráfico
plt.figure(figsize=(8,8))
voronoi_plot_2d(vor, show_vertices=False, line_colors='orange', line_width=2, point_size=8)
plt.scatter(droguerias[:,0], droguerias[:,1], c='red', s=50, label='Droguerías')
plt.scatter(personas_x, personas_y, c='blue', s=1, alpha=0.3, label='Habitantes')
plt.title("Cobertura de droguerías en Tocancipá y densidad poblacional simulada")
plt.xlim(0,100)
plt.ylim(0,100)
plt.legend()
plt.show()
