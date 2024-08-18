from CubeMovements import Cube_movements
from NodeCube2 import Cube
import numpy as np
from copy import deepcopy
from collections import deque
from bitarray import bitarray
import time

class BreathFirstSearch:
    def __init__(self, start_cube):
        # Inicializa el cubo de inicio, el cubo objetivo, el conjunto de visitados y los movimientos posibles
        self.cube = start_cube
        self.goal_cube = [[[k for i in range(3)] for j in range(3)] for k in range(6)]
        self.visited = set()
        self.moves = ['R', 'r', 'L', 'l', 'U', 'u', 'N', 'n', 'F', 'f', 'D', 'd']
                    
    def BreathFirstSearch(self):
        queue = deque()  # Crea una cola para el algoritmo de búsqueda

        source = Cube()  # Crea un nodo de origen
        target = Cube()  # Crea un nodo objetivo
        source.cube = self.cube  # Asigna el cubo de inicio al nodo de origen
        target.cube = self.goal_cube  # Asigna el cubo objetivo al nodo objetivo

        target.cube_bits = self.convert_to_bit(target.cube)  # Convierte el cubo objetivo a bits

        source.path.append(source)  # Agrega el nodo de origen a su propio camino
        source.cube_bits = self.convert_to_bit(source.cube)  # Convierte el cubo de inicio a bits

        self.visited.add(source.cube_bits)  # Agrega el cubo de inicio al conjunto de visitados

        queue.append(source)  # Agrega el nodo de origen a la cola

        while queue:  # Mientras la cola no esté vacía
            current_node = queue.popleft()  # Saca el nodo frontal de la cola

            if current_node.cube_bits == target.cube_bits:  # Si el nodo actual es el objetivo
                self.print_solution(current_node)  # Imprime la solución
                return

            for i in range(len(self.moves)):  # Para cada movimiento posible
                c = Cube_movements(deepcopy(current_node.cube))  # Crea un objeto de movimientos de cubo
                new_cube = c.Movements(self.moves[i])  # Aplica el movimiento al cubo actual
                new_cube_bits = self.convert_to_bit(new_cube)  # Convierte el nuevo cubo a bits

                if new_cube_bits not in self.visited:  # Si el nuevo cubo no ha sido visitado
                    next_cube = Cube()  # Crea un nuevo nodo
                    next_cube.cube_bits = new_cube_bits  # Asigna los bits del nuevo cubo
                    next_cube.cube = new_cube  # Asigna el nuevo cubo
                    next_cube.move = self.moves[i]  # Asigna el movimiento
                    next_cube.path.extend(current_node.path)  # Copia el camino del nodo actual
                    next_cube.path.append(next_cube)  # Agrega el nuevo nodo al camino
                    
                    self.visited.add(next_cube.cube_bits)  # Agrega el nuevo cubo al conjunto de visitados
                    queue.append(next_cube)  # Agrega el nuevo nodo a la cola
                    
    def convert_to_bit(self, cube):
        # Convierte el cubo a una representación de bits
        list = [0] * 6
        x = 0
        for k in range(6):
            for i in range(2, -1, -1):
                for j in range(2, -1, -1):
                    x = x << 3 | cube[k][i][j]
            list[k] = x
            x = 0
        return tuple(list)
    
    def is_visited(self, cube_int_tuple):
        return cube_int_tuple in self.visited
        
    def print_solution(self, node):

        for q in range(len(node.path)):
            if node.path[q].move:
                print("Step: ", q)
            if node.path[q].move == 'R':
                print("Rotate the right layer clockwise.")
            elif node.path[q].move == 'r':
                print("Rotate the right layer anti-clockwise.")
            elif node.path[q].move == 'L':
                print("Rotate the left layer clockwise.")
            elif node.path[q].move == 'l':
                print("Rotate the left layer anti-clockwise.")
            elif node.path[q].move == 'U':
                print("Rotate the top layer clockwise.")  
            elif node.path[q].move == 'u':
                print("Rotate the top layer anti-clockwise.")     
            elif node.path[q].move == 'N':
                print("Rotate the bottom layer clockwise.")  
            elif node.path[q].move == 'n':
                print("Rotate the bottom layer anti-clockwise.")
            elif node.path[q].move == 'F':
                print("Rotate the front layer clockwise.")  
            elif node.path[q].move == 'f':
                print("Rotate the front layer anti-clockwise.") 
            elif node.path[q].move == 'D':
                print("Rotate the back layer clockwise.")  
            elif node.path[q].move == 'd':
                print("Rotate the back layer anti-clockwise.")
            if node.path[q].move:
                print("   front          top           bottom           left          right          back")
                for i in range(3):
                    print("-----------    -----------    -----------    -----------    ----------     -----------")
                    for k in range(6):
                        for j in range(3): 
                            print(self.cube[k][i][j], end = " | ")
                            
                        print(end = "   ")
                    print()
                print("\n0 = white |  1 = orange  |     2 = red  |   3 = green  |    4 = blue  |    5 = yellow")
            print()
        print("Cantidad de pasos: ", len(node.path)-1)

# Example usage:
cube = [[[k for i in range(3)] for j in range(3)] for k in range(6)]
c = Cube_movements(cube)
start_cube = c.shuffle(4)
inicio = time.time()
bfs_solver = BreathFirstSearch(start_cube)
solution_moves = bfs_solver.BreathFirstSearch()
fin = time.time()
print("Tiempo transcurrido: ", fin - inicio, "segundos")