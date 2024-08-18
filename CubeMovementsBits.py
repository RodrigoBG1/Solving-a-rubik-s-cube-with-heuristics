import random

class Cube_movements:
    def __init__(self, cube):
        self.cube = cube

        # matrix that indicates the rotation of a face
        self.rotation = [[(18,20), (9,11), (0,2)],
                        [(21,23), (12,14), (3,5)],
                        [(24,26), (15,17), (6,8)]]

        # 000 - blanco
        # 001 - naranja
        # 010 - rojo
        # 011 - verde
        # 100 - azul
        # 101 - amarillo


    def __get_bits(self, face, gb, lb):
        #Esto es para cuando ya no tenga bits a la izquierda o a la derecha
        if lb > gb or gb < lb: #SEGUN YO NUNCA PASARIA ESTO, PQ SI LE ESTOY MANDANDO BIEN LOS lb Y gb (si pasa, cuando mueves solo un x se ve el ejemplo)
            return 0

        #Esta mascara me ayuda a obtener los bits de un cierto rango (la cantidad de 1 que tenga la mascara es la cantidad de bits que obtendré)
        mask = ((2 ** (gb + 1) - 1) >> lb) << lb

        #Se utiliza el operador AND para poder obtener los bits correctamente y luego se recorre a la derecha para que no se confunda con otro número
        return (face & mask) >> lb 

    def __set_bits(self, face, bits, gb, lb, max_bits=26):
        #Here we get the bits from the left side
        #The mask2 are the bits that I want to add
        #Finally we get the bits from the right side
        mask1 = self.__get_bits(face, max_bits, gb+1)
        mask2 = bits
        mask3 = self.__get_bits(face, lb-1, 0)

        #We make a shift to the left (the shift is the number of bits we will add) to add the mask2, and then we make a shift to the left to add the mask3
        mask1 = ((mask1 << (gb - lb + 1) | mask2) << lb) | mask3   

        return mask1

    def move_x(self, row, n):
        #Here we asign gb and lb depending on the row
        if row == 1:
            gb = 8
            lb = 0
        elif row == 3:
            gb = 26
            lb = 18

        for _ in range(n):
            #We get the bits we will change for each face of the cube
            front_bits = self.__get_bits(self.cube[0], gb, lb)
            left_bits = self.__get_bits(self.cube[3], gb, lb)
            back_bits = self.__get_bits(self.cube[5], gb, lb)
            right_bits = self.__get_bits(self.cube[4], gb, lb)

            #Then we add them to the face they will change
            self.cube[0] = self.__set_bits(self.cube[0], left_bits, gb, lb)
            self.cube[3] = self.__set_bits(self.cube[3], back_bits, gb, lb)
            self.cube[5] = self.__set_bits(self.cube[5], right_bits, gb, lb)
            self.cube[4] = self.__set_bits(self.cube[4], front_bits, gb, lb)
        
            #We make the rotation depending on the row
            if row == 1:
                self.cube[1] = self.__rotate_acw(self.cube[1])
            elif row == 3:
                self.cube[2] = self.__rotate_cw(self.cube[2])

    def move_y(self, col, n):
        #The tiles are the range of the bits (gb and lb) that will be changed depending on the col
        #Also we need the deltas for the back face (the face number 5)
        if col == 1:
            tiles = [(0,2), (9,11), (18,20)]
            deltas = [24, 6, -12]
        elif col == 3:
            tiles = [(6,8), (15, 17), (24, 26)]
            deltas = [12, -6, -24]

        for _ in range(n):
            front_bits = []
            up_bits = []
            back_bits = []
            bottom_bits = []
            #Get the bits that will be changed using the tiles and in specific cases using the deltas
            q = 0
            for tile in tiles:
                front_bits.append(self.__get_bits(self.cube[0], tile[1], tile[0]))
                up_bits.append(self.__get_bits(self.cube[1], tile[1], tile[0]))
                back_bits.append(self.__get_bits(self.cube[5], tile[1] + deltas[q], tile[0] + deltas[q]))
                bottom_bits.append(self.__get_bits(self.cube[2], tile[1], tile[0]))
                q+=1

            #Add them to the faces they will change also using the tiles and deltas
            for i in range(len(tiles)):
                self.cube[0] = self.__set_bits(self.cube[0], bottom_bits[i], tiles[i][1], tiles[i][0])
                self.cube[1] = self.__set_bits(self.cube[1], front_bits[i], tiles[i][1], tiles[i][0])
                self.cube[5] = self.__set_bits(self.cube[5], up_bits[i], tiles[i][1] + deltas[i], tiles[i][0] + deltas[i])
                self.cube[2] = self.__set_bits(self.cube[2], back_bits[i], tiles[i][1], tiles[i][0])

            #Rotate the bits depending on the column
            if col == 1:
                self.cube[3] = self.__rotate_acw(self.cube[3])
            elif col == 3:
                self.cube[4] = self.__rotate_cw(self.cube[4])

    def move_z(self, deep, n):
        #Here it is needed to have 2 tiles and 2 deltas (One for the horizontal bits and other for the vertical bits) depending on the deep
        if deep == 1:
            tiles_hor = [(0, 2), (3, 5), (6, 8)]
            tiles_ver = [(6, 8), (15, 17), (24, 26)]
            delta_hor = 18
            delta_ver = -6
        elif deep == 3:
            tiles_hor = [(18, 20), (21, 23), (24, 26)]
            tiles_ver = [(0,2), (9,11), (18, 20)]
            delta_hor = -18
            delta_ver = 6

        for _ in range(n):
            up_bits = []
            right_bits = []
            bottom_bits = []
            left_bits = []

            #Get the bits that will be changed using the tiles (horizontal and vertical) and in specific cases using the deltas
            for i in range(len(tiles_hor)):
                up_bits.append(self.__get_bits(self.cube[1], tiles_hor[i][1], tiles_hor[i][0]))
                right_bits.append(self.__get_bits(self.cube[4], tiles_ver[2-i][1], tiles_ver[2-i][0]))
                bottom_bits.append(self.__get_bits(self.cube[2], tiles_hor[i][1] + delta_hor, tiles_hor[i][0] + delta_hor))
                left_bits.append(self.__get_bits(self.cube[3], tiles_ver[2-i][1] + delta_ver, tiles_ver[2-i][0] + delta_ver))

            #Add them to the faces they will change also using the tiles(horizontal and vertical) and deltas
            for i in range(len(tiles_hor)):
                self.cube[1] = self.__set_bits(self.cube[1], left_bits[i], tiles_hor[i][1], tiles_hor[i][0])
                self.cube[4] = self.__set_bits(self.cube[4], up_bits[i], tiles_ver[i][1], tiles_ver[i][0])
                self.cube[2] = self.__set_bits(self.cube[2], right_bits[i], tiles_hor[i][1] + delta_hor, tiles_hor[i][0] + delta_hor)
                self.cube[3] = self.__set_bits(self.cube[3], bottom_bits[i], tiles_ver[i][1] + delta_ver, tiles_ver[i][0] + delta_ver)

            #Rotate the bits depending on the deep
            if deep == 1:
                self.cube[5] = self.__rotate_acw(self.cube[5])
            elif deep == 3:
                self.cube[0] = self.__rotate_cw(self.cube[0])

    def __rotate_cw(self, face):
        #For the rotation clockwise we use the rotation matrix
        #If it is 90° we begin with the lower right corner
        #The mask will help to add the bits acording to the gb and lb of the matrix and it will make shifts of 3 
        mask = 0
        for i in range(2, -1, -1):
            for j in range(2, -1, -1):
                mask = (mask << 3) | self.__get_bits(face, self.rotation[i][j][1], self.rotation[i][j][0]) 

        return mask

    def __rotate_acw(self, face):
        #For the rotation anti-clockwise we also use the rotation matrix
        #If it is -90° we begin with the upper left corner
        #The mask will help to add the bits acording to the gb and lb of the matrix and it will make shifts of 3 
        mask = 0
        for i in range(3):
            for j in range(3):
                mask = (mask << 3) | self.__get_bits(face, self.rotation[i][j][1], self.rotation[i][j][0])

        return mask

    def print_cube(self):
        """mask = (2 ** 3) - 1
        for k in range(len(self.cube)):
            aux = self.cube[k]
            print('face', k , '------------')
            for _ in range(3):
                for _ in range(3):
                    print(aux & mask, end=' ')
                    aux >>= 3
                print()"""
        #To print the cube we use a mask of three 1 to obtain the correct bits with the operator AND, then the mask the aux of each face will make a shift of 3
        #This shift to the right help because it deletes the bits that we already print
        mask = (2 ** 3) - 1
        aux = [self.cube[0], self.cube[1], self.cube[2], self.cube[3], self.cube[4], self.cube[5]]
        print("   front          top           bottom           left          right          back")
        for _ in range(3):
            print("-----------    -----------    -----------    -----------    ----------     -----------")
            for i in range(6):
                for _ in range(3):
                    print(aux[i] & mask, end = ' | ')
                    aux[i] >>= 3
                print(end = "   ")
            print()
        print("\n0 = white |  1 = orange  |     2 = red  |   3 = green  |    4 = blue  |    5 = yellow")
        print()
            



    def Movements(self, mov):
        if mov == 'R':
            self.move_y(3, 1)
        elif mov == 'r':
            self.move_y(3, 3)
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
            self.move_z(3, 1)  
        elif mov == 'f':
            self.move_z(3, 3)     
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
                    self.move_y(3, 1)
                elif next == 'r':
                    self.move_y(3, 3)
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
