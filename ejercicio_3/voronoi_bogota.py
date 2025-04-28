import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

# Coordenadas simuladas de colegios y droguerías en Bogotá
puntos = np.random.rand(15, 2)

# Crear diagrama de Voronoi
vor = Voronoi(puntos)

fig = voronoi_plot_2d(vor)
plt.title("Diagrama de Voronoi - Bogotá (simulado)")
plt.show()
