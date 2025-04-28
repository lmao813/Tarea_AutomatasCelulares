import random
class Robot:
    def __init__(self):
        self.position = [0, 0]
        self.direction = [1, 0]  # Avanza hacia la derecha
    def detect_obstacle(self):
        # Probabilidad de detectar obstáculo
        return random.random() < 0.2
    def avoid_obstacle(self):
        # Cambiar de dirección (simplemente gira a la izquierda)
        self.direction = [-self.direction[1], self.direction[0]]
    def move(self):
        if self.detect_obstacle():
            print('Obstáculo detectado. Cambiando dirección.')
            self.avoid_obstacle()
        self.position[0] += self.direction[0]
        self.position[1] += self.direction[1]
        print(f'Nueva posición: {self.position}')

robot = Robot()
for _ in range(20):
    robot.move()
