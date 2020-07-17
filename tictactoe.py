import random

def positional_board():
    print(" 7 | 8 | 9 ")
    print("---|---|---")
    print(" 6 | 5 | 4 ")
    print("---|---|---")
    print(" 1 | 2 | 3 ")

def print_board(board):
    print("")
    for i in range(0,9,3):
        if i == 6:
            print(" {} | {} | {} ".format(board[i],board[i+1],board[i+2]))
        else:
            print(" {} | {} | {} ".format(board[i],board[i+1],board[i+2]))
            print("---|---|---")
    print("")

def input_marker():
    player1_marker = input("Player 1, Choose your marker ('X' or 'O') => \n")
    if player1_marker.upper() == 'X':
        player2_marker = 'O'
    elif player1_marker.upper() == 'O':
        player2_marker = 'X'
    else:
        input_marker()
    print('Player 1 your marker is {} and Player 2 your marker is {}\n'.format(player1_marker, player2_marker))
    return (player1_marker, player2_marker)

def placement(board, marker, position):
    board[positions[position]] = marker

def win_check(board, mark):
    def vertical():
        return (board[0] == board[3] == board[6] == mark) or (board[1] == board[4] == board[7] == mark) or (board[2] == board[5] == board[8] == mark)
    def horizontal():
        return (board[0] == board[1] == board[2] == mark) or (board[3] == board[4] == board[5] == mark) or (board[6] == board[7] == board[8] == mark)
    def diagonal():
        return (board[0] == board[4] == board[8] == mark) or (board[2] == board[4] == board[6] == mark)
    return vertical() == True  or horizontal() == True or diagonal() == True


def first_play():
    n = random.randint(0,1)
    return n

def space_check(board, position):
    return board[positions[position]] == " "

def full_board_check(board):
    for element in board:
        if element == " ":
            return False
    return True

def choice(board):
    player_choice = input("Enter position (as a number 1-9) ")
    if space_check(board, player_choice) == True:
        return player_choice
    else:
        print('Position not available, please try again')
        choice(board)

def replay():
    play_again = input("\nDo you want to play again? (Yes or No) ")
    if play_again.title() == "Yes":
        return True
    else:
        return False



print("Welcome to Tic Tac Toe!")
print("")
print("This game's coordinates are placed as shown below: ")
print("")
positional_board()
print("")
print("Now that you know how to play, Lets start! ")

while True:
    positions = {'7':0,'8':1,'9':2,'6':3,'5':4,'4':5,'1':6,'2':7,'3':8}
    board = [" "," "," "," "," "," "," "," "," "]
    markers = input_marker()
    player1_marker = markers[0]
    player2_marker = markers[1]
    first = first_play()
    print("")
    print("")
    if first == 0:
        print_board(board)
        print("Player1 starts!")
        while full_board_check(board) == False:
            #First player turn:
            print("")
            print("Player1's turn")
            player1_position = choice(board)
            placement(board, player1_marker, player1_position)
            print_board(board)
            if win_check(board, player1_marker) == True:
                print("")
                print("Congratulations, Player1 has won the game!!!")
                break
            else:
                pass

            #Second player turn:
            print("")
            print("Player2's turn")
            player2_postion = choice(board)
            placement(board, player2_marker, player2_postion)
            print_board(board)
            if win_check(board, player2_marker) == True:
                print("")
                print("Congratulations, Player2 has won the game!!")
                break
            else:
                pass

        else:
            print("")
            print("The game is a draw")


    elif first == 1:
        print_board(board)
        print("Player2 starts!")
        while full_board_check(board) == False:
            #First player turn:
            print("")
            print("Player2's turn")
            player2_position = choice(board)
            placement(board, player2_marker, player2_position)
            print_board(board)
            if win_check(board, player2_marker) == True:
                print("")
                print("Congratulations, Player2 has won the game!")
                break
            else:
                pass

            #Second player turn:
            print("")
            print("Player1's turn")
            player1_postion = choice(board)
            placement(board, player1_marker, player1_postion)
            print_board(board)
            if win_check(board, player1_marker) == True:
                print("")
                print("Congratulations, Player1 has won the game!!!")
                break
            else:
                pass

        else:
            print("")
            print("The game is a draw")



    re_play = replay()
    if re_play == False:
        break
    else:
        continue
