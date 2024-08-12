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
                #TODO add wall insertion logic
                keyboard.press('backspace')
            elif keyboard.is_pressed('s'):
                #TODO add start point pos change logic
                keyboard.press('backspace')
            elif keyboard.is_pressed('e'):
                #TODO add end point pos change logic
                keyboard.press('backspace')
            elif keyboard.is_pressed('b'):
                #TODO add BFS logic
                keyboard.press('backspace')
            elif keyboard.is_pressed('d'):
                #TODO add DFS logic
                keyboard.press('backspace')
            elif keyboard.is_pressed('a'):
                #TODO add A* logic
                keyboard.press('backspace')
            elif keyboard.is_pressed('q'):
                clear()
                print(yellow("Goodbye!"))
                keyboard.press('backspace')
                exit()
