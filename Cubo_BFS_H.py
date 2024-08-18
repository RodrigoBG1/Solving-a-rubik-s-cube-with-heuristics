from NodeCube2 import Cube
from CubeMovements import Cube_movements
from queue import PriorityQueue
from copy import deepcopy
import time

class Heuristics:
    @staticmethod
    #Esta es para saber cuántas caras de cada esquina están mal
    def corners_heuristic(node):
        sum = 0
        for k in range(6):
            if node.cube[k][0][0] != node.cube[k][1][1]:
                sum += 1
            if node.cube[k][0][2] != node.cube[k][1][1]:
                sum += 1
            if node.cube[k][2][0] != node.cube[k][1][1]:
                sum += 1
            if node.cube[k][2][2] != node.cube[k][1][1]:
                sum += 1
        return sum
    
    @staticmethod
    #Esta es para saber cuántas esquinas tiene por al menos una cara mal
    def corners_heuristic_2(node):
        sum = 0
        if node.cube[0][0][0] != node.cube[0][1][1] or node.cube[1][2][0] != node.cube[1][1][1] or node.cube[3][0][2] != node.cube[3][1][1]:
            sum += 1
        if node.cube[0][0][2] != node.cube[0][1][1] or node.cube[1][2][2] != node.cube[1][1][1] or node.cube[4][0][0] != node.cube[4][1][1]:
            sum += 1
        if node.cube[0][2][0] != node.cube[0][1][1] or node.cube[3][2][2] != node.cube[3][1][1] or node.cube[2][0][0] != node.cube[2][1][1]:
            sum += 1
        if node.cube[0][2][2] != node.cube[0][1][1] or node.cube[4][2][0] != node.cube[4][1][1] or node.cube[2][0][2] != node.cube[2][1][1]:
            sum += 1
        if node.cube[5][0][0] != node.cube[5][1][1] or node.cube[4][0][2] != node.cube[4][1][1] or node.cube[1][0][2] != node.cube[1][1][1]:
            sum += 1
        if node.cube[5][0][2] != node.cube[5][1][1] or node.cube[3][0][0] != node.cube[3][1][1] or node.cube[1][0][0] != node.cube[1][1][1]:
            sum += 1
        if node.cube[5][2][0] != node.cube[5][1][1] or node.cube[4][2][2] != node.cube[4][1][1] or node.cube[2][2][2] != node.cube[2][1][1]:
            sum += 1
        if node.cube[5][2][2] != node.cube[5][1][1] or node.cube[3][2][0] != node.cube[3][1][1] or node.cube[2][2][0] != node.cube[2][1][1]:
            sum += 1
        return sum

    #Esta es para saber cuántas caras de cada vértice están mal
    @staticmethod
    def edges_heuristic(node):
        sum = 0
        for k in range(6):
            if node.cube[k][0][1] != node.cube[k][1][1]:
                sum += 1
            if node.cube[k][1][0] != node.cube[k][1][1]:
                sum += 1
            if node.cube[k][1][2] != node.cube[k][1][1]:
                sum += 1
            if node.cube[k][2][1] != node.cube[k][1][1]:
                sum += 1
        return sum
    
    #Esta es para saber cuántos vértices tienen por al menos una cara mal
    @staticmethod
    def edges_heuristic_2(node):
        sum = 0
        if node.cube[0][0][1] != node.cube[0][1][1] or node.cube[1][2][1] != node.cube[1][1][1]:
            sum += 1
        if node.cube[4][0][1] != node.cube[4][1][1] or node.cube[1][1][2] != node.cube[1][1][1]:
            sum += 1
        if node.cube[5][0][1] != node.cube[5][1][1] or node.cube[1][0][1] != node.cube[1][1][1]:
            sum += 1
        if node.cube[3][0][1] != node.cube[3][1][1] or node.cube[1][1][0] != node.cube[1][1][1]:
            sum += 1
        if node.cube[0][1][0] != node.cube[0][1][1] or node.cube[3][1][2] != node.cube[3][1][1]:
            sum += 1
        if node.cube[0][1][2] != node.cube[0][1][1] or node.cube[4][1][0] != node.cube[4][1][1]:
            sum += 1
        if node.cube[5][1][0] != node.cube[5][1][1] or node.cube[4][1][2] != node.cube[4][1][1]:
            sum += 1
        if node.cube[5][1][2] != node.cube[5][1][1] or node.cube[3][1][0] != node.cube[3][1][1]:
            sum += 1
        if node.cube[0][2][1] != node.cube[0][1][1] or node.cube[2][0][1] != node.cube[2][1][1]:
            sum += 1
        if node.cube[4][2][1] != node.cube[4][1][1] or node.cube[2][1][2] != node.cube[2][1][1]:
            sum += 1
        if node.cube[5][2][1] != node.cube[5][1][1] or node.cube[2][2][1] != node.cube[2][1][1]:
            sum += 1
        if node.cube[3][2][1] != node.cube[3][1][1] or node.cube[2][1][0] != node.cube[2][1][1]:
            sum += 1
        return sum

    #Esta es para saber cuántas caras de cada esquina y vértice están mal
    @staticmethod
    def corners_edges_heuristic(node):
        sum = 0
        for k in range(6):
            for i in range(3):
                for j in range(3):
                    if node.cube[k][i][j] != node.cube[k][1][1]:
                        sum += 1
        return sum
    
    #Esta es para saber cuántas esquinas y vértices tienen por al menos una cara mal
    @staticmethod
    def corners_edges_heuristic_2(node):
        sum = 0
        if node.cube[0][0][0] != node.cube[0][1][1] or node.cube[1][2][0] != node.cube[1][1][1] or node.cube[3][0][2] != node.cube[3][1][1]:
            sum += 1
        if node.cube[0][0][2] != node.cube[0][1][1] or node.cube[1][2][2] != node.cube[1][1][1] or node.cube[4][0][0] != node.cube[4][1][1]:
            sum += 1
        if node.cube[0][2][0] != node.cube[0][1][1] or node.cube[3][2][2] != node.cube[3][1][1] or node.cube[2][0][0] != node.cube[2][1][1]:
            sum += 1
        if node.cube[0][2][2] != node.cube[0][1][1] or node.cube[4][2][0] != node.cube[4][1][1] or node.cube[2][0][2] != node.cube[2][1][1]:
            sum += 1
        if node.cube[5][0][0] != node.cube[5][1][1] or node.cube[4][0][2] != node.cube[4][1][1] or node.cube[1][0][2] != node.cube[1][1][1]:
            sum += 1
        if node.cube[5][0][2] != node.cube[5][1][1] or node.cube[3][0][0] != node.cube[3][1][1] or node.cube[1][0][0] != node.cube[1][1][1]:
            sum += 1
        if node.cube[5][2][0] != node.cube[5][1][1] or node.cube[4][2][2] != node.cube[4][1][1] or node.cube[2][2][2] != node.cube[2][1][1]:
            sum += 1
        if node.cube[5][2][2] != node.cube[5][1][1] or node.cube[3][2][0] != node.cube[3][1][1] or node.cube[2][2][0] != node.cube[2][1][1]:
            sum += 1
        if node.cube[0][0][1] != node.cube[0][1][1] or node.cube[1][2][1] != node.cube[1][1][1]:
            sum += 1
        if node.cube[4][0][1] != node.cube[4][1][1] or node.cube[1][1][2] != node.cube[1][1][1]:
            sum += 1
        if node.cube[5][0][1] != node.cube[5][1][1] or node.cube[1][0][1] != node.cube[1][1][1]:
            sum += 1
        if node.cube[3][0][1] != node.cube[3][1][1] or node.cube[1][1][0] != node.cube[1][1][1]:
            sum += 1
        if node.cube[0][1][0] != node.cube[0][1][1] or node.cube[3][1][2] != node.cube[3][1][1]:
            sum += 1
        if node.cube[0][1][2] != node.cube[0][1][1] or node.cube[4][1][0] != node.cube[4][1][1]:
            sum += 1
        if node.cube[5][1][0] != node.cube[5][1][1] or node.cube[4][1][2] != node.cube[4][1][1]:
            sum += 1
        if node.cube[5][1][2] != node.cube[5][1][1] or node.cube[3][1][0] != node.cube[3][1][1]:
            sum += 1
        if node.cube[0][2][1] != node.cube[0][1][1] or node.cube[2][0][1] != node.cube[2][1][1]:
            sum += 1
        if node.cube[4][2][1] != node.cube[4][1][1] or node.cube[2][1][2] != node.cube[2][1][1]:
            sum += 1
        if node.cube[5][2][1] != node.cube[5][1][1] or node.cube[2][2][1] != node.cube[2][1][1]:
            sum += 1
        if node.cube[3][2][1] != node.cube[3][1][1] or node.cube[2][1][0] != node.cube[2][1][1]:
            sum += 1
        return sum
    
    #Ve los movimientos a futuro y cuenta en cada movimiento cuantos colores están incorrectos y regresa el minimo de todos los movimientos
    @staticmethod
    def future_heuristics(node):
        minimum = 54
        move_12 = ['R', 'r', #Right
                    'L', 'l', #Left
                    'U', 'u', #Up
                    'N', 'n', #Down
                    'F', 'f', #Front
                    'D', 'd'] #Back
        for q in range(len(move_12)):
            sum = 0
            obj1 = Cube_movements(deepcopy(node.cube))
            new_cube = obj1.Movements(move_12[q])
            for k in range(6):
                for i in range(3):
                    for j in range(3):
                        if new_cube[k][i][j] != new_cube[k][1][1]:
                            sum += 1
            minimum = min(sum, minimum)
        return minimum

    #Ve los movimientos a futuro y cuenta cuántas esquinas tienen por al menos una cara mal y regresa el minimo de todos los movimientos
    @staticmethod
    def future_heuristics_corners_2(node):
        minimum = 54
        move_12 = ['R', 'r', #Right
                    'L', 'l', #Left
                    'U', 'u', #Up
                    'N', 'n', #Down
                    'F', 'f', #Front
                    'D', 'd'] #Back
        for q in range(len(move_12)):
            sum = 0
            obj1 = Cube_movements(deepcopy(node.cube))
            new_cube = obj1.Movements(move_12[q])
            if new_cube[0][0][0] != new_cube[0][1][1] or new_cube[1][2][0] != new_cube[1][1][1] or new_cube[3][0][2] != new_cube[3][1][1]:
                sum += 1
            if new_cube[0][0][2] != new_cube[0][1][1] or new_cube[1][2][2] != new_cube[1][1][1] or new_cube[4][0][0] != new_cube[4][1][1]:
                sum += 1
            if new_cube[0][2][0] != new_cube[0][1][1] or new_cube[3][2][2] != new_cube[3][1][1] or new_cube[2][0][0] != new_cube[2][1][1]:
                sum += 1
            if new_cube[0][2][2] != new_cube[0][1][1] or new_cube[4][2][0] != new_cube[4][1][1] or new_cube[2][0][2] != new_cube[2][1][1]:
                sum += 1
            if new_cube[5][0][0] != new_cube[5][1][1] or new_cube[4][0][2] != new_cube[4][1][1] or new_cube[1][0][2] != new_cube[1][1][1]:
                sum += 1
            if new_cube[5][0][2] != new_cube[5][1][1] or new_cube[3][0][0] != new_cube[3][1][1] or new_cube[1][0][0] != new_cube[1][1][1]:
                sum += 1
            if new_cube[5][2][0] != new_cube[5][1][1] or new_cube[4][2][2] != new_cube[4][1][1] or new_cube[2][2][2] != new_cube[2][1][1]:
                sum += 1
            if new_cube[5][2][2] != new_cube[5][1][1] or new_cube[3][2][0] != new_cube[3][1][1] or new_cube[2][2][0] != new_cube[2][1][1]:
                sum += 1
            minimum = min(sum, minimum)
        return minimum

    #Ve los movimientos a futuro y cuenta cuántos vértices tienen por al menos una cara mal y regresa el minimo de todos los movimientos
    @staticmethod
    def future_heuristics_edges_2(node):
        minimum = 54
        move_12 = ['R', 'r', #Right
                    'L', 'l', #Left
                    'U', 'u', #Up
                    'N', 'n', #Down
                    'F', 'f', #Front
                    'D', 'd'] #Back
        for q in range(len(move_12)):
            sum = 0
            obj1 = Cube_movements(deepcopy(node.cube))
            new_cube = obj1.Movements(move_12[q])
            if new_cube[0][0][1] != new_cube[0][1][1] or new_cube[1][2][1] != new_cube[1][1][1]:
                sum += 1
            if new_cube[4][0][1] != new_cube[4][1][1] or new_cube[1][1][2] != new_cube[1][1][1]:
                sum += 1
            if new_cube[5][0][1] != new_cube[5][1][1] or new_cube[1][0][1] != new_cube[1][1][1]:
                sum += 1
            if new_cube[3][0][1] != new_cube[3][1][1] or new_cube[1][1][0] != new_cube[1][1][1]:
                sum += 1
            if new_cube[0][1][0] != new_cube[0][1][1] or new_cube[3][1][2] != new_cube[3][1][1]:
                sum += 1
            if new_cube[0][1][2] != new_cube[0][1][1] or new_cube[4][1][0] != new_cube[4][1][1]:
                sum += 1
            if new_cube[5][1][0] != new_cube[5][1][1] or new_cube[4][1][2] != new_cube[4][1][1]:
                sum += 1
            if new_cube[5][1][2] != new_cube[5][1][1] or new_cube[3][1][0] != new_cube[3][1][1]:
                sum += 1
            if new_cube[0][2][1] != new_cube[0][1][1] or new_cube[2][0][1] != new_cube[2][1][1]:
                sum += 1
            if new_cube[4][2][1] != new_cube[4][1][1] or new_cube[2][1][2] != new_cube[2][1][1]:
                sum += 1
            if new_cube[5][2][1] != new_cube[5][1][1] or new_cube[2][2][1] != new_cube[2][1][1]:
                sum += 1
            if new_cube[3][2][1] != new_cube[3][1][1] or new_cube[2][1][0] != new_cube[2][1][1]:
                sum += 1
            minimum = min(sum, minimum)
        return minimum

    #Ve los movimientos a futuro y cuenta cuántas esquinas y vértices tienen por al menos una cara mal y regresa el minimo de todos los movimientos
    @staticmethod
    def future_heuristics_corners_edges_2(node):
        minimum = 54
        move_12 = ['R', 'r', #Right
                    'L', 'l', #Left
                    'U', 'u', #Up
                    'N', 'n', #Down
                    'F', 'f', #Front
                    'D', 'd'] #Back
        for q in range(len(move_12)):
            sum = 0
            obj1 = Cube_movements(deepcopy(node.cube))
            new_cube = obj1.Movements(move_12[q])
            if new_cube[0][0][0] != new_cube[0][1][1] or new_cube[1][2][0] != new_cube[1][1][1] or new_cube[3][0][2] != new_cube[3][1][1]:
                sum += 1
            if new_cube[0][0][2] != new_cube[0][1][1] or new_cube[1][2][2] != new_cube[1][1][1] or new_cube[4][0][0] != new_cube[4][1][1]:
                sum += 1
            if new_cube[0][2][0] != new_cube[0][1][1] or new_cube[3][2][2] != new_cube[3][1][1] or new_cube[2][0][0] != new_cube[2][1][1]:
                sum += 1
            if new_cube[0][2][2] != new_cube[0][1][1] or new_cube[4][2][0] != new_cube[4][1][1] or new_cube[2][0][2] != new_cube[2][1][1]:
                sum += 1
            if new_cube[5][0][0] != new_cube[5][1][1] or new_cube[4][0][2] != new_cube[4][1][1] or new_cube[1][0][2] != new_cube[1][1][1]:
                sum += 1
            if new_cube[5][0][2] != new_cube[5][1][1] or new_cube[3][0][0] != new_cube[3][1][1] or new_cube[1][0][0] != new_cube[1][1][1]:
                sum += 1
            if new_cube[5][2][0] != new_cube[5][1][1] or new_cube[4][2][2] != new_cube[4][1][1] or new_cube[2][2][2] != new_cube[2][1][1]:
                sum += 1
            if new_cube[5][2][2] != new_cube[5][1][1] or new_cube[3][2][0] != new_cube[3][1][1] or new_cube[2][2][0] != new_cube[2][1][1]:
                sum += 1
            if new_cube[0][0][1] != new_cube[0][1][1] or new_cube[1][2][1] != new_cube[1][1][1]:
                sum += 1
            if new_cube[4][0][1] != new_cube[4][1][1] or new_cube[1][1][2] != new_cube[1][1][1]:
                sum += 1
            if new_cube[5][0][1] != new_cube[5][1][1] or new_cube[1][0][1] != new_cube[1][1][1]:
                sum += 1
            if new_cube[3][0][1] != new_cube[3][1][1] or new_cube[1][1][0] != new_cube[1][1][1]:
                sum += 1
            if new_cube[0][1][0] != new_cube[0][1][1] or new_cube[3][1][2] != new_cube[3][1][1]:
                sum += 1
            if new_cube[0][1][2] != new_cube[0][1][1] or new_cube[4][1][0] != new_cube[4][1][1]:
                sum += 1
            if new_cube[5][1][0] != new_cube[5][1][1] or new_cube[4][1][2] != new_cube[4][1][1]:
                sum += 1
            if new_cube[5][1][2] != new_cube[5][1][1] or new_cube[3][1][0] != new_cube[3][1][1]:
                sum += 1
            if new_cube[0][2][1] != new_cube[0][1][1] or new_cube[2][0][1] != new_cube[2][1][1]:
                sum += 1
            if new_cube[4][2][1] != new_cube[4][1][1] or new_cube[2][1][2] != new_cube[2][1][1]:
                sum += 1
            if new_cube[5][2][1] != new_cube[5][1][1] or new_cube[2][2][1] != new_cube[2][1][1]:
                sum += 1
            if new_cube[3][2][1] != new_cube[3][1][1] or new_cube[2][1][0] != new_cube[2][1][1]:
                sum += 1
            minimum = min(sum, minimum)
        return minimum
    #Calcula la distancia entre cada esquina (y arista) y la posición en la debería encontrarse
    @staticmethod
    def manhattan_distance_3d(node):
        distance = 0
        tuple_of_corners_colors = [('013',1,3,3), ('014',3,3,3), ('023',1,1,3), ('024',3,1,3), ('145',3,3,1), ('135',1,3,1), ('245',3,1,1), ('235'),1,1,1]
        tuple_of_corners = [(''.join(sorted(str(node.cube[0][0][0]) + str(node.cube[1][2][0]) + str(node.cube[3][0][2]))), 1, 3, 3),
                            (''.join(sorted(str(node.cube[0][0][2]) + str(node.cube[1][2][2]) + str(node.cube[4][0][0]))), 3, 3, 3),
                            (''.join(sorted(str(node.cube[0][2][0]) + str(node.cube[2][0][0]) + str(node.cube[3][2][2]))), 1, 1, 3),
                            (''.join(sorted(str(node.cube[0][2][2]) + str(node.cube[2][0][2]) + str(node.cube[4][2][0]))), 3, 1, 3),
                            (''.join(sorted(str(node.cube[5][0][0]) + str(node.cube[1][0][2]) + str(node.cube[4][0][2]))), 3, 3, 1),
                            (''.join(sorted(str(node.cube[5][0][2]) + str(node.cube[1][0][0]) + str(node.cube[3][0][0]))), 1, 3, 1),
                            (''.join(sorted(str(node.cube[5][2][0]) + str(node.cube[2][2][2]) + str(node.cube[4][2][2]))), 3, 1, 1),
                            (''.join(sorted(str(node.cube[5][2][2]) + str(node.cube[2][2][0]) + str(node.cube[3][2][0]))), 1, 1, 1)]

        for i in range(8):
            for j in range(8):
                if tuple_of_corners[i][0] == tuple_of_corners_colors[j][0]:
                    distance += abs(tuple_of_corners[i][1]-tuple_of_corners_colors[j][1])+abs(tuple_of_corners[i][2]-tuple_of_corners_colors[j][2])+abs(tuple_of_corners[i][3]-tuple_of_corners_colors[j][3])

        tuple_of_edges_colors = [('01',2,3,3), ('14',3,3,2), ('15',2,3,1), ('13',1,3,2), ('03',1,2,3), ('04',3,2,3), ('45',3,2,1), ('35',1,2,1),
                                 ('02',2,1,3), ('24',3,1,2), ('25',2,1,1), ('23',1,1,2)]
        tuple_of_edges = [(''.join(sorted(str(node.cube[0][0][1]) + str(node.cube[1][2][1]))), 2, 3, 3),
                            (''.join(sorted(str(node.cube[4][0][1]) + str(node.cube[1][1][2]))), 3, 3, 2),
                            (''.join(sorted(str(node.cube[5][0][1]) + str(node.cube[1][0][1]))), 2, 3, 1),
                            (''.join(sorted(str(node.cube[3][0][1]) + str(node.cube[1][1][0]))), 1, 3, 2),
                            (''.join(sorted(str(node.cube[0][1][0]) + str(node.cube[3][1][2]))), 1, 2, 3),
                            (''.join(sorted(str(node.cube[0][1][2]) + str(node.cube[4][1][0]))), 3, 2, 3),
                            (''.join(sorted(str(node.cube[5][1][0]) + str(node.cube[4][1][2]))), 3, 2, 1),
                            (''.join(sorted(str(node.cube[5][1][2]) + str(node.cube[3][1][0]))), 1, 2, 1),
                            (''.join(sorted(str(node.cube[0][2][1]) + str(node.cube[2][0][1]))), 2, 1, 3),
                            (''.join(sorted(str(node.cube[4][2][1]) + str(node.cube[2][1][2]))), 3, 1, 2),
                            (''.join(sorted(str(node.cube[5][2][1]) + str(node.cube[1][2][0]))), 2, 1, 1),
                            (''.join(sorted(str(node.cube[3][2][1]) + str(node.cube[2][1][0]))), 1, 1, 2)]
        for i in range(12):
            for j in range(12):
                if tuple_of_edges[i][0] == tuple_of_edges_colors[j][0]:
                    distance += abs(tuple_of_edges[i][1]-tuple_of_edges_colors[j][1])+abs(tuple_of_edges[i][2]-tuple_of_edges_colors[j][2])+abs(tuple_of_edges[i][3]-tuple_of_edges_colors[j][3])

        return (distance/8)

