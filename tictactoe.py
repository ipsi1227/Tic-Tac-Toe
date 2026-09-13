import random

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

def display_board(board):

    print()

    for i in range(9):

        if board[i] == " ":
            print(" " + str(i + 1) + " ", end="")
        else:
            print(" " + board[i] + " ", end="")

        if i % 3 != 2:
            print("|", end="")

        if i % 3 == 2 and i != 8:
            print()
            print("---+---+---")

    print()
    print()


def check_winner(board, player):

    for a, b, c in winning_combinations:

        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False


def board_full(board):

    return " " not in board

def get_move(board, player):

    while True:

        try:
            position = int(input(player + ", choose a position (1-9): "))

        except ValueError:
            print("Please enter a number!")
            continue

        if position < 1 or position > 9:
            print("Choose a number between 1 and 9!")
            continue

        index = position - 1

        if board[index] != " ":
            print("That position is already taken!")
            continue

        return index

def play_computer():

    board = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]

    print()
    print("You = X")
    print("Computer = O")

    while True:

        display_board(board)

        index = get_move(board, "You")
        board[index] = "X"

        if check_winner(board, "X"):
            display_board(board)
            print("YOU WIN!")
            break
        if board_full(board):
            display_board(board)
            print("DRAW!")
            break

        empty_positions = []

        for i in range(9):

            if board[i] == " ":
                empty_positions.append(i)

        computer_move = random.choice(empty_positions)

        board[computer_move] = "O"

        print("Computer chose position", computer_move + 1)
        if check_winner(board, "O"):
            display_board(board)
            print("COMPUTER WINS!")
            break
        if board_full(board):
            display_board(board)
            print("DRAW!")
            break

def play_friend():

    board = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]

    print()
    print("Player 1 = X")
    print("Player 2 = O")

    while True:

        display_board(board)

        index = get_move(board, "Player 1")
        board[index] = "X"

        if check_winner(board, "X"):
            display_board(board)
            print("PLAYER 1 WINS!")
            break
        if board_full(board):
            display_board(board)
            print("DRAW!")
            break

        display_board(board)

        index = get_move(board, "Player 2")
        board[index] = "O"

        if check_winner(board, "O"):
            display_board(board)
            print("PLAYER 2 WINS!")
            break

        if board_full(board):
            display_board(board)
            print("DRAW!")
            break

print("================================")
print("       TIC-TAC-TOE ")
print("================================")

print()
print("Who do you want to play with?")
print("1. Computer")
print("2. Friend ")


while True:

    choice = input("\nChoose 1 or 2: ")

    if choice == "1":

        play_computer()
        break

    elif choice == "2":

        play_friend()
        break

    else:

        print("Please choose 1 or 2!")
