import sys

class Cell:
    """
    Represents a single cell in a Sudoku grid. Tracks its value, associated row/column/block, 
    and remaining possible values.
    """
    
    def __init__(self):
        """
        Initializes the cell with default values. The cell has no assigned value and an empty list of possibilities.
        """
        self.row = None
        self.col = None
        self.block = None
        self.value = None
        self.possibilities = []
        
        
    def set_value(self, value):
        """
        Sets the value of the cell and updates the possibilities of related cells.
        """
        self.value = value
        self._update_possibilities(value)
        
        
    def _update_possibilities(self, value):
        """
        Removes the given value from the possibilities of all related cells (same row, column, block).
        """
        affected_cells = set(self.row + self.col + self.block)
        
        for cell in affected_cells:
            if value in cell.possibilities:
                cell.possibilities.remove(value)
                
                
    def get_unique_possibility(self):
        """
        Returns the only possible value for the cell if it's unique, or a value that is unique among affected cells.
        """
        if len(self.possibilities) == 1:
            return self.possibilities[0]
        else:
            for possibility in self.possibilities:
                if self._possibility_unique(possibility):
                    return possibility
        return None
                
                
    def _possibility_unique(self, possibility):
        """
        Checks whether a given possibility is unique among the possibilities of related cells.
        """
        affected_cells = set(self.row + self.col + self.block)
        possible_values = set(p for cell in affected_cells for p in cell.possibilities)
        
        if possibility not in possible_values:
            return True
        else:
            return False



