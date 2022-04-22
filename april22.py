board = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

def print_board():
    for i in range(len(board)):
        print(board[i])

def check_bounds(int):
    return int < 0 or int > 2;

def check_board(counter, board):
    #if we have three in a row anywhere, return false

    # horizontal 3
    horizontal = vertical = diagonal = True
    for i in range(len(board)): # row
        h_value = board[i][0];
        horizontal = board[i][1] == board[i][2] == h_value
        if horizontal and h_value != 0:
            print('Player', h_value, 'wins', 'horizontal')
            return False

    # vertical 3
    for i in range(len(board)):  # row
        v_value = board[0][i];
        vertical = board[1][i] == board[2][i] == v_value
        if vertical and v_value != 0:
            print('Player', v_value, 'wins', 'vertical')
            return False

    # diagonal 3
    for i in range(len(board)):  # row
        d_value = board[1][1]
        diagonal1 = board[0][0] == board[2][2] == d_value
        diagonal2 = board [0][2] == board[2][0] == d_value
        if (diagonal1 or diagonal2) and d_value != 0:
            print('Player', d_value, 'wins', 'diagonal')
            return False

    # else -> tie:
    if counter > 8:
        print('Tie')
        return False

    return True;

counter = 0

while check_board(counter, board):

    # board[row][col]

    print('Turn:',counter + 1)
    print('Player',counter % 2 + 1)

    x_location = int(input("which row? (0-2) "))
    y_location = int(input("which col? (0-2) "))

    if check_bounds(x_location) or check_bounds(y_location) or board[x_location][y_location] != 0:
        # reprompt user
        print("try a new location")
        x_location = int(input("which row? "))
        y_location = int(input("which col? "))

    # set location to X
    if counter % 2 == 1:
        board[x_location][y_location] = counter % 2 + 1
        print_board()
    else:
        board[x_location][y_location] = counter % 2 + 1
        print_board()

    counter += 1

    print('------------------------------')