def plot_grid(grid, step):
    cmap = plt.cm.get_cmap('viridis', 3)
    plt.imshow(grid, cmap=cmap)
    plt.title(f"Paso {step}")
    plt.axis('off')
    plt.show()

for step in range(steps):
    new_grid = grid.copy()
    for i in range(size):
        for j in range(size):
            if grid[i, j] == 0:  # Susceptible
                neighbors = grid[max(0,i-1):min(size,i+2), max(0,j-1):min(size,j+2)]
                if 1 in neighbors and np.random.rand() < p_infect:
                    new_grid[i, j] = 1
            elif grid[i, j] == 1:  # Infectado
                if np.random.rand() < p_recover:
                    new_grid[i, j] = 2
    grid = new_grid
    plot_grid(grid, step)
