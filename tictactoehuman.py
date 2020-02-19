# TIC TAC TOE TWO PLAYER
import random
def show_board(board):
    print(f"{board[1]}|{board[2]}|{board[3]}")
    print("-+-+-")
    print(f"{board[4]}|{board[5]}|{board[6]}")
    print("-+-+-")
    print(f"{board[7]}|{board[8]}|{board[9]}")
def make_move(board,letter,move):
    if isSpaceFree(board,move):
        board[move]=letter
    else:
        print("wrong move")
        if turn=="player1":
            turn="player2"
        else:
            turn="player1"
def first_chance():
    if random.randint(0,1)==0:
        return 'player1'
    else:
        return 'player2'

def choose_letter():
    i=input("player 1 letter (x,o)  :").upper()
    if i=="X":
        return["X","O"]
    else:
        return["O","X"]
def player1_move():
    print("player1 move\n")
    turn="player2"
    return int(input(""))
def player2_move():
    print("player2 move\n")
    turn = 'player1'
    return int(input(""))
def winner(bo,le):
    
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # Across thetop
    (bo[4] == le and bo[5] == le and bo[6] == le) or # Across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # Across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # Down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # Down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # Down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # Diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # Diagonal

def isBoardFull(board):
     # Return True if every space on the board has been taken. Otherwise,return False.
     for i in range(1, 10):
         if isSpaceFree(board, i):
             return False
     return True
def isSpaceFree(board, move):
     # Return True if the passed move is free on the passed board.
     return board[move] == ' '

print("Welcome to Tic Tac Toe")
while True:
    board = [" "]*10
    show_board(board)
    gameisplaying= True
    player1_letter,player2_letter=choose_letter()
    turn=first_chance()
    while gameisplaying:
        if turn=="player1":
            move=player1_move()
            make_move(board,player1_letter,move)
            show_board(board)
            if winner(board,player1_letter):
                print("hurrah player1 is winner")
                gameisplaying= False
            elif isBoardFull(board):
                print("game is tie")
                gameisplaying= False
            else:
                turn= "player2"



        else:
            move=player2_move()
            make_move(board,player2_letter,move)
            show_board(board)
            if winner(board,player2_letter):
                print("hurrah player2 is winner")
                gameisplaying= False
            elif isBoardFull(board):
                print("game is tie")
                gameisplaying= False
            else:
                turn= "player1"
    break