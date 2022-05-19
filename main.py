def user_input():
    '''Accepts user input within the range of (1-9).'''
    choice = ''
    acceptable_range = range(1,10)
    within_range = False

    while not choice.isdigit() or not within_range:

        choice = input("Enter a number from (1-9): ")

        if not choice.isdigit():
            print('Please enter a number')
        
        if int(choice) in acceptable_range:
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


def update_board(game_board,marker ,position):
    '''Takes the game list and user choice to update the game board.'''
    game_board[position] = marker

def check_winner(board):
    """Checks whether all postions are filled in the board in which case its a tie. Otherwise, Checks if the cells are empty then checks if they are the same.
    """
    if all(board):
        print("TIE!")
        return True

    if board[0] and board[1] and board[2]:
        if board[0] == board[1] == board[2]:
            print("WINNER!")
            return True

    elif board[3] and board[4] and board[5]:
        if board[3] == board[4] == board[5]:
            print("WINNER!")
            return True
    
    elif board[6] and board[7] and board[8]:
        if board[6] == board[7] == board[8]:
            print("WINNER!")
            return True

    elif board[0] and board[3] and board[6]:
        if board[0] == board[3] == board[6]:
            print("WINNER!")
            return True

    elif board[1] and board[4] and board[7]:
        if board[1] == board[4] == board[7]:
            print("WINNER!")
            return True
    
    elif board[2] and board[5] and board[8]:
        if board[2] == board[5] == board[8]:
            print("WINNER!")
            return True

    elif board[0] and board[4] and board[8]:
        if board[0] == board[4] == board[8]:
            print("WINNER!")
            return True
    
    elif board[2] and board[4] and board[6]:
        if board[2] == board[4] == board[6]:
            print("WINNER!")
            return True
    
    return False

def display(board):
    print('\n'*100)

    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

    print('-----------')

    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])

    print('-----------')

    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


def full_board_check(board):
    # all() returns true if there are no emptyu stings in the list
    return all(board)


def replay():
    choice = ''
    while choice in ['X', 'Y']:
        choice = input('Do you want to play again? (Yor N): ').upper()

    return choice == 'Y'



def game():
    board = ['#', '', '', '', '', '', '', '', '','']
    gameover= False
    player1 = 'X'
    player2 = 'O'
    while not gameover:
        choice = user_input()
        board = update_board(board, choice, player1)
        display(board)
        gameover = check_winner(board)   
        if gameover:
            break 
        choice = user_input()
        board = update_board(board, choice, player2)
        display(board)
        gameover = check_winner(board)
    replay = input("Do you wwant to play again? (Y/N)? ")
    if replay == 'Y':
        game()
    
game()


