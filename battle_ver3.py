import os
import random
import sys

def game_mode():
    print("""Please chose game mode :
                1 - Player vs Player
                2 - Player vs Computer
                3 - Player vs AI
                """)
    game_mode = input("Your choice is :")
    return game_mode

def user_board_size():
    print(""" Please chose board size :
                1 - 5 x 5
                2 - 10 x 10
                3 - You can give a number of size
                """)
    user_choice = input("Your choice is :")
    if user_choice == "1":
        user_board_size = 7
    elif user_choice == "2":
        user_board_size = 12
    elif user_board_size == "3":
        user_board_size = int(input("How many field ? :"))
    return user_board_size

def check_fit (board_size, ship_size, user_row, user_column, ship_orientation):
        if ship_orientation == "horizontal" :
            if user_column + ship_size <= board_size - 1:
                return True
            else :
                print("Ship will not fit in the table(H)")
                return False
        if ship_orientation == "vertical" :
            if user_row + ship_size <= board_size - 1:
                return True
            else :
                print("Ship will not fit in the table(V)")
                return False                

def check_correct_positon (board, ship_size, user_row, user_column, ship_orientation):
    """ sprawdza czy statek może zostac umieszczony na podanej pozycji. Warunke to puste miejsca
    przeznaczone na statek oraz puste pola sąsiadujące. Puste oznacza wartość "0" """              
    for row in range(user_row - 1, user_row + 2):        
        for column in range (user_column -1, user_column + ship_size + 1):
            try :
                if row < 0 or column < 0:
                    pass
                else :
                    if board[row][column] == "0":
                        pass
                    else:
                        return False
                        break
            except IndexError:
                continue
    return True

def init_board(board_size):    
    board = []
    for i in range(board_size):
        board.append(["0"]*(board_size))    
    return board
    
def show_board(board, board_size):
    print("  ",end ="")
    for number in range (1,board_size-1):
        print(number,end=" ")
    for row in range(1,board_size-1):
        ascii_letter = 64 + row
        print()
        print(chr(ascii_letter),end = " ")
        for column in range(1,board_size-1):
            print(board[row][column], end=" ")
    print()

def get_ship_orientation() :
    print(""" Chose ship orientation :
                1. Horizonatal
                2. Vertical        
            """)
    ship_orientation = input("Your choice is (1 or 2):")
    if ship_orientation == "1":
        ship_orientation = "horizontal"
    elif ship_orientation == "2":
        ship_orientation = "vertical"
    else:
        print("Something went wrong, try again")
        get_ship_orientation()
    return ship_orientation

def get_ship_coridnates():
    print("""Chose ship`s position (first field).
            Row - (from A to E)
            Column (from 1 to 5))
            Enter the row first :
            """)
    user_row_letter = input("Enter the row first :")
    user_row = int(ord(user_row_letter.lower())- 96)
    
    user_column = int(input("Enter the column now :"))
    return user_row, user_column

def get_shot_coridnates():
    print("""Chose shot position. (first field).
            Row - (from A to E)
            Column (from 1 to 5))
            Enter the row first :
            """)
    user_row_letter = input("Enter the row first :")
    user_row = int(ord(user_row_letter.lower())- 96)
    
    user_column = int(input("Enter the column now :"))
    return user_row, user_column

def random_shot_coordinates(board_size,board_displayed):
    random_row = random.randint(1,board_size - 2)
    random_column = random.randint(1,board_size - 2)
    if board_displayed[random_row][random_column] == "0":
        return random_row, random_column
    else :    
        random_shot_coordinates(board_size,board_displayed)
    
    
def take_value_field(board,row,column):
    return board[row][column]

def mark_ships(board, ship_size, ship_orientation, user_row, user_column):
    if ship_orientation == "horizontal":
        for column in range(user_column, user_column + ship_size):
            board[user_row][column] = "X"
    if ship_orientation == "vertical":
        for row in range(user_row, user_row + ship_size):
            board[row][user_column] = "X"

def mark_board(board,row,column,sign):
    board[row][column] = sign

def set_ships(ship_list,board):    
    for ship in range (len(ship_list)):
        completed_ship = False
        os.system("cls || clear")
        show_board(board, board_size)
        while completed_ship == False:
            os.system("cls || clear")
            show_board(board, board_size)
            print (f'Set position for the ship of size: {ship_list[ship]} \n')
            ship_size = ship_list[ship]        
            ship_orientation = get_ship_orientation()
            user_row, user_column = get_ship_coridnates()
            if check_correct_positon(board, ship_size, user_row, user_column, ship_orientation) is True and check_fit(board_size,ship_size,user_row,user_column,ship_orientation):
                mark_ships(board, ship_size, ship_orientation, user_row, user_column)
                completed_ship = True
            else:
                print("You cant put ship here. Try again")
        show_board(board, board_size)  

def random_set_ships(ship_list,board):
    for ship in ship_list:
        completed_ship = False
        while completed_ship == False:
            ship_size = ship
            ship_orientation, user_row, user_column = random_ship_cordinates(board_size)
            if check_correct_positon(board, ship_size, user_row, user_column, ship_orientation) is True and check_fit(board_size,ship_size,user_row,user_column,ship_orientation):
                mark_ships(board, ship_size, ship_orientation, user_row, user_column)
                completed_ship = True
            else:
                pass

