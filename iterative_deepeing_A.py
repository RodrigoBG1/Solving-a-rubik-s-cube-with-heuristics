from CubeMovements import Cube_movements
from NodeCube2 import Cube
import numpy as np
from copy import deepcopy
from collections import deque
from bitarray import bitarray

class IterativeDeepeningSearch:
    def __init__(self, start_cube):
        self.cube = start_cube
        self.goal_cube = [[[k for i in range(3)] for j in range(3)] for k in range(6)]
        self.visited = set()
        self.diccionario = {0:'000001', 1:'000010', 2:'000100', 3:'001000', 4:'010000', 5:'100000'}
        self.moves = ['R', 'r', 'L', 'l', 'U', 'u', 'N', 'n', 'F', 'f', 'D', 'd']
                    
    def IterativeDeepeningSearch(self):
        for depth in range(100):  # Assuming a maximum depth of 100 moves
            result = self.depth_limited_search(depth)
            if result is not None:
                self.print_solution(result)
                return
        print("Solution not found within the maximum depth.")

    def depth_limited_search(self, depth):
        source = Cube()
        target = Cube()
        source.cube = self.cube
        target.cube = self.goal_cube

        target.cube_bits = self.convert_to_bit(target.cube)

        source.path.append(source)
        source.cube_bits = self.convert_to_bit(source.cube)

        self.visited.clear()
        self.visited.add(str(source.cube_bits))

        stack = [(source, 0)]  # (node, current_depth)

        while stack:
            current_node, current_depth = stack.pop()

            if current_node.cube_bits == target.cube_bits:
                return current_node

            if current_depth < depth:
                for i in range(len(self.moves)):
                    c = Cube_movements(deepcopy(current_node.cube))
                    new_cube = c.Movements(self.moves[i])
                    new_cube_bits = self.convert_to_bit(new_cube)

                    if not self.is_visited(new_cube_bits):
                        next_cube = Cube()
                        next_cube.cube_bits = new_cube_bits
                        next_cube.cube = new_cube
                        next_cube.move = self.moves[i]
                        next_cube.path.extend(current_node.path)
                        next_cube.path.append(next_cube)

                        self.visited.add(str(next_cube.cube_bits))
                        stack.append((next_cube, current_depth + 1))

        return None

    def convert_to_bit(self, cube):
        bit_string = bitarray()
        for k in range(6):
            for i in range(3):
                for j in range(3):
                    bit_string.extend(self.diccionario[cube[k][i][j]])
        return bit_string

    def is_visited(self, bit_string):
        bit_string = int(bit_string.to01(), 2)
        if bit_string in self.visited:
            return True
        else:
            return False

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

cube = [[[k for i in range(3)] for j in range(3)] for k in range(6)]
c = Cube_movements(cube)
start_cube = c.shuffle(6)
ids_solver = IterativeDeepeningSearch(start_cube)
solution_moves = ids_solver.IterativeDeepeningSearch()