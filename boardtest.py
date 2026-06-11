winning_combos = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Horizontal rows
    [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Vertical columns
    [1, 5, 9], [3, 5, 7]   # Diagonals
]
def init_board():
    return {i: " " for i in range(1, 10)}
def aivshuman(board, current_player):
    import random


    def humanplay(board, current_player):
        print("Human, its your turn")
        return ask_coords(board)
    
    def winplay(board, current_player):
        for combo in winning_combos:
            k1, k2, k3 = combo
            
            if current_player == 2 and board[k1] == " " and board[k2] == "O" and board[k3] == "O":
                return k1
            elif current_player == 2 and board[k1] == "O" and board[k2] == " " and board[k3] == "O":
                return k2
            elif current_player == 2 and board[k1] == "O" and board[k2] == "O" and board[k3] == " ":
                return k3
        
    def blockplay(board, current_player):
        for combo in winning_combos:
            k1, k2, k3 = combo
            
            if current_player == 2 and board[k1] == "X" and board[k2] == "X" and board[k3] == " ":
                return k3
            elif current_player == 2 and board[k1] == "X" and board[k2] == " " and board[k3] == "X":
                return k2
            elif current_player == 2 and board[k1] == " " and board[k2] == "X" and board[k3] == "X":
                return k1
    
    def is_valid_move(board):
        valid = []
        for move in board:
            if board[move] == " ":
                valid.append(move)
        return valid
    
    if current_player == 1:
        return humanplay(board, current_player)
    
    valid_moves = is_valid_move(board)
    winning_move = winplay(board, current_player)
    blocking_move = blockplay(board, current_player)

    if winning_move != None:
        return winning_move
    elif blocking_move != None:
        return blocking_move
    elif valid_moves:
        return random.choice(valid_moves)
    
#use for humanvshuman mode, but also referenced in aivshuman function for humanplay

def ask_coords(board):
    while True:
        try:
            coords = int(input("Pick your coords   "))
        except ValueError:
            print("Thats not a valid move, try again")
            continue

        if coords < 1 or coords > 9 or board[coords] != " ":
            print("Pick an empty square between 1 and 9, try again")
            continue
        
        else:
            return coords
def make_move(b, coords, current_player):
    if current_player == 1:
        b[coords] = "X"
    elif current_player == 2:
        b[coords] = "O"

def swap(x):
    if x == 1: return 2
    else: return 1

def render(b):
    print(
        f"""+---+---+---+ \n| {b[1]} | {b[2]} | {b[3]} |\n| {b[4]} | {b[5]} | {b[6]} |\n| {b[7]} | {b[8]} | {b[9]} |\n+---+---+---+"""
    )
#b stands for board, but it can be any variable name. I just wanted to make it shorter for the sake of readability in the function. It is a common convention to use b for board in tic tac toe implementations.
def check_win(b):
    for combo in winning_combos:
        k1, k2, k3 = combo
        if b[k1] == "X" and b[k2] == "X" and b[k3] == "X":
            print("Player 1 Wins!!!")
            redo = input("Do you want to play again? (y/n)   ")
            if redo == "y":
                return 2
            else:
                return 1
        elif b[k1] == "O" and b[k2] == "O" and b[k3] == "O":
            print("Player 2 Wins!!!")
            redo = input("Do you want to play again? (y/n)   ")
            if redo == "y":
                return 2
            else:
                return 1
    if " " not in b.values():
        print("Its a Tie!!!")
        redo = input("Do you want to play again? (y/n)   ")
        if redo == "y":
            return 2
        else:
            return 1
    return 0

def greet():
    print(
        "\nWelcome to Tic Tac Toe!!! \nPlayer 1 is X \nPlayer 2 is O \nTo make a move, type the number of the square you want to place your piece in. \nThe squares are numbered as follows:\n+---+---+---+ \n| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |\n+---+---+---+"
    )


greet()
board = init_board()
current_player = 1
gamecheck = 0
while gamecheck != 1:
    print(f"Player {current_player}'s turn")
    coords = aivshuman(board, current_player)
    make_move(board, coords, current_player)
    render(board)
    current_player = swap(current_player)
    gamecheck = check_win(board)
    if gamecheck == 2:
        board = init_board()
        current_player = 1
        gamecheck = 0
        render(board)