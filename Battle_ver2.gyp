import os
import time
from random import randint


ship_sets = ['S', 'SS', 'SSS', 'SSSS']
chosen_set_of_ships = []
board = []

def main():
    os.system("cls || clear")
    print("Let's the seabattle begins!")
    time.sleep(1)
    choose_game_mode()
    board_size(board)
    print_board(board)
    print(chosen_set_of_ships)
    random_ship_placement()

def choose_game_mode():
    user_game_mode = input("Please, choose game mode:\n 1 - Player vs Player\n 2 - Player vs Comp ")
    if user_game_mode == '1':
        player = '1'
        return player
    elif user_game_mode == '2':
        computer = '2'
        return computer         
    else:
        os.system("cls || clear")
        print("Input correct data and try again")
        time.sleep(1)
        choose_game_mode()

def board_size(board):                                   #function for choosing board size and ship_set according to it
    os.system("cls || clear")  
    userinput = input("Please, choose board size:\n 1 - small (5*5)\n 2 - regular (10*10)\n 3 - big (15*15)")
    if userinput == '1':  
        for row in range(0, 5):                         #quantity os "S" = 3
            board.append(['O'] * 5)
        for ship in range(3):
            chosen_set_of_ships.append(ship_sets[0])
        chosen_set_of_ships.append(ship_sets[1])        #quantity os "SS" = 1
    elif userinput == '2':
        for row in range(0, 10):
            board.append(['O'] * 10)
        for ship in range(4):                            #quantity os "S" = 4      
            chosen_set_of_ships.append(ship_sets[0])
        for ship in range(3):                            #quantity os "SS" = 3
            chosen_set_of_ships.append(ship_sets[1])
        for ship in range(2):                            #quantity os "SSS" = 2
            chosen_set_of_ships.append(ship_sets[2])
        chosen_set_of_ships.append(ship_sets[3])         #quantity os "SSSS" = 1
    elif userinput == '3':
        for row in range(0, 15): 
            board.append(['0'] * 15)
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
        time.sleep(1)
    return board, chosen_set_of_ships 


# if col+1 > len(row):
# try another side
                                

def print_board(board):
    for row in board: 
        print(" ".join(row))

def random_ship_placement():
    ship_placed = 0
    remaining_ships_to_place = chosen_set_of_ships
    while remaining_ships_to_place != []:
        for ship in range(0, len(chosen_set_of_ships)):
            while ship_placed <= len(chosen_set_of_ships):
                random_row = randint(0,len(board) - 1)
                random_column = randint(0,len(board) - 1)
                if len(chosen_set_of_ships[len(chosen_set_of_ships)]) > 1 and board[random_row][random_column] == 'O':
                    board[random_row][random_column] = chosen_set_of_ships[len(chosen_set_of_ships)]
                    try:
                        mark_nearest_cell(board, random_row, random_column)
                    except IndexError:
                        break
                    chosen_set_of_ships.pop(0)
                    ship_placed += 1
                elif len(chosen_set_of_ships[0]) > 2 and board[random_row][random_column] == 'O':
                    board[random_row][random_column] = chosen_set_of_ships[0][0]
                    chosen_set_of_ships.pop(0)
                elif len(chosen_set_of_ships[0]) > 1 and board[random_row][random_column] == 'O':
                    pass            
        print_board(board)
        return board

def check_nearest_ship(board, random_row, random_column):
    try:
        board[random_row-1][random_column-1] = 'o'
        board[random_row-1][random_column] = 'o'
        board[random_row-1][random_column+1] = 'o'
        board[random_row+1][random_column-1] = 'o'                      
        board[random_row+1][random_column] = 'o'
        board[random_row+1][random_column+1] = 'o'
        board[random_row][random_column-1] = 'o'
        board[random_row][random_column+1] = 'o'
    except IndexError:
        pass      
    return board


def game_vs_player():
    pass

def game_vs_computer():
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