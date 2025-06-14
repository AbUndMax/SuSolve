# Simple Sudoku solver program
from SudokuMatrix import SudokuMatrix
from resources.example_sudokus import examples
import argparse


def fill_possibilities(sudoku_matrix):
    """
    For each empty cell in the Sudoku matrix, fills its list of possible values (1-9) 
    based on the current state of the board.

    For every cell without a fixed value, all numbers already present in the same row, 
    column, or block are excluded. The remaining numbers are added to the cell's 
    possibilities list.

    Args:
        sudoku_matrix (SudokuMatrix): The SudokuMatrix object whose cells will be analyzed and updated.
    """
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


def solve_via_logic(sudoku_matrix):
    
    fill_possibilities(sudoku_matrix)
        
    def x_wing(sudoku_matrix, num):
        """ https://sudoku.com/de/sudoku-regeln/h-flugel/ 
        
        1) find two rows a, b with a ≠ b, that contain num exactly twice 
        2) check if positions of num in a are the same as in b.
        3) eliminate all possibilities of element num from those columns in which num occurs in a and b
            and which rows in that columns are not a or b!
        
        """
                
        rows = sudoku_matrix.rows
        found_crosses = [] # saves the "coordinates" of found crosses: (row1, row2, col1, col2)
        
        # find crosses (1 & 2)
        for i in range(8): # range(8) because row number 8 can ONLY build a cross with row 9 and row 9 not with itself!
            current_num_indices = [index for index, cell in enumerate(rows[i]) if num in cell.possibilities]
            if len(current_num_indices) != 2: # fullfill condition 1
                continue
            
            for j in range (i + 1, 9):
                compared_num_indices = [index for index, cell in enumerate(rows[j]) if num in cell.possibilities]
                if len(compared_num_indices) != 2: # fullfill condition 1
                    continue
                
                if current_num_indices == compared_num_indices: # fullfill condition 2
                    # tuple to save the cross: (row1=i, row2=j, col1=index[0], col2=index[1])
                    found_crosses.append((i, j, current_num_indices[0], current_num_indices[1]))
        
        # eliminate possibilities (3):
        # loop over the found crosses
        for a, b, col1, col2 in found_crosses: # a and b are the indices of the rows in which num builds a cross
            # for each of both columns
            for c in [col1, col2]: # c is the index of the col in which num possibilities gets removed
                col = sudoku_matrix.cols[c]
                # loop over each entry and eliminate possibilities for num that are not in row a or b
                for i in range(9):
                    cell = col[i]
                    if i != a and i != b and num in cell.possibilities:
                        cell.possibilities.remove(num)
                    
                
    def y_wing(sudoku_matrix, num):
        """ https://sudoku.com/de/sudoku-regeln/y-flugel/ """
        #TODO
        pass
    
    
    def swordfish(sudoku_matrix, num):
        """ https://sudoku.com/de/sudoku-regeln/schwertfisch/ """
        #TODO
        pass
    
    
    def naked_pairs():
        #TODO
        pass
    
    
    def hidden_singles():
        #TODO
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
    
    
def solve_via_TnE():
    #TODO
    pass
    
    
def solve_via_backtracking():
    #TODO
    pass


def main():
    parser = argparse.ArgumentParser(description="Solve Sudoku")
    parser.add_argument("-s", "--stepWiseSolving", action="store_true", help="enables stepwise printout - press enter to see next step")
    args = parser.parse_args()
    
    global stepwise_solving_mode
    stepwise_solving_mode = args.stepWiseSolving
    
    # initialize SudokuMatrix instance
    sudoku_matrix = SudokuMatrix()
        
    # read in a sudoku that should be solved
    sudoku_matrix.read_from_string(examples["easy"])
    
    print("\n>>> Initial Sudoku:")
    sudoku_matrix.print_matrix()
    
    # solve the sudoku
    solve_via_logic(sudoku_matrix)
    
    print("\n>>> Solved Sudoku:")
    sudoku_matrix.print_matrix()
        

if __name__ == "__main__":
    main()