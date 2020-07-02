#Tic Tac Toe
#Author: Alex Sutter

def play_match(player_name):#Done!
    #function used to running the match. Match is won when one of the players won the number of games needed to win
    num_human_wins = 0
    num_computer_wins = 0
    single_game_count = 1
    
    #for improvements ask best of what. So how many games should they play
    #loop deciding the winner of the match and whether or not to contiue with another game in the match
    while num_human_wins < 2 and num_computer_wins < 2:
        print("GAME", single_game_count)
        winner = play_one_game(player_name)
        single_game_count += 1
        if winner == player_name:
            num_human_wins += 1
            print(player_name, "won this game best 2 out of 3")
        elif winner == "computer":
            num_computer_wins += 1
            print("the computer won this game best 2 out of 3")
        else:
            print("That was a tie you are playing best 2 out of 3 ties don't count here")
    if num_human_wins == 2:
        return "The match was won by ", player_name
    else:
        return "The match was won by the computer"
    return
    
def play_one_game(player_name):#Done!
    #function used to play one game of tic-tac-toe and reporting the winner
    board = initialize_board()
    print_board(board)
    for turns_played in range(2):
        human_plays(board)
        computer_plays(board)
        print_board(board)
    while not game_over(board):
        human_plays(board)
        if not game_over(board):
            computer_plays(board)
        print_board(board)
    #loop ends and the game is over 
    
    if game_winner(board) == "X":
        return player_name
    elif game_winner(board) == "O":
        return "computer"
    else:
        return "tie"

def initialize_board():#Done!
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    return board

def game_over(board):#Done!
    #function determines if the game is over by seeing if the there are three X's or O's in a row
    num_of_empty = 0
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                num_of_empty += 1
    if num_of_empty >= 1:
        is_game_over = False
    else:
        return True
    
    for row in range(3):#checking for 3 horizontally
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            if board[row][0] != " " and board[row][1] != " " and board[row][2] != " ":
                return True
    for col in range(3):#checking for 3 vertically
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            if board[0][col] != " " and board[1][col] != " " and board[2][col] != " ":
                return True
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:#checking for diagonal \
        if board[0][0] != " " and board[1][1] != " " and board[2][2] != " ":
            return True
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:#checking for diagonal /
        if board[0][2] != " " and board[1][1] != " " and board[2][0] != " ":
            return True
    return is_game_over

def game_winner(board):#Done!
    #Who won the game "X", "O", or "tie"
    for row in range(3):#see if the winning was horizontal
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            if board[row][0] == "X":
                return "X"
            else:
                return "O"
    for col in range(3):#see if the winning was vertical
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            if board[0][col] == "X":
                return "X"
            else:
                return "O"
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:#winner won diagonally \
        if board[0][0] == "X":
            return "X"
        else:
            return "O"
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:#winner won diagonally /
        if board[0][2] == "X":
            return "X"
        else:
            return "O"
    return "tie"

def human_plays(board):#Done!
    used = False
    while used == False:
        row = int(input("In which row do you want to play? [0-2]: "))
        while row < 0 and row > 2:
            row = int(input("That is not a valid input the number must be [0-2]: "))
        col = int(input("In which column do you want to play? [0-2]: "))
        while col < 0 and col > 2:
            col = int(input("That is not a valid input the number must be [0-2]: "))
        if board[row][col] == " ":
            board[row][col] = "X"
            used = True
        elif board[row][col] != " ":
            print("That spot has already been used. Please try again.")
    return

