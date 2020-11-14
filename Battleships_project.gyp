import os
import time
from random import randint


ship_sets = ['S', 'SS', 'SSS', 'SSSS']
chosen_set_of_ships = []


def main():
    board = [[]]
    os.system("cls || clear")
    print("Let's the seabattle begins!")
    time.sleep(1)
    choose_game_mode()
    board, chosen_set_of_ships = board_size(board)
    print_board(board)
    print(chosen_set_of_ships)
    print(board)
    random_ship_placement(board)
    print_board(board) 

def choose_game_mode():
<<<<<<< HEAD
    user_game_mode = input("Please, choose game mode:\n 1 - Player vs Player\n 2 - Player vs Comp ")
    if user_game_mode == '1':
        player = 1
        return player
    elif user_game_mode == '2':
        computer = 2
        return computer         
    else:
        os.system("cls || clear")
        print("Input correct data and try again")
        time.sleep(1)
        choose_game_mode()


def board_size(board):                            # function for choosing board size and ship_set according to it
    os.system("cls || clear")  
    userinput = input("Please, choose board size:\n 1 - small (5*5)\n 2 - regular (10*10)\n 3 - big (15*15)")
    if userinput == '1': 
        for row in range(0, 5):
            cell = {"symbol" : "O", "status" : "inactive"}
            board = add_objects_to_list(board, 5, cell, row)
            if row < 4:
                board.append([])
        for ship in range(3):                           #quantity os "S" = 3
            chosen_set_of_ships.append(ship_sets[0])
        chosen_set_of_ships.append(ship_sets[1])        #quantity os "SS" = 1
    elif userinput == '2':
        for row in range(0, 10):
            board.append([cell] * 10)
        for ship in range(4):                            #quantity os "S" = 4      
            chosen_set_of_ships.append(ship_sets[0])
        for ship in range(3):                            #quantity os "SS" = 3
            chosen_set_of_ships.append(ship_sets[1])
        for ship in range(2):                            #quantity os "SSS" = 2
            chosen_set_of_ships.append(ship_sets[2])
        chosen_set_of_ships.append(ship_sets[3])         #quantity os "SSSS" = 1
    elif userinput == '3':
        for row in range(0, 15): 
            board.append([cell] * 15)
        for ship in range(8):                            #quantity os "S" = 8     
            chosen_set_of_ships.append(ship_sets[0])
        for ship in range(6):                            #quantity os "SS" = 6
            chosen_set_of_ships.append(ship_sets[1])
        for ship in range(4):                            #quantity os "SSS" = 4
            chosen_set_of_ships.append(ship_sets[2])
        for ship in range(2):                            #quantity os "SSSS" = 2
            chosen_set_of_ships.append(ship_sets[3])        
    else:
        print("Input correct data")
        time.sleep(2)
        # board = board_size(board, cell)
    return board, chosen_set_of_ships 

def add_objects_to_list(board, size, user_object, row):
    for index in range(size):
        board[row].append(user_object)
    return board


# cell = {"symbol" : "O", "status" : "inactive"}
    # if cell["status"] == "inactive":
    # for row in board: 
    #   for column in board:
            # print(column["symbol"] end = " ")
        # print("\n")

# if col+1 > len(row):
# try another side
                                

def print_board(board):
    for row in range(len(board)): 
        for cell in board[row]:
            print(get_object_value(cell, "symbol"), end = " ")
        print()

def random_ship_placement(board):
    for ships in range(0, len(chosen_set_of_ships) - 1):
        while chosen_set_of_ships != []:
            random_column = randint(0, len(board) - 1)
            random_row = randint(0, len(board) - 1) 
            print(random_column, random_row)
            if len(chosen_set_of_ships[0]) == 2:
                board[random_column][random_row] = set_object_value(board[random_column][random_row], "symbol", "S")  
                if board[random_column][random_row-1] == 'O': 
                    try:
                        board[random_column][random_row-1] = set_object_value(board[random_column][random_row], "symbol", "S")
                    except IndexError:
                        continue
                elif board[random_column][random_row+1] == 'O':
                    try:
                        board[random_column+1][random_row+1] = set_object_value(board[random_column][random_row], "symbol", "S")
                    except IndexError:
                        continue
                elif board[random_column+1][random_row] == '0':
                    try:
                        board[random_column-1][random_row] = set_object_value(board[random_column][random_row], "symbol", "S")
                    except IndexError:
                        continue
                elif board[random_column+1][random_row] == '0':
                    try:
                        board[random_column+1][random_row] = set_object_value(board[random_column][random_row], "symbol", "S")
                    except IndexError:
                        continue
                chosen_set_of_ships.pop(0)
            else:
                board[random_column][random_row] = 'S'
                chosen_set_of_ships.pop(0)
    print(board)
    return board

def set_object_value(cell, index, value):
    cell[index] = value
    return cell 

def get_object_value(cell, index):
    return cell[index]

def check_nearest_ship():
    pass


def game_vs_player():
    pass

def game_vs_computer():
=======
    correct_data = False
    while correct_data == False:
        game_mode = input("""Select a game option
                1. Player vs Player
                2. Player vs Computer (level easy)
                3. Player vs AI (level medium)
                """))
        correct_data = state_input(game_mode)  
    return game_mode   

def state_input(user_input):
    if user_input == "1" or user_input == "2" or user_input == "3":
        return True
    else :     
        if len(user_input) != 1:
            print("Too many characters")                       
        else:
            print("The sign entered is out of range or not a digit")                
        print("""
            Try again
            """)
        return False
   

def board_size():
    board = []
    userinput = input("Please, choose field size:\n 1 - small\n 2 - standart\n 3 - big ")
    while userinput != 1 or userinput != 2 or userinput != 3:
        if userinput == '1': 
            for i in range(0,5):
                board.append(["O"]*5)
        if userinput == '2':
            for i in range(0,10):
                board.append(["O"]*5)
        if userinput == '3':
            for i in range():
                pass                                
def fields_output():
>>>>>>> 1ee8b5dd53ffc21df43ece3877e967c2fd599dde
    pass

def change_player():
    pass

def field_marking():
    pass

def check_hit_condition():
    pass

def check_win_condition():
    pass

def random_place_ships():
    pass

if __name__ == "__main__":
    main()
    choose_game_mode()