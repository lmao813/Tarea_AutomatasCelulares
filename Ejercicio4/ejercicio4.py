import numpy as np
import matplotlib.pyplot as plt

# Parámetros
n_cells = 101  # número de celdas
n_steps = 50   # número de generaciones
rule_number = 30  # Rule 30 como ejemplo

# Convertir regla a bits
rule = np.array([int(x) for x in np.binary_repr(rule_number, width=8)], dtype=np.int8)

# Inicializar matriz
cells = np.zeros((n_steps, n_cells), dtype=np.int8)
cells[0, n_cells // 2] = 1  # Semilla inicial en el centro

# Evolución del AC
for i in range(1, n_steps):
    for j in range(1, n_cells - 1):
        pattern = cells[i-1, j-1]*4 + cells[i-1, j]*2 + cells[i-1, j+1]
        cells[i, j] = rule[7 - pattern]

# Mostrar
plt.figure(figsize=(10,6))
plt.imshow(cells, cmap="binary")
plt.title(f"Autómata Celular 1D - Regla {rule_number}")
plt.axis('off')
plt.show()