class SudokuMatrix:
    """
    Represents a complete 9x9 Sudoku grid, composed of Cell objects.
    Handles input, output, and tracking of rows, columns, and 3x3 blocks.
    """
    
    def __init__(self):
        """
        Initializes a 9x9 matrix of Cell objects, and assigns them to corresponding rows, columns, and blocks.
        """
        self.matrix = [[Cell() for _ in range(9)] for _ in range(9)]
        
        self.rows = [self.matrix[i] for i in range(9)]
        self.cols = [[self.matrix[j][i] for j in range(9)] for i in range(9)]
        self.blocks = [[None for _ in range(9)] for _ in range(9)]
            
        for i in range(9):
            for j in range(9):
                cell = self.matrix[i][j]
                block_index = (i // 3) * 3 + (j // 3)
                cell_row_in_block = i % 3
                cell_col_in_block = j % 3
                block_cell_index = cell_row_in_block * 3 + cell_col_in_block
                self.blocks[block_index][block_cell_index] = cell
                
                cell.row = self.rows[i]
                cell.col = self.cols[j]
                cell.block = self.blocks[block_index]
                
                
    def is_solved(self):
        """
        Returns True if all cells in the matrix have a value assigned (i.e., puzzle is solved).
        """
        return all(cell.value is not None for row in self.matrix for cell in row)


    def read_from_input(self):
        """
        Prompts the user to input values for each row of the Sudoku grid via the command line.
        Values must be comma-separated. Empty cells can be marked with '-' or left blank.
        """
        for i in range(9):
            line = input(f"input row number {i + 1} (comma seperated)")
            split_line = [int(value.strip()) if value.strip() not in ("-", "") else None for value in line.split(",")]
            if len(split_line) != 9:
                print("INVALID INPUT! - number of cells in row too long!")
                sys.exit(1)
                
            for j, entry in enumerate(split_line):
                self.matrix[i][j].value = entry
                
    
    def read_from_string(self, string):
        """
        Reads the Sudoku puzzle from a formatted string, where rows are separated by semicolons
        and values by commas. Empty cells can be marked with '-' or left blank.
        """
        rows = string.split(";")
        for i, row in enumerate(rows):
            split_line = [int(value.strip()) if value.strip() not in ("-", "") else None for value in row.split(",")]
            for j, entry in enumerate(split_line):
                self.matrix[i][j].value = entry
            
            
    def _print_matrix_deprecated(self):
        """
        DEPRECATED
        Prints the full 9x9 Sudoku grid in a formatted way. Empty cells are shown as '-'.
        """
        matrix = ""        
        for i in range(9):
            matrix += "\n"
            for j in range(9):
                value = self.matrix[i][j].value if self.matrix[i][j].value is not None else "-"
                matrix += f"{value:^3}"
        print(matrix)
        
        
    def _print_matrix_with_marker(self, i, j):
        """
        DEPRECATED
        Prints the full 9x9 Sudoku grid in a formatted way. Empty cells are shown as '-'.
        cell i,j gets markes with ">[i,j]<"
        """
        matrix = ""        
        for loop_i in range(9):
            matrix += "\n"
            for loop_j in range(9):
                value = self.matrix[loop_i][loop_j].value if self.matrix[loop_i][loop_j].value is not None else "-"
                if loop_i == i and loop_j == j:
                    value = ">" + str(value) + "<"
                matrix += f"{value:^3}"
        print(matrix)
        
        
    def _print_possibilities_per_cell(self):
        """
        DEPRECATED
        Prints the possible values for each cell that still has unresolved options.
        """
        for i in range(9):
            for j in range(9):
                poss = self.matrix[i][j].possibilities
                if poss:
                    print("cell:", i, j)
                    print(poss)
                    print("\n")
                    
                    
    def _print_possibility_matrix(self):
        """ 
        DEPRECATED
        """
        row_char_length = 91
        matrix_string = "-" * row_char_length + "\n"
        for row in self.rows:
            row_string = ""
            for h in range (3):  # 3 rows
                row_string += "|"
                for i in range(9): # 9 cells
                    cell = row[i]
                    for j in range(3): # 3 probabilities per row per cell
                        possibility_value = j + (h * 3) + 1
                        if possibility_value in cell.possibilities:
                            row_string += " " + str(possibility_value) + " "
                        else:
                            row_string += "   "
                        
                    row_string += "|"
                row_string += "\n"
            matrix_string += row_string + "-" * row_char_length  + "\n"
            
        print(matrix_string)
        
        
    def _generate_matrix_string(self, i=None, j=None, showPossibilities=False, showCellValues=True):
        """
        Creates a formatted string representation of the Sudoku grid.

        Each cell is displayed as an ASCII graphic.
        - Cells with a fixed value are shown with a frame and the value in the center:
          ┌───────┐
          │>╔═══╗<│
          │>║ 5 ║<│
          │>╚═══╝<│
          └───────┘

        - Empty cells optionally display possible values as small numbers in their respective positions.
        - Optionally, a specific cell (i, j) can be highlighted.
        - If showPossibilities=True, possible values are shown in empty cells.

        Args:
            i (int, optional): Row index of the cell to highlight.
            j (int, optional): Column index of the cell to highlight.
            showPossibilities (bool, optional): If True, possible values are shown in empty cells.

        Returns:
            str: The ASCII representation of the Sudoku grid.
        """
        
        def value_border(possibility_value, value, marked):
            match(possibility_value):
                case 1:
                    return ">╔" if marked else " ╔"
                case 2 | 8:
                    return "═══"
                case 3:
                    return "╗<" if marked else "╗ "
                case 4:
                    return ">║" if marked else " ║"
                case 5:
                    return " " + str(value) + " "
                case 6:
                    return "║<" if marked else "║ "
                case 7:
                    return ">╚" if marked else " ╚"
                case 9:
                    return "╝<" if marked else "╝ "
        
        
        top_border =    "┌" + "┬".join(["───────"] * 9) + "┐"
        row_border =    "├" + "┼".join(["───────"] * 9) + "┤"
        bottom_border = "└" + "┴".join(["───────"] * 9) + "┘"
        
        matrix_string = top_border + "\n"
        for row_index, row in enumerate(self.rows):
            row_string = ""
            for h in range (3):  # 3 rows
                row_string += "│"
                for col_index in range(9): # 9 cells
                    cell = row[col_index]
                    marked = row_index == i and col_index == j
                    for position in range(3): # 3 probabilities per row per cell
                        possibility_value = position + (h * 3) + 1
                        possibilities = cell.possibilities
                        if not cell.value: # if there are possibilities (i.e no value)
                            if showPossibilities and possibility_value in possibilities:
                                row_string += " " + str(possibility_value)
                            else:
                                row_string += "  "
                        else:
                            row_string += value_border(possibility_value, cell.value, marked) if showCellValues else "  "
                        
                    row_string += "│" if showCellValues and cell.value else " │"
                row_string += "\n"
            matrix_string += row_string
            matrix_string += row_border if row_index < 8 else bottom_border
            matrix_string += "\n"
            
        return matrix_string
    
        
    def print_matrix(self, i=None, j=None, showPossibilities=False, showCellValues=True):
        """
        Prints the Sudoku grid as an ASCII graphic to the console.

        Optionally, a specific cell (i, j) can be highlighted.
        If showPossibilities=True, possible values are displayed in empty cells.

        Args:
            i (int, optional): Row index of the cell to highlight.
            j (int, optional): Column index of the cell to highlight.
            showPossibilities (bool, optional): If True, possible values are shown in empty cells.
        """
        print(self._generate_matrix_string(i, j, showPossibilities, showCellValues))
        
        
    def __str__(self):
        return self._generate_matrix_string()