def display_board(board):
    print('\n'*100)
    print(' '+' '+' '+'|'+' '+' '+' '+'|'+' '+' '+' ')
    print(' '+board[7]+' '+'|'+' '+board[8]+' '+'|'+' '+board[9])
    print(' '+' '+' '+'|'+' '+' '+' '+'|'+' '+' '+' ')
    print(' '+' '+' '+' '+' '+' '+' '+' '+' '+' '+' ')
    print('-'*11)
    print(' '+' '+' '+' '+' '+' '+' '+' '+' '+' '+' ')
    print(' '+' '+' '+'|'+' '+' '+' '+'|'+' '+' '+' ')
    print(' '+board[4]+' '+'|'+' '+board[5]+' '+'|'+' '+board[6])
    print(' '+' '+' '+'|'+' '+' '+' '+'|'+' '+' '+' ')
    print(' '+' '+' '+' '+' '+' '+' '+' '+' '+' '+' ')
    print('-'*11)
    print(' '+' '+' '+' '+' '+' '+' '+' '+' '+' '+' ')
    print(' '+' '+' '+'|'+' '+' '+' '+'|'+' '+' '+' ')
    print(' '+board[1]+' '+'|'+' '+board[2]+' '+'|'+' '+board[3])
    print(' '+' '+' '+'|'+' '+' '+' '+'|'+' '+' '+' ')


def player_input():
    marker=''
    
    #KEEP ASKING PLAYER 1 TO CHOOSE X OR O
    while marker!='X' and marker!='O':
        marker=input("Player1, choose your marker (X or O): ")
        
    #ASSIGN PLAYER 2, ITS OPPOSITE MARKER
    player1=marker
    
    if player1=='X':
        player2='O'
    else:
        player2='X'
        
    return(player1,player2)

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):
    return((board[7]==board[8]==board[9]==mark)or #across the top
           (board[4]==board[5]==board[6]==mark)or #across the middle
           (board[1]==board[2]==board[3]==mark)or #across the bottom
           (board[7]==board[4]==board[1]==mark)or #down the left
           (board[8]==board[5]==board[2]==mark)or #down the middle
           (board[9]==board[6]==board[3]==mark)or #down the right
           (board[7]==board[5]==board[3]==mark)or #left to right diagnolly
           (board[9]==board[5]==board[1]==mark))  #right to left diagnolly

import random

def choose_first():
    if random.randint(0,1)==0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board,position):
    return board[position]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position=0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("Choose your next position (1-9): "))
    
    return position

def replay():
    x='wrong'
    
    while not (x=='Yes' or x=='No'):
        x=input('Do you want to play again (Yes or No): ')
    
    if x=='Yes':
        return True
    else:
        return False

print("Welcome to Tic Tac Toe!")

while True:
    theBoard=[' ']*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn+' will go first.')

    play_game=input('Are you ready to play? Enter Yes or No.').upper()[0]

    if play_game.lower()[0]=='y':
        game_on=True
    else:
        game_on=False

    while game_on:
        if turn=='Player 1':
        
            display_board(theBoard)
            position=player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)
        
            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print('Congratulation, you have won the game!')
                game_on=False
            
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is draw!')
                    break
                
                else:
                    turn='Player 2'
                
                
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)
        
            if win_check(theBoard,player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:turn='Player 1'
    if not replay():
        break