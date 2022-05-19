import random

def user_input():
    '''Accepts user input within the range of (1-9).'''
    choice = ''
    acceptable_range = range(1,10)
    within_range = False

    while not choice.isdigit() or not within_range:

        choice = input("Enter a number from (1-9): ")

        if not choice.isdigit():
            print('Please enter a number')
        
        elif int(choice) in acceptable_range:
            within_range = True

    return int(choice)

def player_input():
    """
    OUTPUT = (Player 1 marker, Player 2 marker)
    """
    marker = ''

    while marker not in ['X', 'O']:
        marker = input('Player 1: choose X or O: ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def choose_first():

    if random.randint(1, 2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'

def update_board(game_board,marker ,position):
    '''Takes the game list and user choice to update the game board.'''
    game_board[position] = marker

def check_winner(board,mark):
    return (  # across the top
        (board[7] == mark and board[8] == mark and board[9] == mark) or  
            # across the middle
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            # across the bottom
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            # down the middle
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            # down the right side
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            # diagonal
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  

def display_board(game_board):

    print(' ' + game_board[7] + ' | ' + game_board[8] + ' | ' + game_board[9])

    print('-----------')

    print(' ' + game_board[4] + ' | ' + game_board[5] + ' | ' + game_board[6])

    print('-----------')

    print(' ' + game_board[1] + ' | ' + game_board[2] + ' | ' + game_board[3])

def full_board_check(game_board):
    # all() returns true if there are no emptyu stings in the list
    return all(game_board)

def replay():
    choice = ''
    while choice in ['X', 'Y']:
        choice = input('Do you want to play again? (Yor N): ').upper()

    return choice == 'Y'



def game():
    print('Welcome to Tic-Tack-Toe!')
    while True:
        gameover = False
        board = ['#', '', '', '', '', '', '', '', '','']
        player1_marker,player2_marker = player_input()
        turn = choose_first()
        print(turn + ' will go first')
        
        while not gameover:
            if turn == 'Player 1':
                display_board(board)
                position = user_input()
                update_board(board,player1_marker,position)
                if check_winner(board,player1_marker):
                    display_board(board)
                    print('Player 1 WON!' )
                    gameover = True
                else:
                    if full_board_check(board):
                        print("It's a tie")
                        gameover = True
                    else:
                        turn = 'Player 2'
            else:
                display_board(board)
                position = user_input()
                update_board(board, player2_marker, position)
                if check_winner(board, player2_marker):
                    display_board(board)
                    print('Player 2 WON!')
                    gameover = True
                else:
                    if full_board_check(board):
                        print("It's a tie")
                        gameover = True
                    else:
                        turn = 'Player 1'

  
        if not replay():
            break
    
game()


