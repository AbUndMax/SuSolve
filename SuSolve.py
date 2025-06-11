# Simple Sudoku solver program
from SudokuMatrix import SudokuMatrix
import argparse

easy = """
9, -, 2, 1, 5, 4, -, -, 7;
-, 7, -, 2, 8, 9, 5, 1, -;
 , 8, 5,  ,  , 7,  , 9,  ;
4, -, 6, -, 7, -, -, -, 3;
-, 1, -, 9, 6, -, -, 5, -;
-, 5, -, 8, 4, 2, 1, -, -;
-, -, -, 4, -, 5, -, -, -;
-, 3, 1, -, -, 6, 9, 4, -;
-, 4, -, -, 1, -, -, -, -
"""

hard = """
3, -, -, -, -, -, -, -, 9;
-, -, -, -, 7, -, 1, -, 2;
-, -, -, -, -, 9, 5, -, -;
-, 7, -, -, 5, -, -, -, -;
1, -, -, 4, -, -, 6, 8, -;
-, -, 6, -, -, -, -, -, -;
7, 1, -, -, 9, -, -, -, 5;
-, -, -, -, -, 3, 8, -, -;
4, -, -, -, -, -, -, 2, -
"""

xWing = """
-, -, 3, 8, -, -, 5, 1, -;
-, -, 8, 7, -, -, 9, 3, -;
1, -, -, 3, -, 5, 7, 2, 8;
-, -, -, 2, -, -, 8, 4, 9;
8, -, 1, 9, -, 6, 2, 5, 7;
-, -, -, 5, -, -, 1, 6, 3;
9, 6, 4, 1, 2, 7, 3, 8, 5;
3, 8, 2, 6, 5, 9, 4, 7, 1;
-, 1, -, 4, -, -, 6, 9, 2
"""

def debug_check(sudoku_matrix):
    while (user := input("input cell index -> row,col")) != "q":
        user_in = user.split(",")
        for cell in sudoku_matrix._sudoku_matrix[int(user_in[0])][int(user_in[1])].block:
            print(cell.value)
            

def solve_sudoku(sudoku_matrix):
    
    def fill_possibilities(sudoku_matrix):
        for i in range(9):
            for j in range(9):
                current_cell = sudoku_matrix.matrix[i][j]
                if not current_cell.value:
                    for possibility in range(1, 10):
                        match_in_row = any(cell.value == possibility for cell in current_cell.row)
                        match_in_col = any(cell.value == possibility for cell in current_cell.col)
                        match_in_block = any(cell.value == possibility for cell in current_cell.block)
                        if match_in_row or match_in_col or match_in_block:
                            continue
                        else:
                            current_cell.possibilities.append(possibility)
    
    
    def solve(sudoku_matrix):
        
        def x_wing(sudoku_matrix, num):
            """ https://sudoku.com/de/sudoku-regeln/h-flugel/ 
            
            1) find two rows a, b with a ≠ b, that contain num exactly twice 
            2) check if positions of num in a are the same as in b.
            3) eliminate all possibilities of element num from those columns in which num occurs in a and b
               and which rows in that columns are not a or b!
            
            """
            pass
                        
                    
        def y_wing(sudoku_matrix, num):
            """ https://sudoku.com/de/sudoku-regeln/y-flugel/ """
            pass
        
        
        def swordfish(sudoku_matrix, num):
            """ https://sudoku.com/de/sudoku-regeln/schwertfisch/ """
            pass
        
        while not sudoku_matrix.is_solved():
            
            # eliminate possibilities
            for num in range(1, 10):
                x_wing(sudoku_matrix, num)
                y_wing(sudoku_matrix, num)
                swordfish(sudoku_matrix, num)
            
            # find unique values and set them
            for i in range(9):
                for j in range(9):
                    current_cell = sudoku_matrix.matrix[i][j]
                    unique = current_cell.get_unique_possibility()
                    if unique:
                        current_cell.set_value(unique)
                        
                        # print matrix if user enabled stepwise mode
                        if stepwise_solving_mode:
                            sudoku_matrix.print_matrix(i, j, True, True)
                            input() # hold until user presses enter
                
                
    fill_possibilities(sudoku_matrix)
    solve(sudoku_matrix)

def main():
    parser = argparse.ArgumentParser(description="Solve Sudoku")
    parser.add_argument("-s", "--stepWiseSolving", action="store_true", help="enables stepwise printout - press enter to see next step")
    args = parser.parse_args()
    
    global stepwise_solving_mode
    stepwise_solving_mode = args.stepWiseSolving
    
    # initialize SudokuMatrix instance
    sudoku_matrix = SudokuMatrix()
        
    # read in a sudoku that should be solved
    sudoku_matrix.read_from_string(xWing)
    
    print("\n>>> Initial Sudoku:")
    sudoku_matrix.print_matrix()
    
    # solve the sudoku
    solve_sudoku(sudoku_matrix)
    
    print("\n>>> Solved Sudoku:")
    sudoku_matrix.print_matrix()
        

if __name__ == "__main__":
    main()