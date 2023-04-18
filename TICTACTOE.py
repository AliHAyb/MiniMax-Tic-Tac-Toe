import numpy as np
import random
import time
from random import choice

MAX_PLAYER = 1
MIN_PLAYER = -1
BOARD = np.zeros(9).reshape(3,3)
BOARD = BOARD.tolist()

def player_to_letter(player):
    if player == MIN_PLAYER:
        return 'X'
    else:
        return 'O'
    
def winning_position(board, player):
    col1 = []
    col2 = []
    col3 = []
    
    for row in board:
        if row.count(row[0]) == len(row) and row[0] == player_to_letter(player):
            return True
        
        col1.append(row[0])
        col2.append(row[1])
        col3.append(row[2])
    if (col1.count(col1[0]) == len(col1) and col1[0] == player_to_letter(player)) or (col2.count(col2[0]) == len(col2) and col2[0] == player_to_letter(player)) or (col3.count(col3[0]) == len(col3) and col3[0] == player_to_letter(player)):
        return True
    
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] == player_to_letter(player):
        return True
     
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] == player_to_letter(player):
        return True
    return False  

def heuristic(board):
    if winning_position(board, MAX_PLAYER):
        score = +1
    elif winning_position(board, MIN_PLAYER):
        score = -1
    else:
        score = 0

    return score

def end_game(board):
    return winning_position(board,MAX_PLAYER) or winning_position(board,MIN_PLAYER)

def available_moves(board):
    moves = []
    for row_ind, row in enumerate(board):
        for col_ind, col in enumerate(row):
            if col == 0:
                moves.append([row_ind, col_ind])
    return moves

def minimax(board, depth, player):
    if player == MAX_PLAYER:
        best = [None, None, -10000]
    else:
        best = [None, None, +10000]

    if depth == 0 or end_game(board):
        score = heuristic(board)
        return [None, None, score]

    for cell in available_moves(board):
        x, y = cell[0], cell[1]
        board[x][y] = player_to_letter(player)
        score = minimax(board, depth - 1, -player)
        board[x][y] = 0
        score[0], score[1] = x, y

        if player == MAX_PLAYER:
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score

    return best

def smart_computer(player):

    depth = len(available_moves(BOARD))
    if depth == 0 or end_game(BOARD):
        return

    options = [0, 1, 2]
    
    if depth == 9:
        x = choice(options)
        y = choice(options)
    else:
        move = minimax(BOARD, depth, player)
        x, y = move[0], move[1]

    BOARD[x][y] = player_to_letter(player)
    time.sleep(1)

def dumb_computer(player):

    depth = len(available_moves(BOARD))
    if depth == 0 or end_game(BOARD):
        return
    options = [0, 1, 2]
    x = choice(options)
    y = choice(options)

    BOARD[x][y] = player_to_letter(player)
    time.sleep(1)
    
def human(player):
    move_mapper = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }
   
    while True:
        try:
            square = int(input("Choose a square: "))
            if square in list(move_mapper.keys()):
                move = move_mapper[square]
                if move in available_moves(BOARD):
                    BOARD[move[0]][move[1]] = player_to_letter(player)                   
                    return
                else:
                    print("This square is already chosen.")
            else:
                print("This is not a valid square.")
        except:
            print("This is not a valid square.")

def tic_tac_toe():
    mode = input("Write 'Easy' to play a dumb computer and 'Hard' to play a smart one: \n")
    computer_talking = ["You're not gonna win :)", "mfakkar halak adde?", "AI never loses!"]
    while not end_game(BOARD) and len(available_moves(BOARD)) != 0:
        human(MIN_PLAYER)
        print(np.array(BOARD))
        if end_game(BOARD):
            print("Human has won.")
            break
        time.sleep(1)
        print(choice(computer_talking ))
        time.sleep(1)
        if mode == 'Easy':
            dumb_computer(MAX_PLAYER)
        elif mode == 'Hard':
            smart_computer(MAX_PLAYER)
        print(np.array(BOARD))
        if end_game(BOARD):
            print("Computer has won.")
        if len(available_moves(BOARD)) == 0 and winning_position(BOARD, MIN_PLAYER) is False and winning_position(BOARD, MAX_PLAYER) is False:
            print('Draw!')
            break
        
        
tic_tac_toe()