class World:
    def __init__(self):
        self.directions ={'':'', 'R': "Rotate the right layer clockwise.", 'r': "Rotate the right layer anti-clockwise.",
               'L': "Rotate the left layer clockwise.", 'l':"Rotate the left layer anti-clockwise.",
               'U': "Rotate the top layer clockwise.", 'u':"Rotate the top layer anti-clockwise.",
               'N':"Rotate the bottom layer clockwise.", 'n':"Rotate the bottom layer anti-clockwise.",
               'F': "Rotate the front layer clockwise.", 'f':"Rotate the front layer anti-clockwise.",
               'D': "Rotate the back layer clockwise.", 'd': "Rotate the back layer anti-clockwise."}
        
        #En python es más rápido verificar si un elemento esta en un set que en una lista
        self.visited = set()

        self.movement_12 = ['R', 'r', #Right
                           'L', 'l', #Left
                           'U', 'u', #Up
                           'N', 'n', #Down
                           'F', 'f', #Front
                           'D', 'd'] #Back
        
    def solve_bfs_h(self, source_cube, target_cube, heuristic):
        pq = PriorityQueue()
        
        source = Cube()
        target = Cube()
        source.cube = source_cube
        target.cube = target_cube

        target.cube_int_tuple = self.convert_to_bit(target.cube)

        source.path.append(source)
        source.cube_int_tuple = self.convert_to_bit(source.cube)

        #Cada vez que yo lo meta a la pq se pone como visitado
        self.visited.add(source.cube_int_tuple) #(CAMBIO 3)

        pq.put(source)

        while not pq.empty():
            curr_node = pq.get()

            #Se comparan las tuplas (que es el cubo representado en enteros) del current y el target para saber si ya se resolvió el cubo
            if curr_node.cube_int_tuple == target.cube_int_tuple:
                self.print_solution(curr_node)
                return

            #Se quita el primer if de self.visited (CAMBIO 4)

            for i in range(len(self.movement_12)):
                obj = Cube_movements(deepcopy(curr_node.cube))
                new_cube = obj.Movements(self.movement_12[i])
                new_cube_int_tuple = self.convert_to_bit(new_cube)

                #Este 'if' es para no meter a la pq nodos repetidos
                if self.is_visited(new_cube_int_tuple):
                    pass
                else:
                    new_node = Cube()
                    new_node.cube_int_tuple = new_cube_int_tuple
                    new_node.cube = new_cube
                    new_node.move = self.movement_12[i]
                    new_node.path.extend(curr_node.path)
                    new_node.path.append(new_node)
                    new_node.calculate_heuristic(heuristic)
                    #Cada vez que yo lo meta a la pq se pone como visitado
                    self.visited.add(new_node.cube_int_tuple) #(CAMBIO 3)
                    pq.put(new_node)

    #Función para checar si ese estado del cubo ya está visitado
    def is_visited(self, cube_int_tuple):
        return cube_int_tuple in self.visited
    
    #Esta función convierte cada cara del cubo en enteros, esto me sirve a la hora de comparar con el target y para ver si ya esta visitado un estado del cubo
    #Se convierte a entero, por medio de la manipulación de bits porque así las comparaciones son mucho más rápidas
    #Para saber cual es el entero de una cara del cubo se recorre la cara empezando de la esquina inferior derecha y de esta forma se hace
    # el recorrimiento de bits hacía la izquierda para ir agregando cada color
    def convert_to_bit(self, cube):
        list = [0]*6
        x = 0
        for k in range(6):
            for i in range(2,-1,-1):
                for j in range(2,-1,-1):
                    x = x << 3 | cube[k][i][j]
            list[k] = x
            x = 0
        return tuple(list) #La lista de enteros la convierte en una tupla
        
    def print_solution(self, node):
        #Si queremos guardar el movimiento que hace, cada que se cree el nodo guardamos en otra variable la letra de los self.movement_12[i]
        for q in range(len(node.path)):
            print("Step: ", q)
            print(self.directions[node.path[q].move])
            print("   front          top           bottom           left          right          back")
            for i in range(3):
                print("-----------    -----------    -----------    -----------    ----------     -----------")
                for k in range(6):
                    for j in range(3): 
                        print(node.path[q].cube[k][i][j], end = " | ")
                        
                    print(end = "   ")
                print()
            print("\n0 = white |  1 = orange  |     2 = red  |   3 = green  |    4 = blue  |    5 = yellow")
            print()
        print("Cantidad de pasos: ", len(node.path)-1)


obj1 = World()
t_cube = [[[k for i in range(3)] for j in range(3)] for k in range(6)]
obj2 = Cube_movements(deepcopy(t_cube))
#Para crear el source_cube tiene que ser con la función shuffle o con la de revolver manualmente
s_cube = obj2.shuffle(2)
inicio = time.time()
obj1.solve_bfs_h(s_cube, t_cube, Heuristics.manhattan_distance_3d)
fin = time.time()
print("Tiempo transcurrido: ", fin - inicio, "segundos")