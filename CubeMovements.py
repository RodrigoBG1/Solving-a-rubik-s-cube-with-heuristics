import numpy as np
import random
from copy import deepcopy
import tkinter as tk
from PIL import Image, ImageTk

class Cube_movements:
    def __init__(self,cube):
        self.cube = cube

    def print_cube(self):
        print("   front          top           bottom           left          right          back")
        for i in range(3):
            print("-----------    -----------    -----------    -----------    ----------     -----------")
            for k in range(6):
                for j in range(3): 
                    print(self.cube[k][i][j], end = " | ")
                    
                print(end = "   ")
            print()
        print("\n0 = white |  1 = orange  |     2 = red  |   3 = green  |    4 = blue  |    5 = yellow")
        print('\n')

    #Siempre es a la derecha (es decir, si quieres que gire 1 a la izquierda debes mandar un 3)
    #Divide entre 4 y el residuo son los giros que daré


    def rotate_90(self, matrix, k):
        n = len(matrix)
        for _ in range(k):
            rotated = [[0 for _ in range(n)] for _ in range(n)]

            for i in range(n):
                for j in range(n):
                    rotated[j][n - i - 1] = matrix[i][j]
            matrix = rotated
            
        return rotated


    def move_x(self, row, n):
        row -= 1
        n = n % 4
        for _ in range(n):
            aux = deepcopy(self.cube[0][row][:])
            self.cube[0][row][:] = self.cube[3][row][:]
            self.cube[3][row][:] = self.cube[5][row][:]
            self.cube[5][row][:] = self.cube[4][row][:]
            self.cube[4][row][:] = aux

        if row == 0:
            if n == 1:
                self.cube[1] = self.rotate_90(self.cube[1], k=3)
            elif n == 2:
                self.cube[1] = self.rotate_90(self.cube[1], k=2)
            elif n == 3:
                self.cube[1] = self.rotate_90(self.cube[1], k=1)

        elif row == 1:
            pass

        elif row == 2:
            if n == 1:
                self.cube[2] = self.rotate_90(self.cube[2], k=1)
            elif n == 2:
                self.cube[2] = self.rotate_90(self.cube[2], k=2)
            elif n == 3:
                self.cube[2] = self.rotate_90(self.cube[2], k=3)

    def move_y(self, col, n):
        col -= 1
        n = n % 4

        if col == 0:
            col2 = 2
        elif col == 1:
            col2 = col
        elif col == 2:
            col2 = 0

        for _ in range(n):
            aux = deepcopy([fila[col] for fila in self.cube[0]])

            for i in range(len(self.cube[0])):
                self.cube[0][i][col] = self.cube[2][i][col]
                self.cube[2][i][col] = self.cube[5][2-i][col2]
                self.cube[5][2-i][col2] = self.cube[1][i][col]
                self.cube[1][i][col] = aux[i]

        if col == 0:
            if n == 1:
                self.cube[3] = self.rotate_90(self.cube[3], k=3)
            elif n == 2:
                self.cube[3] = self.rotate_90(self.cube[3], k=2)
            elif n == 3:
                self.cube[3] = self.rotate_90(self.cube[3], k=1)

        elif col == 1:
            pass

        elif col == 2:
            if n == 1:
                self.cube[4] = self.rotate_90(self.cube[4], k=1)
            elif n == 2:
                self.cube[4] = self.rotate_90(self.cube[4], k=2)
            elif n == 3:
                self.cube[4] = self.rotate_90(self.cube[4], k=3)

    def move_z(self, deep, n):
        deep -= 1
        n = n % 4

        if deep == 0:
            deep2 = 2
        elif deep == 1:
            deep2 = deep
        elif deep == 2:
            deep2 = 0

        for _ in range(n):
            aux = deepcopy([fila[deep2] for fila in self.cube[4]])

            for i in range(3):
                self.cube[4][i][deep2] = self.cube[1][deep][i]
                self.cube[1][deep][i] = self.cube[3][2-i][deep]
                self.cube[3][2-i][deep] = self.cube[2][deep2][2-i]
                self.cube[2][deep2][2-i] = aux[i]

        if deep == 0:
            if n == 1:
                self.cube[5] = self.rotate_90(self.cube[5], k=3)
            elif n == 2:
                self.cube[5] = self.rotate_90(self.cube[5], k=2)
            elif n == 3:
                self.cube[5] = self.rotate_90(self.cube[5], k=1)

        elif deep == 1:
            pass

        elif deep == 2:
            if n == 1:
                self.cube[0] = self.rotate_90(self.cube[0], k=1)
            elif n == 2:
                self.cube[0] = self.rotate_90(self.cube[0], k=2)
            elif n == 3:
                self.cube[0] = self.rotate_90(self.cube[0], k=3)


    def Movements(self, mov):
        if mov == 'R':
            self.move_y(3, 3)
        elif mov == 'r':
            self.move_y(3, 1)
        elif mov == 'L':
            self.move_y(1, 1)
        elif mov == 'l':
            self.move_y(1, 3)
        elif mov == 'U':
            self.move_x(1, 1)  
        elif mov == 'u':
            self.move_x(1, 3)     
        elif mov == 'N':
            self.move_x(3, 1)  
        elif mov == 'n':
            self.move_x(3, 3)
        elif mov == 'F':
            self.move_z(3, 3)  
        elif mov == 'f':
            self.move_z(3, 1)    
        elif mov == 'D':
            self.move_z(1, 1)  
        elif mov == 'd':
            self.move_z(1, 3)
        return self.cube

    def shuffle(self,mov):
        for _ in range(mov):
            mo = random.randint(1, 3)
            r = random.choice([1, 3])
            n = random.choice([1, 3])
            print(mo, " ", r, " ", n)
            if mo == 1:
                self.move_x(r, n)
            elif mo == 2:
                self.move_y(r, n)
            else:
                self.move_z(r, n)
        self.print_cube()
        return self.cube
        # 
    
    def manual(self):
        mov = """
        You can use the next moviments:
        R: Rotate the right layer clockwise.
        r: Rotate the right layer anti-clockwise.
        L: Rotate the left layer clockwise.
        l: Rotate the left layer anti-clockwise.
        U: Rotate the top layer clockwise.
        u: Rotate the top layer anti-clockwise.
        N: Rotate the bottom layer clockwise.
        n: Rotate the bottom layer anti-clockwise.
        F: Rotate the front layer clockwise.
        f: Rotate the front layer anti-clockwise.
        D: Rotate the back layer clockwise.
        d: Rotate the back layer anti-clockwise.
        use "X 1" to leave 
        
        """
        print(mov)
        while True:
            next, nu = input("Enter the moviment and number of movements (D 2)").split()
            n = int(nu)
            for _ in range(n):
                if next == 'R':
                    self.move_y(3, 3)
                elif next == 'r':
                    self.move_y(3, 1)
                elif next == 'L':
                    self.move_y(1, 1)
                elif next == 'l':
                    self.move_y(1, 3)
                elif next == 'U':
                    self.move_x(1, 1)  
                elif next == 'u':
                    self.move_x(1, 3)     
                elif next == 'N':
                    self.move_x(3, 1)  
                elif next == 'n':
                    self.move_x(3, 3)
                elif next == 'F':
                    self.move_z(3, 1)  
                elif next == 'f':
                    self.move_z(3, 3)     
                elif next == 'D':
                    self.move_z(1, 1)  
                elif next == 'd':
                    self.move_z(1, 3)
                elif next == 'X':
                    return self.cube
            print("Your move")    
            self.print_cube()

#6 son las caras, 3 son las filas, 3 son las columnas
cube = [[[k for i in range(3)] for j in range(3)] for k in range(6)]
obj1 = Cube_movements(cube)
obj1.print_cube()

