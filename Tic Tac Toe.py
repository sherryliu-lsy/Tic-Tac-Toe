import random, copy

player_1 = "X"
player_2 = "O"

def print_board(board):
    print("    0    1    2")
    for i in range(len(board)):
        print(i, board[i])

def make_copy(board):
    duplicate = []
    for i in range(3):
        duplicate.append(copy.copy(board[i]))
    return duplicate


def reset_board(board):
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def is_valid_turn(board, i, j):
    if board[i][j] == " " and 3 > i > -1 and 3 > j > -1:
        return True
    else:
        return False


def has_won(board, player):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True
    elif board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    else:
        return False


def find_spot(board):
    spots = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                spots.append([i, j])
    return spots


def computer_easy(board):
    choice1 = random.choice(find_spot(board))
    board[choice1[0]][choice1[1]] = "O"

def computer_medium(board):
    
    # 1. if computer can win in next step, win immediately
    for i in range(3):
        for j in range(3):
            computer1 = make_copy(board)
            if is_valid_turn(computer1, i ,j):
                computer1[i][j] = "O"
                if has_won(computer1, player_2):
                    board[i][j] = "O"
                    return 0

    # 2. if player can win in next step, stop player
    for i in range(3):
        for j in range(3):
            computer1 = make_copy(board)
            if is_valid_turn(computer1, i ,j):
                computer1[i][j] = player_1
            if has_won(computer1, player_1):
                board[i][j] = "O"
                return 0
                
    computer_easy(board)

def computer_hard(board):
    
    # 1. if computer can win in next step, win immediately
    for i in range(3):
        for j in range(3):
            computer1 = make_copy(board)
            if is_valid_turn(computer1, i ,j):
                computer1[i][j] = "O"
                if has_won(computer1, player_2):
                    board[i][j] = "O"
                    return 0

    # 2. if player can win in next step, stop player
    for i in range(3):
        for j in range(3):
            computer1 = make_copy(board)
            if is_valid_turn(computer1, i ,j):
                computer1[i][j] = player_1
            if has_won(computer1, player_1):
                board[i][j] = "O"
                return 0

    # 3. the next best moves:

    # in the middle
    if board[1][1] == " ":
        board[1][1] = "O"
        return 0

    # 4 corners
    temp_list = [[0,0],[0,2],[2,0],[2,2]]
    for i in temp_list:
        if is_valid_turn(board,i[0],i[1]):
            board[i[0]][i[1]] = "O"
            return 0

    # any random place
    computer_easy(board)

# Game engine

def again():
    again = 0
    while again != "yes" and again != "no":
        again = input("Would you like to play again? (yes/no) ")
    if again == "yes":
        return True
    else:
        return False

def game():

    board = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]
    won = False
    counter = 0

    print()
    print("Welcome to tic-tac-toe!")

    start = int(input("(1) Player vs Computer; (2) Player 1 vs Player 2 "))
    if start == 1:
        choice = int(input("Select difficulty: (1) Easy; (2) Medium; (3) IMPOSSIBLE "))
    else:
        choice = 0
        
    print()
    
    print_board(board)
    print()

    while not won:

        if counter == 9:
            print("It's a tie!")
            if again():
                game()
        
        elif counter % 2 == 0:
            if choice == 0:
                input_1 = input("Player 1: Where would you like to play? ")
            else:
                input_1 = input("Player: Where would you like to play? ")
            if len(str(input_1)) == 2 and is_valid_turn(board, int(input_1[0]), int(input_1[len(input_1)-1])):
                board[int(input_1[0])][int(input_1[1])] = player_1
                counter += 1
            else:
                print("Invalid input. Please try again.")
                continue

        else:

            if choice == 0:
                input_2 = input("Player 2: Where would you like to play? ")
                if len(str(input_2)) == 2 and is_valid_turn(board, int(input_2[0]), int(input_2[1])):
                    board[int(input_2[0])][int(input_2[1])] = player_2
                    counter += 1
                else:
                    print("Invalid input. Please try again.")
                    continue
            else:
                print("Computer:")
                counter += 1
                if choice == 1:
                    computer_easy(board)
                elif choice == 2:
                    computer_medium(board)
                else:
                    computer_hard(board)

        print_board(board)
        print()
        
        if has_won(board, player_1):
            won = True
            print("Congradulations! You've won :)")
            if again():
                game()
            break
        elif has_won(board, player_2):
            if choice == 3:
                println("Congradulations to Player 2! :)")
            else:
                print("Game over. Computer won.")
            if again():
                game()  
            break
        else:
            continue

    print("Thanks for playing!")

game()
