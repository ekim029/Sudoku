
import numpy as np

class Puzzle:

    DIM, SUBGRID_DIM = 9, 3

    def __init__(self):
        self.values = np.empty([DIM, DIM], dtype = int)
        self.valIsFixed = np.empty([DIM, DIM], dtype = bool)
        self.rowContains = np.empty([DIM, DIM + 1], dtype = bool)
        self.columnContains = np.empty([DIM, DIM + 1], dtype = bool)
        self.subgridHasValue = np.empty([SUBGRID_DIM, SUBGRID_DIM, DIM + 1], dtype = bool)


    def solveRB(self, n):
        if n >= 81:
            return True
        row = n / 9
        col = n % 9

        for i in range(9):
            if self.valIsFixed[row][col]:
                if self.solveRB(n + 1):
                    return True
                else:
                    return False
            elif not self.rowContains[row][i + 1] and not self.columnContains[col][i + 1] \
                and not self.subgridHasValue[row / 3][col / 3][i + 1]:
                self.placeVal(i + 1, row, col)
                if self.solveRB(n + 1):
                    return True
                self.removeVal(i + 1, row, col)
        return False


    def solve(self):
        foundSol = self.solveRB(0)
        return foundSol


    def placeVal(self, val, row, col):
        self.values[row][col] = val
        self.subgridHasValue[row / SUBGRID_DIM][col / SUBGRID_DIM][val] = True
        self.rowContains[row][val] = True
        self.columnContains[col][val] = True


    def removeVal(self, val, row, col):
        self.values[row][col] = 0
        self.subgridHasValue[row / SUBGRID_DIM][col / SUBGRID_DIM][val] = False
        self.rowContains[row][val] = False
        self.columnContains[col][val] = False


    def readFrom(self, input):
        i = 0
        for line in input:
            j = 0
            for val in line.split(" "): 
                self.placeVal(val, i, j)
                if val != 0:
                    self.valIsFied[i][j] = True
                j += 1
            i += 1


    def display(self):
        for i in range(DIM):
            self.printRowSeparator()
            for j in range(DIM):
                print("|")
                if self.values[i][j] == 0:
                    print("   ")
                else:
                    print(" " + self.values[i][j] + " ")
            print("|")

        self.printRowSeparator()


    def printRowSeparator(self):
        for i in range(DIM):
            print("----")
        print("-\n")
    