def computer_plays(board):#make computer smarter and less likely to lose
    #Determine where the computer plays in the location of the "O" 
    #Currently scans through the rows and columns to find the first open spot and plays there
    num_of_spaces_used = 0
    for row in range(3):
        for col in range(3):
            if board[row][col] != " ":
                num_of_spaces_used += 1

    if num_of_spaces_used == 1:
        if board[1][1] == "X":
            board[2][2] = "O"
            return
        else:
            board[1][1] = "O"
            return

    elif num_of_spaces_used >= 3:
        for row in range(3):#checks for winning spot horizontally
            if board[row][0] == board[row][1] or board[row][1] == board[row][2] or board[row][0] == board[row][2]:
                if board[row][0] == "O" and board[row][1] == "O" and board[row][2] == " ":
                    board[row][2] = "O"
                    return
                elif board[row][1] == "O" and board[row][2] == "O" and board[row][0] == " ":
                    board[row][0] = "O"
                    return
                elif board[row][0] == "O" and board[row][2] == "O" and board[row][1] == " ":
                    board[row][1] = "O"
                    return
        for col in range(3):#checks for winning spot vertically
            if board[0][col] == board[1][col] or board[1][col] == board[2][col] or board[0][col] == board[2][col]:
                if board[0][col] == "O" and board[1][col] == "O" and board[2][col] == " ":
                    board[2][col] = "O"
                    return
                elif board[1][col] == "O" and board[2][col] == "O" and board[0][col] == " ":
                    board[0][col] = "O"
                    return
                elif board[0][col] == "O" and board[2][col] == "O" and board[1][col] == " ":
                    board[1][col] = "O"
                    return
        if board[0][0] == board[1][1] or board[1][1] == board[2][2] or board[0][0] == board[2][2]:#checks for winning spot diagonally \
            if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == " ":
                board[2][2] = "O"
                return
            elif board[1][1] == "O" and board[2][2] == "O" and board[0][0] == " ":
                board[0][0] = "O"
                return
            elif board[0][0] == "O" and board[2][2] == "O" and board[1][1] == " ":
                board[1][1] = "O"
                return
        if board[0][2] == board[1][1] or board[1][1] == board[2][0] or board[0][2] == board[2][0]:#checks for winning spot diagonally /
            if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == " ":
                board[2][0] = "O"
                return
            elif board[1][1] == "O" and board[2][0] == "O" and board[0][2] == " ":
                board[0][2] = "O"
                return
            elif board[0][2] == "O" and board[2][0] == "O" and board[1][1] == " ":
                board[1][1] = "O"
                return
        for row in range(3):#checks for blocking X horizontally
            if board[row][0] == board[row][1] or board[row][1] == board[row][2] or board[row][0] == board[row][2]:
                if board[row][0] == "X" and board[row][1] == "X" and board[row][2] == " ":
                    board[row][2] = "O"
                    return
                elif board[row][1] == "X" and board[row][2] == "X" and board[row][0] == " ":
                    board[row][0] = "O"
                    return
                elif board[row][0] == "X" and board[row][2] == "X" and board[row][1] == " ":
                    board[row][1] = "O"
                    return
        for col in range(3):#checks for blocking X vertically
            if board[0][col] == board[1][col] or board[1][col] == board[2][col] or board[0][col] == board[2][col]:
                if board[0][col] == "X" and board[1][col] == "X" and board[2][col] == " ":
                    board[2][col] = "O"
                    return
                elif board[1][col] == "X" and board[2][col] == "X" and board[0][col] == " ":
                    board[0][col] = "O"
                    return
                elif board[0][col] == "X" and board[2][col] == "X" and board[1][col] == " ":
                    board[1][col] = "O"
                    return
        if board[0][0] == board[1][1] or board[1][1] == board[2][2] or board[0][0] == board[2][2]:#checks for blocking X diagonally \
            if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == " ":
                board[2][2] = "O"
                return
            elif board[1][1] == "X" and board[2][2] == "X" and board[0][0] == " ":
                board[0][0] = "O"
                return
            elif board[0][0] == "X" and board[2][2] == "X" and board[1][1] == " ":
                board[1][1] = "O"
                return
        if board[0][2] == board[1][1] or board[1][1] == board[2][0] or board[0][2] == board[2][0]:#checks for blocking X diagonally /
            if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == " ":
                board[2][0] = "O"
                return
            elif board[1][1] == "X" and board[2][0] == "X" and board[0][2] == " ":
                board[0][2] = "O"
                return
            elif board[0][2] == "X" and board[2][0] == "X" and board[1][1] == " ":
                board[1][1] = "O"
                return
        if num_of_spaces_used == 3 and board[2][0] == " ":
            board[2][0] = "O"
            return
        if board[0][1] != " " and board[1][0] != " " and board[1][2] != " " and board[0][2]:
            board[0][2] = "O"
            return
        if board[1][1] == "O":
            if board[0][1] == " ":
                board[0][1] = "O"
                return
            elif board[1][0] == " ":
                board[1][0] = "O"
                return
            elif board[1][2] == " ":
                board[1][2] = "O"
                return
            elif board[2][1] == " ":
                board[2][1] = "O"
                return
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    return

def print_board(board):#Done!
    print("*" * 13)
    for row in range(3):
        for column in range(3):
            print("* ", board[row][column], end="")
        print("*")
        print("*" * 13)
    return

if __name__ == "__main__":
    print(play_match(input("What is your name? ")))