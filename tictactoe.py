import random

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]


def display_board():
    print()

    for i in range(9):
        if board[i] == " ":
            print(" " + str(i + 1), end=" ")
        else:
            print(" " + board[i], end=" ")

        if i % 3 != 2:
            print("|", end=" ")

        if i % 3 == 2 and i != 8:
            print()
            print("---+---+---")

    print()
    print()


def check_winner(player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False


def board_full():
    return " " not in board


print("TIC-TAC-TOE")
print("You = X")
print("Computer = O")

while True:

    display_board()

    try:
        position = int(input("Choose a position (1-9): "))
    except ValueError:
        print("Please enter a number!")
        continue

    index = position - 1

    if position < 1 or position > 9:
        print("Choose a number between 1 and 9!")
        continue

    if board[index] != " ":
        print("That position is already taken!")
        continue

    board[index] = "X"

    if check_winner("X"):
        display_board()
        print("YOU WIN!")
        break

    if board_full():
        display_board()
        print("DRAW!")
        break


    empty_positions = []

    for i in range(9):
        if board[i] == " ":
            empty_positions.append(i)

    computer_move = random.choice(empty_positions)

    board[computer_move] = "O"

    print("Computer chose position", computer_move + 1)

    if check_winner("O"):
        display_board()
        print("COMPUTER WINS!")
        break

    if board_full():
        display_board()
        print("DRAW!")
        break
