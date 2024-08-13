import keyboard
from os import system, name
from simple_colors import *

base_board = [
    ["s", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "e"]
]

board = base_board.copy()

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def print_board(board):
    return_board = ""
    i = 0
    return_board += "#  | "
    for j in range(20):
        if j < 10:
            return_board += str(j) + "  | "
        else:
            return_board += str(j) + " | "
    return_board += "\n--------------------------------------------------------------------------------------------------------\n"
    for row in board:
        if i < 10:
            return_board += str(i) + "  | "
        else:
            return_board += str(i) + " | "
        for col in row:
            return_board += col + "  | "
        return_board += "\n--------------------------------------------------------------------------------------------------------\n"
        i += 1
    print(return_board)

def find_tile_pos(board, tile):
    for i in range(20):
        for j in range(20):
            if board[i][j] == tile:
                return i, j
    return -1, -1

def change_tile(board, tile, x=-1, y=-1):
    if x < 0:
        x, y = find_tile_pos(board, tile)
    board[x][y] = tile

def get_int_coords():
    print_board(board)
    try:
        x = int(input("Enter x coordinate: "))
        y = int(input("Enter y coordinate: "))
    except ValueError:
        print(red("NaN!", "bold"))
        return -1, -1
    if x < 0 or y < 0 or x > 19 or y > 19:
        print(red("Invalid coordinates!", "bold"))
        return -1, -1
    return x, y

def bfs(board):
    pass # https://youtu.be/pcKY4hjDrxk?t=364

def dfs(board):
    pass

def a_star(board):
    pass

if __name__ == "__main__":
    clear()
    while True:
        print(yellow("Welcome to the algorithm visualiser! Press any key to start, or press 'H' for help!"))
        while True:
            if keyboard.is_pressed('H'):
                clear()
                print(yellow("Welcome to the algorithm visualiser! Press any key to start, or press 'H' for help!"))
                print(yellow("Press 'Q' to quit, 'R' to reset, 'H' for help, 'W' to insert a wall, 'S' to change start point pos, 'E' to change end point pos", "bold"), "\n")
                print(yellow("Press 'B' for BFS, 'D' for DFS, 'A' for A*", "bold"))
                keyboard.press('backspace')
            elif keyboard.is_pressed('r'):
                board = base_board.copy()
                clear()
                keyboard.press('backspace')
            elif keyboard.is_pressed('w'):
                keyboard.press('backspace')
                x,y  = get_int_coords()
                if x < 0:
                    continue
                change_tile(board, "w", x, y)
            elif keyboard.is_pressed('s'):
                keyboard.press('backspace')
                print_board(board)
                x,y  = get_int_coords()
                if x < 0:
                    continue
                x1, y1 = find_tile_pos(board, "s")
                change_tile(board, ".", x1, y1)
                change_tile(board, "s", x, y)
            elif keyboard.is_pressed('e'):
                keyboard.press('backspace')
                print_board(board)
                x,y  = get_int_coords()
                if x < 0:
                    continue
                x1, y1 = find_tile_pos(board, "e")
                change_tile(board, ".", x1, y1)
                change_tile(board, "e", x, y)
            elif keyboard.is_pressed('b'):
                bfs(board)
                keyboard.press('backspace')
            elif keyboard.is_pressed('d'):
                dfs(board)
                keyboard.press('backspace')
            elif keyboard.is_pressed('a'):
                a_star(board)
                keyboard.press('backspace')
            elif keyboard.is_pressed('q'):
                clear()
                print(yellow("Goodbye!"))
                keyboard.press('backspace')
                exit()
