pole = [' ', ' ', ' ',
        ' ', ' ', ' ',
        ' ', ' ', ' ']

game_still_going = True

winner = None

current_player = 'X'


def field():
    print('---------')
    print('|', pole[0], pole[1], pole[2], '|')
    print('|', pole[3], pole[4], pole[5], '|')
    print('|', pole[6], pole[7], pole[8], '|')
    print('---------')


def game_process():
    field()  # Виводить поле

    while game_still_going:
        # Place, were X or O is put
        turn(current_player)

        check_if_game_over()
        # Flip to the other player
        flip_player()
    # This code below works if the game process is ending
    if winner == 'X' or winner == 'O':
        print(winner, 'won!')
    if winner is None:
        print('Draw!')
    # if winner == 'X' or winner == 'O' or winner is None:
    #     flag = True
    #     while flag:
    #         flag = input('Do you wanna play one more game? [yes/no]:')
    #         for element in pole:
    #             pole = ' '
    #         game_process()
    #         if flag == 'no':
    #             flag = False
    #     print('Завершення роботи програми')


def turn(player):
    print(player + 's turn')
    valid = False
    while not valid:
        horizontal, vertical = input('Enter coordiantes:').split()
        while horizontal not in ['1', '2', '3']:
            horizontal, vertical = input('Inavlid input. Enter coordiantes:').split()
        while vertical not in ['1', '2', '3']:
            horizontal, vertical = input('Inavlid input. Enter coordiantes:').split()
        horizontal = int(horizontal)
        vertical = int(vertical)

        if horizontal == 1 and vertical == 1 and pole[0] == ' ':
            valid = True
            pole[0] = player
        if horizontal == 1 and vertical == 2 and pole[1] == ' ':
            valid = True
            pole[1] = player
        if horizontal == 1 and vertical == 3 and pole[2] == ' ':
            valid = True
            pole[2] = player
        if horizontal == 2 and vertical == 1 and pole[3] == ' ':
            valid = True
            pole[3] = player
        if horizontal == 2 and vertical == 2 and pole[4] == ' ':
            valid = True
            pole[4] = player
        if horizontal == 2 and vertical == 3 and pole[5] == ' ':
            valid = True
            pole[5] = player
        if horizontal == 3 and vertical == 1 and pole[6] == ' ':
            valid = True
            pole[6] = player
        if horizontal == 3 and vertical == 2 and pole[7] == ' ':
            valid = True
            pole[7] = player
        if horizontal == 3 and vertical == 3 and pole[8] == ' ':
            valid = True
            pole[8] = player
        if valid == False:
            print("You can't go there!")

    field()



def check_if_game_over():
    check_if_win()
    check_if_draw()


def check_if_win():
    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return


def check_rows():
    global game_still_going
    row_1 = pole[0] == pole[1] == pole[2] != ' '
    row_2 = pole[3] == pole[4] == pole[5] != ' '
    row_3 = pole[6] == pole[7] == pole[8] != ' '
    # If someone one we new to change game_still_going to end our while loop
    if row_1 or row_2 or row_3:
        game_still_going = False
        # The code below shows who actually won: X or O
    if row_1:
        return pole[0]
    elif row_2:
        return pole[3]
    elif row_3:
        return pole[6]
    return


def check_columns():
    global game_still_going
    column_1 = pole[0] == pole[3] == pole[6] != ' '
    column_2 = pole[1] == pole[4] == pole[7] != ' '
    column_3 = pole[2] == pole[5] == pole[8] != ' '
    # If someone one we knew to change game_still_going to end our while loop
    if column_1 or column_2 or column_3:
        game_still_going = False
        # The code below shows who actually won: X or O
    if column_1:
        return pole[0]
    elif column_2:
        return pole[1]
    elif column_3:
        return pole[2]
    return


def check_diagonals():
    global game_still_going
    diagonal_1 = pole[0] == pole[4] == pole[8] != ' '
    diagonal_2 = pole[2] == pole[4] == pole[6] != ' '
    # If someone one we knew to change "game_still_going" to end our while loop
    if diagonal_1 or diagonal_2:
        game_still_going = False
        # The code below shows who actually won: X or O
    if diagonal_1:
        return pole[0]
    elif diagonal_2:
        return pole[2]
    return


def check_if_draw():
    global game_still_going
    if ' ' not in pole:
        game_still_going = False
    return


def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return
game_process()