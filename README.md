# SuSolve

Sudoku Solver in Python

## Running the Solver
To run the Sudoku solver, you can use the following command in your terminal:

```bash
python SuSolve.py
```

The program asks you to input the Sudoku row by row. For empty cells "-" or " " is allowed.

### Optionals:
- `-s`/ `--stepWiseSolving`: You can activate a "stepWise solving mode" that requires you to press enter after each new values that was set.


## Printouts:
- The initial and solved Sudoku matrix will be printed to the console:
```bash
>>> Initial Sudoku:
┌───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┐
│ ╔═══╗ │       │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │       │       │ ╔═══╗ │
│ ║ 9 ║ │       │ ║ 2 ║ │ ║ 1 ║ │ ║ 5 ║ │ ║ 4 ║ │       │       │ ║ 7 ║ │
│ ╚═══╝ │       │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │       │       │ ╚═══╝ │
├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│       │ ╔═══╗ │       │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │       │
│       │ ║ 7 ║ │       │ ║ 2 ║ │ ║ 8 ║ │ ║ 9 ║ │ ║ 5 ║ │ ║ 1 ║ │       │
│       │ ╚═══╝ │       │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │       │
├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│       │ ╔═══╗ │ ╔═══╗ │       │       │ ╔═══╗ │       │ ╔═══╗ │       │
│       │ ║ 8 ║ │ ║ 5 ║ │       │       │ ║ 7 ║ │       │ ║ 9 ║ │       │
│       │ ╚═══╝ │ ╚═══╝ │       │       │ ╚═══╝ │       │ ╚═══╝ │       │
├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│ ╔═══╗ │       │ ╔═══╗ │       │ ╔═══╗ │       │       │       │ ╔═══╗ │
│ ║ 4 ║ │       │ ║ 6 ║ │       │ ║ 7 ║ │       │       │       │ ║ 3 ║ │
│ ╚═══╝ │       │ ╚═══╝ │       │ ╚═══╝ │       │       │       │ ╚═══╝ │
├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│       │ ╔═══╗ │       │ ╔═══╗ │ ╔═══╗ │       │       │ ╔═══╗ │       │
│       │ ║ 1 ║ │       │ ║ 9 ║ │ ║ 6 ║ │       │       │ ║ 5 ║ │       │
│       │ ╚═══╝ │       │ ╚═══╝ │ ╚═══╝ │       │       │ ╚═══╝ │       │
├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│       │ ╔═══╗ │       │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │       │       │
│       │ ║ 5 ║ │       │ ║ 8 ║ │ ║ 4 ║ │ ║ 2 ║ │ ║ 1 ║ │       │       │
│       │ ╚═══╝ │       │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │       │       │
├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│       │       │       │ ╔═══╗ │       │ ╔═══╗ │       │       │       │
│       │       │       │ ║ 4 ║ │       │ ║ 5 ║ │       │       │       │
│       │       │       │ ╚═══╝ │       │ ╚═══╝ │       │       │       │
├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│       │ ╔═══╗ │ ╔═══╗ │       │       │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │       │
│       │ ║ 3 ║ │ ║ 1 ║ │       │       │ ║ 6 ║ │ ║ 9 ║ │ ║ 4 ║ │       │
│       │ ╚═══╝ │ ╚═══╝ │       │       │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │       │
├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│       │ ╔═══╗ │       │       │ ╔═══╗ │       │       │       │       │
│       │ ║ 4 ║ │       │       │ ║ 1 ║ │       │       │       │       │
│       │ ╚═══╝ │       │       │ ╚═══╝ │       │       │       │       │
└───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┘


>>> Solved Sudoku:
┌───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┐
│ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │
│ ║ 9 ║ │ ║ 6 ║ │ ║ 2 ║ │ ║ 1 ║ │ ║ 5 ║ │ ║ 4 ║ │ ║ 3 ║ │ ║ 8 ║ │ ║ 7 ║ │
│ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │
├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │
│ ║ 3 ║ │ ║ 7 ║ │ ║ 4 ║ │ ║ 2 ║ │ ║ 8 ║ │ ║ 9 ║ │ ║ 5 ║ │ ║ 1 ║ │ ║ 6 ║ │
│ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │
├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │
│ ║ 1 ║ │ ║ 8 ║ │ ║ 5 ║ │ ║ 6 ║ │ ║ 3 ║ │ ║ 7 ║ │ ║ 4 ║ │ ║ 9 ║ │ ║ 2 ║ │
│ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │
├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │
│ ║ 4 ║ │ ║ 9 ║ │ ║ 6 ║ │ ║ 5 ║ │ ║ 7 ║ │ ║ 1 ║ │ ║ 8 ║ │ ║ 2 ║ │ ║ 3 ║ │
│ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │
├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │
│ ║ 2 ║ │ ║ 1 ║ │ ║ 8 ║ │ ║ 9 ║ │ ║ 6 ║ │ ║ 3 ║ │ ║ 7 ║ │ ║ 5 ║ │ ║ 4 ║ │
│ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │
├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │
│ ║ 7 ║ │ ║ 5 ║ │ ║ 3 ║ │ ║ 8 ║ │ ║ 4 ║ │ ║ 2 ║ │ ║ 1 ║ │ ║ 6 ║ │ ║ 9 ║ │
│ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │
├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │
│ ║ 8 ║ │ ║ 2 ║ │ ║ 7 ║ │ ║ 4 ║ │ ║ 9 ║ │ ║ 5 ║ │ ║ 6 ║ │ ║ 3 ║ │ ║ 1 ║ │
│ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │
├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │
│ ║ 5 ║ │ ║ 3 ║ │ ║ 1 ║ │ ║ 7 ║ │ ║ 2 ║ │ ║ 6 ║ │ ║ 9 ║ │ ║ 4 ║ │ ║ 8 ║ │
│ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │
├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │
│ ║ 6 ║ │ ║ 4 ║ │ ║ 9 ║ │ ║ 3 ║ │ ║ 1 ║ │ ║ 8 ║ │ ║ 2 ║ │ ║ 7 ║ │ ║ 5 ║ │
│ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │
└───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┘
```


