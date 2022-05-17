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



def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)


def update_board(user_choice):
    row1 = ['', '', '']
    row2 = ['', '', '']
    row3 = ['', '', '']

    if user_choice == 1:
        row3[0] = 'X'
    elif user_choice == 2:
        row3[1] = 'X'
    elif user_choice == 3:
        row3[2] = 'X'
    elif user_choice == 4:
        row2[1] = 'X'
    elif user_choice == 5:
        row2[2] = 'X'
    elif user_choice == 6:
        row2[1] = 'X'
    elif user_choice == 7:
        row1[2] = 'X'
    elif user_choice == 8:
        row1[1] = 'X'
    elif user_choice == 9:
        row1[2] = 'X'
    display(row1, row2, row3)



