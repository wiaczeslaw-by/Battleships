import os
import random
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
        user_board_size = 5
    elif user_choice == "2":
        user_board_size = 10
    elif user_board_size == "3":
        user_board_size = int(input("How many field ? :"))
    return user_board_size

def check_fit (board_size, ship_size, user_row, user_column, ship_orientation):
        if ship_orientation == "horizontal" :
            if user_column + ship_size < board_size + 1:
                return True
            else :
                print("Ship will not fit in the table")
                return False
        if ship_orientation == "vertical" :
            if user_row + ship_size < board_size + 1:
                return True
            else :
                print("Ship will not fit in the table")
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


def init_board(board, board_size):    
    for i in range(board_size):
        board.append(["0"]*(board_size))    
    return board
    
def show_board(board, board_size):
    print("  ",end ="")
    for number in range (1,board_size+1):
        print(number,end=" ")
    for row in range(0,board_size):
        ascii_letter = 65 + row
        print()
        print(chr(ascii_letter),end = " ")
        for column in range(0,board_size):
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
    user_row = int(ord(user_row_letter.lower())- 97)
    
    user_column = int(input("Enter the column now :"))-1
    return user_row, user_column

def mark_ships(board, ship_size, ship_orientation, user_row, user_column):
    if ship_orientation == "horizontal":
        for column in range(user_column, user_column + ship_size):
            board[user_row][column] = "S"
    if ship_orientation == "vertical":
        for row in range(user_row, user_row + ship_size):
            board[row][user_column] = "S"

def set_ships(ship_list,board):
    
    for ship in range (len(ship_list)):
        completed_ship = False
        os.system("cls || clear")
        show_board(board, board_size)
        while completed_ship == False:
            print (f'Set position yours ship in size: {ship_list[ship]} \n')
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
    for ship in range (len(ship_list)):
        completed_ship = False
        while completed_ship == False:
            ship_size = ship_list[ship]
            ship_orientation, user_row, user_column = random_ship_cordinates(board_size)
            if check_correct_positon(board, ship_size, user_row, user_column, ship_orientation) is True and check_fit(board_size,ship_size,user_row,user_column,ship_orientation):
                mark_ships(board, ship_size, ship_orientation, user_row, user_column)
                completed_ship = True
            else:
                pass


def two_boards (board, board_1, board_size):
    print("  ",end ="")
    for number in range (1,board_size+1):
        print(number,end=" ")
    print("      ",end="")
    for number in range (1,board_size+1):
        print(number,end=" ")

    for row in range(0,board_size):
        ascii_letter = 65 + row
        print()
        print(chr(ascii_letter),end = " ")
        for column in range(0,board_size):
            print(board[row][column], end=" ")
        print("    ",end="")
        print(chr(ascii_letter),end = " ")
        for column in range(0,board_size):
            print(board_1[row][column], end=" ")
    print()

def random_ship_cordinates(board_size):
    ship_orientation = random.randint(1,2)
    if ship_orientation == 1:
        ship_orientation = "horizontal"
    else :
        ship_orientation = "vertical"
    #print(ship_orientation)
    random_row = random.randint(0,board_size - 1)
    random_column = random.randint(0,board_size - 1)
    #print(random_row,",",random_column)
    return ship_orientation, random_row, random_column

board = []
board_1 = []
ship_list = []
ship_5_5 = [2,1,1,1]
ship_10_10 =[4,3,3,2,2,2,1,1,1,1]

game_mode = game_mode()
board_size = user_board_size()

init_board(board, board_size)
init_board(board_1, board_size)

if board_size == 5:
    ship_list = ship_5_5
elif board_size == 10:
    ship_list = ship_10_10
else:
    ship_list = ship_10_10

#set_ships(ship_list, board)
#set_ships(ship_list, board_1)
random_set_ships(ship_list, board)
random_set_ships(ship_list, board_1)
two_boards(board, board_1,board_size)