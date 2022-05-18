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



def update_board(game_board,user_choice ,player):
    '''Takes the game list and user choice to update the game list.'''
    if user_choice == 1:
        game_board[0] = player
    elif user_choice == 2:
        game_board[1] = player
    elif user_choice == 3:
        game_board[2] = player
    elif user_choice == 4:
        game_board[3] = player
    elif user_choice == 5:
        game_board[4] = player
    elif user_choice == 6:
        game_board[5] = player
    elif user_choice == 7:
        game_board[6] = player
    elif user_choice == 8:
        game_board[7] = player
    elif user_choice == 9:
        game_board[8] = player
   

    return game_board

def check_winner(game_list):
    """Checks whether all postions are filled in the board in which case its a tie. Otherwise, Checks if the cells are empty then checks if they are the same.
    """
    if all(game_list):
        print("TIE!")
        return True

    if game_list[0] and game_list[1] and game_list[2]:
        if game_list[0] == game_list[1] == game_list[2]:
            print("WINNER!")
            return True

    elif game_list[3] and game_list[4] and game_list[5]:
        if game_list[3] == game_list[4] == game_list[5]:
            print("WINNER!")
            return True
    
    elif game_list[6] and game_list[7] and game_list[8]:
        if game_list[6] == game_list[7] == game_list[8]:
            print("WINNER!")
            return True

    elif game_list[0] and game_list[3] and game_list[6]:
        if game_list[0] == game_list[3] == game_list[6]:
            print("WINNER!")
            return True

    elif game_list[1] and game_list[4] and game_list[7]:
        if game_list[1] == game_list[4] == game_list[7]:
            print("WINNER!")
            return True
    
    elif game_list[2] and game_list[5] and game_list[8]:
        if game_list[2] == game_list[5] == game_list[8]:
            print("WINNER!")
            return True

    elif game_list[0] and game_list[4] and game_list[8]:
        if game_list[0] == game_list[4] == game_list[8]:
            print("WINNER!")
            return True
    
    elif game_list[2] and game_list[4] and game_list[6]:
        if game_list[2] == game_list[4] == game_list[6]:
            print("WINNER!")
            return True
    
    return False


def game():
    game_list = [''] * 9
    gameover= False
    player = 'X'
    while not gameover:
        choice = user_input()
        game_list = update_board(game_list, choice, player)
        print(game_list)
        gameover = check_winner(game_list)    
        

game()


