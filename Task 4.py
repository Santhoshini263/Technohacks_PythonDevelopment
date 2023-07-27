import random

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
currentPlayer = "X"
winner = None
play = True


# printing board
def print_Board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-" * 9)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" * 9)
    print(board[6] + " | " + board[7] + " | " + board[8])


# taking input from user(player)
def player_Input(board):
    pos = int(input(f"Enter a number 1-9  Player (X): "))
    if pos >= 1 and pos <= 9 and board[pos - 1] == "-":
        board[pos - 1] = currentPlayer
    else:
        print("Oops! Invalid position...Try in next move! ")


# check for (row, column, diagonal) win or tie
def check_Row(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def check_Column(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True


def check_Diagonal(board):
    global winner
    if (board[0] == board[4] == board[5] and board[0] != "-") or (board[2] == board[4] == board[6] and board[2] != "-"):
        winner = board[4]
        return True


def check_Tie(board):
    global play
    if "-" not in board:
        print_Board(board)
        print("Its a tie")
        play = False


def check_Win():
    if check_Diagonal(board) or check_Row(board) or check_Column(board):
        print_Board(board)
        if winner == "X":
            print("Congratulations!!You won the game...")
        elif winner == "O":
            print("Computer won the game...")
        exit(0)


# switch the player
def switch_Player():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


# computer move
def computer_move(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switch_Player()


print("WELCOME TO TIC-TAC-TOE GAME....")
while play:
    print_Board(board)
    player_Input(board)
    check_Win()
    check_Tie(board)
    switch_Player()
    computer_move(board)
    check_Win()
    check_Tie(board)
