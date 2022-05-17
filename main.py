def user_input():

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

    if user_choice == 1:
        game_board[0] = player
    elif user_choice == 2:
        game_board[1] = player
    elif user_choice == 3:
        game_board[2] = player
    elif user_choice == 4:
        game_board[1] = player
    elif user_choice == 5:
        game_board[2] = player
    elif user_choice == 6:
        game_board[1] = player
    elif user_choice == 7:
        game_board[2] = player
    elif user_choice == 8:
        game_board[1] = player
    elif user_choice == 9:
        game_board[2] = player
   

    return game_board




