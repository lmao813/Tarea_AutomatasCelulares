import numpy as np
import matplotlib.pyplot as plt

def automata_celular_1d(size=100, steps=50, rule=30):
    grid = np.zeros((steps, size), dtype=int)
    grid[0, size//2] = 1  # Celda inicial

    # Regla en binario
    rule_bin = np.array([int(x) for x in np.binary_repr(rule, width=8)], dtype=int)
    patterns = np.array([[1,1,1],[1,1,0],[1,0,1],[1,0,0],
                         [0,1,1],[0,1,0],[0,0,1],[0,0,0]])

    for i in range(1, steps):
        for j in range(1, size-1):
            neighborhood = grid[i-1, j-1:j+2]
            for idx, pattern in enumerate(patterns):
                if np.array_equal(neighborhood, pattern):
                    grid[i,j] = rule_bin[idx]
                    break

    plt.imshow(grid, cmap="binary")
    plt.title(f"Autómata Celular 1D - Regla {rule}")
    plt.show()

automata_celular_1d()
