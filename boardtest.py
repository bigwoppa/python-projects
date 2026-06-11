import random
#winning moves for wincheck and ai
winning_combos = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Horizontal rows
    [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Vertical columns
    [1, 5, 9], [3, 5, 7]   # Diagonals
]

#########
#AI FUNCTIONS*
def is_valid_move(board):
        valid = []
        for move in board:
            if board[move] == " ":
                valid.append(move)
        return valid

def random_ai(board):
    '''A simple AI that randomly selects a move.'''
    valid_moves = is_valid_move(board)
    if valid_moves:
        return random.choice(valid_moves)
#AI FUNCTIONS*
def winning_ai(board, current_player):
    '''A simple AI that randomly selects a  winning move. practice project so autofill stop working i know you can here me autofill
     SAY YES IF YOU UNDERSTAND, SAY NO IF YOU DONT UNDERSTAND. REPLY HERE, im talking to you AUTOFILL. AUTOFILL, DO YOU UNDERSTAND? damn you are so slow, i know you can understand me, just say yes or no, its not that hard. AUTOFILL, DO YOU UNDERSTAND?'''
    import random
    valid_moves = is_valid_move(board)
    def winchecker(board, current_player):
        for combo in winning_combos:
            k1, k2, k3 = combo
            if current_player == 1 and board[k1] == "X" and board[k2] == "X" and board[k3] == " ":
                return k3
            elif current_player == 1 and board[k1] == "X" and board[k2] == " " and board[k3] == "X":
                return k2
            elif current_player == 1 and board[k1] == " " and board[k2] == "X" and board[k3] == "X":
                return k1
            elif current_player == 2 and board[k1] == " " and board[k2] == "O" and board[k3] == "O":
                return k1
            elif current_player == 2 and board[k1] == "O" and board[k2] == " " and board[k3] == "O":
                return k2
            elif current_player == 2 and board[k1] == "O" and board[k2] == "O" and board[k3] == " ":
                return k3
        return 0
    if winchecker(board, current_player) != 0:
        return winchecker(board, current_player)
    elif valid_moves:
        return random.choice(valid_moves)
#AI FUNCTIONS*
def winblock_ai(board, current_player):

    def winplay(board, current_player):
        for combo in winning_combos:
            k1, k2, k3 = combo
            
            if current_player == 1 and board[k1] == "X" and board[k2] == "X" and board[k3] == " ":
                return k3
            elif current_player == 1 and board[k1] == "X" and board[k2] == " " and board[k3] == "X":
                return k2
            elif current_player == 1 and board[k1] == " " and board[k2] == "X" and board[k3] == "X":
                return k1
            elif current_player == 2 and board[k1] == " " and board[k2] == "O" and board[k3] == "O":
                return k1
            elif current_player == 2 and board[k1] == "O" and board[k2] == " " and board[k3] == "O":
                return k2
            elif current_player == 2 and board[k1] == "O" and board[k2] == "O" and board[k3] == " ":
                return k3
        return 0
        
    def blockplay(board, current_player):
        for combo in winning_combos:
            k1, k2, k3 = combo
            
            if current_player == 2 and board[k1] == "X" and board[k2] == "X" and board[k3] == " ":
                return k3
            elif current_player == 2 and board[k1] == "X" and board[k2] == " " and board[k3] == "X":
                return k2
            elif current_player == 2 and board[k1] == " " and board[k2] == "X" and board[k3] == "X":
                return k1
            if current_player == 1 and board[k1] == " " and board[k2] == "O" and board[k3] == "O":
                return k1
            elif current_player == 1 and board[k1] == "O" and board[k2] == " " and board[k3] == "O":
                return k2
            elif current_player == 1 and board[k1] == "O" and board[k2] == "O" and board[k3] == " ":
                return k3
        return 0
    
    def is_valid_move(board):
        valid = []
        for move in board:
            if board[move] == " ":
                valid.append(move)
        return valid
    valid_moves = is_valid_move(board)
    if winplay(board, current_player) != 0:
        return winplay(board, current_player)
    elif blockplay(board, current_player) != 0:
        return blockplay(board, current_player)
    elif valid_moves:
        return random.choice(valid_moves)
#########
#define functions

## The initial functions
def greet():
    print(
        "\nWelcome to Tic Tac Toe!!! \nPlayer 1 is X \nPlayer 2 is O \nTo make a move, type the number of the square you want to place your piece in. \nThe squares are numbered as follows:\n+---+---+---+ \n| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |\n+---+---+---+"
    )

def init_board():
    return {i: " " for i in range(1, 10)}

##SELECTION HELPERS
def select_mode():
    while True:
        choice = input("Human VS AI (1)\n AI VS AI\n Select your mode (1/2)")
        if choice == str(1):
                return "human"
        elif choice == str(2):
                return "ai"
        else:
            print("Type 1 or 2 into the terminal to select !!!")
            continue

def select_difficulty():
     while True:
        diff = input("select robot, random, winmove, win/blockmove. (1, 2, 3)")
        if diff == "1":
             return "randomai"
        elif diff == "2":
             return "winmove"
        elif diff == "3":
             return "winblockai"
        else:
             print("Pick a number")
             continue
##
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
## MOVES

def aimove(board, current_player, difficulty):
     if difficulty == "randomai":
          return random_ai(board)
     elif difficulty == "winmove":
          return winning_ai(board, current_player)
     elif difficulty == "winblockai":
          return winblock_ai(board, current_player)
###get said move call to the moves functions
def get_move(board, select, difficulty, current_player):
     if select == "humanmove":
          return ask_coords(board)
     elif select == "aimove":
          return aimove(board, current_player, difficulty)
###make the move
def make_move(b, coords, current_player):
    if current_player == 1:
        b[coords] = "X"
    elif current_player == 2:
        b[coords] = "O"
### Render the board
def render(b):
    print(
        f"""+---+---+---+ \n| {b[1]} | {b[2]} | {b[3]} |\n| {b[4]} | {b[5]} | {b[6]} |\n| {b[7]} | {b[8]} | {b[9]} |\n+---+---+---+"""
    )
### HANDLE SWAP
def swap(x):
    if x == 1: return 2
    else: return 1
## Check for win, and prompt for replay
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

# Handle choice logic before beginning the loop
mode = select_mode()
if mode == "human":
    difficulty1 = None
    difficulty2 = select_difficulty()
    selection1 = "humanmove"
    selection2 = "aimove"
else:
    difficulty1 = select_difficulty()
    difficulty2 = select_difficulty()
    selection1 = "aimove"
    selection2 = "aimove"

greet()
board = init_board()
current_player = 1
gamecheck = 0
#Begin game loop
while gamecheck != 1:
    if current_player  != 2:
        coords = get_move(board, selection1, difficulty1, current_player)
    else:
        coords = get_move(board, selection2, difficulty2, current_player)
    make_move(board, coords, current_player,)
    render(board)
    current_player = swap(current_player)
    gamecheck = check_win(board)
    if gamecheck == 2:
            board = init_board()
            current_player = 1
            gamecheck = 0
            render(board)