def two_boards (board_1,board_2):
    print("  ",end ="")
    for number in range (1,len(board_1)-1):
        print(number,end=" ")
    if len(board_1) > 9:
        print("     ",end="")
    else:
        print("      ",end="")
    for number in range (1,len(board_2)-1):
        print(number,end=" ")

    for row in range(1,len(board_1)-1):
        ascii_letter = 64 + row
        print()
        print(chr(ascii_letter),end = " ")
        for column in range(1,len(board_1)-1):
            print(board_1[row][column], end=" ")
        print("    ",end="")
        print(chr(ascii_letter),end = " ")
        for column in range(1,len(board_2)-1):
            print(board_2[row][column], end=" ")
    print()

def random_ship_cordinates(board_size):
    ship_orientation = random.randint(1,2)
    if ship_orientation == 1:
        ship_orientation = "horizontal"
    else :
        ship_orientation = "vertical"
    #print(ship_orientation)
    random_row = random.randint(1,board_size - 2)
    random_column = random.randint(1,board_size - 2)
    #print(random_row,",",random_column)
    return ship_orientation, random_row, random_column

def give_a_shot(player,sequence):
    #win = False
    if player == "player_2":
        board = board_1
        board_displayed = board_1_displayed
    else:
        board = board_2
        board_displayed = board_2_displayed
    next_shot = True
    while next_shot == True:
        print(f"Now {player}")
        if game_mode == "1":
            user_shot_row, user_shot_column = get_shot_coridnates()
        if game_mode == "2" and sequence % 2 == 0:
            user_shot_row, user_shot_column = get_shot_coridnates()
        else :            
            user_shot_row, user_shot_column = random_shot_coordinates(board_size,board_displayed)
        user_shot_value = take_value_field(board,user_shot_row,user_shot_column)
        print(f'You chose {user_shot_row} {user_shot_column}')
        if user_shot_value == "0":
            board_displayed[user_shot_row][user_shot_column] = "M"
            print("You've missed!")
            next_shot = False
        elif user_shot_value == "X":
            mark_board(board_displayed,user_shot_row,user_shot_column,"H")
            ship_elements.clear()
            check_adjacent(board,user_shot_row,user_shot_column, "X")
            if is_sunk(board_displayed) is True:
                print("You've sunk a ship!")
                mark_ship_sunk(board_displayed)
            else:
                print("You've hit a ship!")
        win = has_won(board_displayed)
        if win == True:
            end_game(player)
            exit()
        two_boards(board_1_displayed, board_2_displayed)

def has_won(board):
    count = 0    
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == "S":
                count += 1
    if count == 5:        
        return True
    else:   
        return False

def check_adjacent(board, row, column, sign):
    if board[row+1][column] == sign and check_ship_elements(row+1,column) == False:
        ship_elements.append([row,column])
        check_adjacent(board,row+1, column, sign)
    elif board[row+1][column] == sign and check_ship_elements(row+1,column) == True:
        pass

    if board[row-1][column] == sign and check_ship_elements(row-1,column) == False:
        ship_elements.append([row,column])
        check_adjacent(board,row-1, column, sign)
    elif board[row-1][column] == sign and check_ship_elements(row-1,column) == True:
        pass   
    
    if board[row][column+1] == sign and check_ship_elements(row,column+1) == False:
        ship_elements.append([row,column])
        check_adjacent(board,row, column+1, sign)
    elif board[row][column+1] == sign and check_ship_elements(row,column+1) == True:
        pass

    if board[row][column-1] == sign and check_ship_elements(row,column-1) == False:
        ship_elements.append([row,column])
        check_adjacent(board,row, column -1, sign)
    elif board[row][column-1] == sign and check_ship_elements(row,column-1) == True:
        pass  
    if board[row][column] == sign and check_ship_elements(row,column) == False:
        ship_elements.append([row,column])
            
    if board[row][column] == "0" or board[row][column] =="M":
        if len(ship_elements) == 1:
            pass
        else:
            check_adjacent(board,ship_elements[0][0],ship_elements[0][1],sign)
    
def check_ship_elements(row,column):
    for element in ship_elements:
        if element == [row,column]:
            return True
    return False

def is_sunk(board_displayed):    
    for element in ship_elements:
        row = element[0]
        column = element[1]
        if board_displayed[row][column] != "H":
            return False
    return True

def mark_ship_sunk(board_displayed):
    for element in ship_elements:
        row = element[0]
        column = element[1]
        board_displayed[row][column] = "S"

def end_game(text):
    print(text, "wins !!!")

def fill_boards(game_mode):
    if game_mode == "1":
        set_ships(ship_list, board_1)
        print("You have finished positioning the ships")
        os.system("cls || clear")
        input("Press ENTER to allow the next player to position the ships")
        set_ships(ship_list, board_2)
        print("You have finished positioning the ships")
        os.system("cls || clear")
    else :
        set_ships(ship_list, board_1)
        print("You have finished positioning the ships")
        os.system("cls || clear")
        input("Press ENTER to allow the computer to position the ships")
        random_set_ships(ship_list, board_2)
    
def play_game():    
    two_boards(board_1_displayed, board_2_displayed)
    sequence = 0
    for sequence in range (100):
        if sequence % 2 == 0:
            give_a_shot("player_1",sequence)            
        else:    
            give_a_shot("player_2",sequence)

ship_list = []
ship_elements = []
ship_5_5 = [2,1,1,1]
ship_10_10 =[4,3,3,2,2,2,1,1,1,1]

game_mode = game_mode()
board_size = user_board_size()
board_1 = init_board(board_size)
board_2 = init_board(board_size)
board_1_displayed = init_board(board_size)
board_2_displayed = init_board(board_size)

if board_size == 7:
    ship_list = ship_5_5
elif board_size == 12:
    ship_list = ship_10_10
else:
    ship_list = ship_10_10

fill_boards(game_mode)
play_game()