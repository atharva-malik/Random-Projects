import random

#Here we will write our programs
player = input("Please enter your name. \n")# This will store the data entered by the player in this variable.
print(f"Hello {player}, you are playing the computer version of scissor, paper, rock.")# This will print the name of the player and eveything else which is written inside the brackets().
# Now we will make the computer choose its move.
while True: # This loop will continue to run until we use break.
    p_move = input("Define your move (s for scissors, r for rock and p for paper.) :\n")# This will store the player's move in the p_move variable.
    a = random.randint(0, 2)# This program will help the computer decide its move.(We chose three numbers because there are only three possible moves.)
    # Now let us decide who wil win.
    if p_move == "s" or p_move == "S":
        if a == 0:
            print("Oh, it is a draw.")
            yes = input("Do you want to restart(y / n) ?\n")
            if yes == "y" or yes == "Y":
                print("You got it.")
                continue # This will restart the loop.
            elif yes == "n" or yes == "N":
                print("Thank you for playing.")
                break # This will end the continuous loop.
            else :
                print("Invalid Input.")
                break
        elif a == 1:
            print("Oh yes, I win.")
            yes = input("Do you want to restart(y / n) ?\n")
            if yes == "y" or yes == "Y":
                print("You got it.")
                continue # This will restart the loop.
            elif yes == "n" or yes == "N":
                print("Thank you for playing.")
                break # This will end the continuous loop.
            else :
                print("Invalid Input.")
                break
        elif a == 2:
            print("Oh nooo! You win.")
            yes = input("Do you want to restart(y / n) ?\n")
            if yes == "y" or yes == "Y":
                print("You got it.")
                continue # This will restart the loop.
            elif yes == "n" or yes == "N":
                print("Thank you for playing.")
                break # This will end the continuous loop.
            else :
                print("Invalid Input.")
                break
    if p_move == "p" or p_move == "P":
        if a == 0:
            print("Oh yes. I win.")
            yes = input("Do you want to restart(y / n) ?\n")
            if yes == "y" or yes == "Y":
                print("You got it.")
                continue # This will restart the loop.
            elif yes == "n" or yes == "N":
                print("Thank you for playing.")
                break # This will end the continuous loop.
            else :
                print("Invalid Input.")
                break
        elif a == 1:
            print("Oh noooo. You win.")
            yes = input("Do you want to restart(y / n) ?\n")
            if yes == "y" or yes == "Y":
                print("You got it.")
                continue # This will restart the loop.
            elif yes == "n" or yes == "N":
                print("Thank you for playing.")
                break # This will end the continuous loop.
            else :
                print("Invalid Input.")
                break
        elif a == 2:
            print("Oh, it is a draw.")
            yes = input("Do you want to restart(y / n) ?\n")
            if yes == "y" or yes == "Y":
                print("You got it.")
                continue # This will restart the loop.
            elif yes == "n" or yes == "N":
                print("Thank you for playing.")
                break # This will end the continuous loop.
            else :
                print("Invalid Input.")
                break
    if p_move == "R" or p_move == "r":
        if a == 0:
            print("Oh noooo. You win.")
            yes = input("Do you want to restart(y / n) ?\n")
            if yes == "y" or yes == "Y":
                print("You got it.")
                continue # This will restart the loop.
            elif yes == "n" or yes == "N":
                print("Thank you for playing.")
                break # This will end the continuous loop.
            else :
                print("Invalid Input.")
                break
        elif a == 1:
            print("Oh, it is a draw.")
            yes = input("Do you want to restart(y / n) ?\n")
            if yes == "y" or yes == "Y":
                print("You got it.")
                continue # This will restart the loop.
            elif yes == "n" or yes == "N":
                print("Thank you for playing.")
                break # This will end the continuous loop.
            else :
                print("Invalid Input.")
                break
        elif a == 2:
            print("Oh yes. I win.")
            yes = input("Do you want to restart(y / n) ?\n")
            if yes == "y" or yes == "Y":
                print("You got it.")
                continue # This will restart the loop.
            elif yes == "n" or yes == "N":
                print("Thank you for playing.")
                break # This will end the continuous loop.
            else :
                print("Invalid Input.")
                break