- If the Solving mode is activated, cells that were newly set will be marked with `>` and `<`:
```bash
┌───────┐
│>╔═══╗<│
│>║ 5 ║<│
│>╚═══╝<│
└───────┘
```

Furthermore, the possible values per cell will be printed in the console:
```bash
┌───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┐
│ ╔═══╗ │>╔═══╗<│ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │     3 │     3 │ ╔═══╗ │
│ ║ 9 ║ │>║ 6 ║<│ ║ 2 ║ │ ║ 1 ║ │ ║ 5 ║ │ ║ 4 ║ │       │       │ ║ 7 ║ │
│ ╚═══╝ │>╚═══╝<│ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │   8   │   8   │ ╚═══╝ │
├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│     3 │ ╔═══╗ │     3 │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │       │
│       │ ║ 7 ║ │ 4     │ ║ 2 ║ │ ║ 8 ║ │ ║ 9 ║ │ ║ 5 ║ │ ║ 1 ║ │     6 │
│       │ ╚═══╝ │       │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │       │
├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│ 1     │ ╔═══╗ │ ╔═══╗ │     3 │     3 │ ╔═══╗ │   2 3 │ ╔═══╗ │   2   │
│       │ ║ 8 ║ │ ║ 5 ║ │     6 │       │ ║ 7 ║ │ 4   6 │ ║ 9 ║ │ 4   6 │
│       │ ╚═══╝ │ ╚═══╝ │       │       │ ╚═══╝ │       │ ╚═══╝ │       │
├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│ ╔═══╗ │   2   │ ╔═══╗ │       │ ╔═══╗ │ 1     │   2   │   2   │ ╔═══╗ │
│ ║ 4 ║ │       │ ║ 6 ║ │   5   │ ║ 7 ║ │       │       │       │ ║ 3 ║ │
│ ╚═══╝ │     9 │ ╚═══╝ │       │ ╚═══╝ │       │   8   │   8   │ ╚═══╝ │
├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│   2   │ ╔═══╗ │       │ ╔═══╗ │ ╔═══╗ │     3 │   2   │ ╔═══╗ │   2   │
│       │ ║ 1 ║ │       │ ║ 9 ║ │ ║ 6 ║ │       │ 4     │ ║ 5 ║ │ 4     │
│ 7 8   │ ╚═══╝ │ 7 8   │ ╚═══╝ │ ╚═══╝ │       │ 7     │ ╚═══╝ │   8   │
├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│     3 │ ╔═══╗ │     3 │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │       │       │
│       │ ║ 5 ║ │       │ ║ 8 ║ │ ║ 4 ║ │ ║ 2 ║ │ ║ 1 ║ │     6 │     6 │
│ 7     │ ╚═══╝ │ 7   9 │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │ 7     │     9 │
├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│   2   │   2   │       │ ╔═══╗ │   2 3 │ ╔═══╗ │   2 3 │   2 3 │ 1 2   │
│     6 │       │       │ ║ 4 ║ │       │ ║ 5 ║ │     6 │     6 │     6 │
│ 7 8   │     9 │ 7 8 9 │ ╚═══╝ │     9 │ ╚═══╝ │ 7     │ 7     │   8   │
├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│   2   │ ╔═══╗ │ ╔═══╗ │       │   2   │ ╔═══╗ │ ╔═══╗ │ ╔═══╗ │   2   │
│   5   │ ║ 3 ║ │ ║ 1 ║ │       │       │ ║ 6 ║ │ ║ 9 ║ │ ║ 4 ║ │   5   │
│ 7 8   │ ╚═══╝ │ ╚═══╝ │ 7     │       │ ╚═══╝ │ ╚═══╝ │ ╚═══╝ │   8   │
├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│   2   │ ╔═══╗ │       │     3 │ ╔═══╗ │     3 │   2 3 │   2 3 │   2   │
│   5 6 │ ║ 4 ║ │       │       │ ║ 1 ║ │       │     6 │     6 │   5 6 │
│ 7 8   │ ╚═══╝ │ 7 8 9 │ 7     │ ╚═══╝ │   8   │ 7     │ 7     │   8   │
└───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┘
```