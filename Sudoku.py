
class Sudoku:

    def main():
        puzzle = Puzzle()
        fileName = input("Please enter the name of puzzle file: ")

        try:
            inputFile = open(fileName, 'r')
            puzzle.readFrom(inputFile)
        except:
            print("Error accessing file " + fileName)
        
        print("Here is the inial puzzle: ")
        puzzle.display()

        if puzzle.solve():
            print("Here is the solution: ")
        else:
            print("No solution could be found")
            print("Here is the current state of the puzzle")
        
        puzzle.display()