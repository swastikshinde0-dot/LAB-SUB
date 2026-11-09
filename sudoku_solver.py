def is_valid(grid, row, col, num):
    for c in range(9):
        if grid[row][c] == num:
            return False

    for r in range(9):
        if grid[r][col] == num:
            return False

    sr = (row // 3) * 3
    sc = (col // 3) * 3

    for r in range(sr, sr+3):
        for c in range(sc, sc+3):
            if grid[r][c] == num:
                return False

    return True


def solve_sudoku(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                for num in range(1, 10):
                    if is_valid(grid, r, c, num):
                        grid[r][c] = num

                        if solve_sudoku(grid):
                            return True

                        grid[r][c] = 0

                return False

    return True


print("Enter 9 rows with 9 numbers each (0 = empty):")
grid = []

for i in range(9):
    row = list(map(int, input().split()))

    if len(row) != 9 or any(n < 0 or n > 9 for n in row):
        raise ValueError("Enter exactly 9 digits from 0 to 9")

    grid.append(row)

if solve_sudoku(grid):
    print("Solved Sudoku:")
    for row in grid:
        print(*row)
else:
    print("No solution exists")