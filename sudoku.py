def board_input():
    grid = []
    grid_size = int(input('Enter grid size (number of rows): '))
    for i in range(grid_size):
        row = []
        elements = list(map(int(), input('').split(",")))
        row.append(elements)
        grid.append(row)
    return grid

def solve(grid):

    #base case
    find = find_empty(grid)
    if not find:
        return True
    else:
        (row, col) = find

    for i in range(1, 10):
        if valid(grid, i, (row, col)):
            grid[row][col] = i

            if solve(grid):
                return True

            grid[row][col] = 0

    return False


def valid(grid, num, pos):

    #row check
    for i in range(len(grid[0])):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    #column check
    for i in range(len(grid)):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    #square check
    x_box = pos[1]//3
    y_box = pos[0]//3
    for i in range(y_box*3, y_box*3 + 3):
        for j in range(x_box*3, x_box*3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(grid):
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")


def find_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j)

    return None

board = board_input()

print("")
print_board(board)
solve(board)
print("  ")
print("___________________________")
print("  ")
print_board(board)
print("")
