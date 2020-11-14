import os
import time
import math
from random import randint

player = 1
board = []
chosen_set_of_ships = []
ship_sets = ['S', 'SS', 'SSS', 'SSSS']

def main():                                              # consistent main function
    os.system("cls || clear")
    print("Let's the seabattle begins!")
    time.sleep(1)
    choose_game_mode()
    board_size(board)
    print_board(board) 
    print(chosen_set_of_ships)
    placement_phase(board, player) 
    player_1_board = board
    player_2_board = []
    time.sleep(3)
    os.system("cls || clear")
    awaiting_function(2) 
    placement_phase(player_2_board, 2)

def awaiting_function(player):                           # funcion provides waiting for another player's action
    """funcion provides waiting for another player's action"""               
    input(f"Press any key to start player {player} ships placement phase")
    
def choose_game_mode():                                  # function for choosing game mode Pl vs Pl or Pl vs AI
    """ function for choosing game mode Pl vs Pl or Pl vs AI """

    user_game_mode = input("Please, choose game mode:\n 1 - Player vs Player\n 2 - Player vs AI")
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

def board_size(board):                                   # function for choosing board size and ship for actual board
    """
    function for choosing board size and ship for actual board
    """
    os.system("cls || clear")  
    userinput = input("Please, choose board size:\n 1 - small (5*5)\n 2 - regular (10*10)\n 3 - big (15*15) ")
    if userinput == '1':  
        for row in range(0, 5):                           #quantity os "S" = 3
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

def placement_phase(board, player):                      # function for placing ships on the board
    """ function for placing ships on the board """
    print (f"Player {player} ship placement phase")
    for ship in range(0, len(chosen_set_of_ships)): 
        print(f"Please, provide data to place your '{chosen_set_of_ships[-1]}' ship ")

        input_row = int(input("Please, input row number "))
        input_column = int(input("Please, input column number "))

        if board[input_row][input_column] == 'O' and int(len(chosen_set_of_ships[-1])) > 1:

            input_direction = input("Please, provide ship direction horizontal or vertical H/V ")
            board[input_row][input_column] = 'X' 

            if input_direction == 'V' and (input_row == 0 and input_column == 0) or (input_row == 0 and input_column == 4):
                try: 
                    board[abs(input_row - 1)][input_column] = 'X'
                except IndexError:
                    board[input_row + 1][input_column] = 'X'
            elif input_direction == 'H':
                try: 
                    board[input_row][input_column+1] = 'X'
                except IndexError:
                    board[input_row][abs(input_column-1)] = 'X'
            else:
                try: 
                    board[input_row - 1][input_column] = 'X'
                except IndexError:
                    board[input_row + 1][input_column] = 'X'
            
            chosen_set_of_ships.pop(-1)
            print_board(board)
            print(f"Ships to place: {chosen_set_of_ships}")

        elif board[input_row][input_column] == 'O' and int(len(chosen_set_of_ships[-1])) > 0:
            board[input_row][input_column] = 'X' 
            chosen_set_of_ships.pop(-1)
            print(f"Ships to place: {chosen_set_of_ships}")
            print_board(board)
            player += 1 

    return board, player 

def print_board(board):                                  # function printing actual condition of board
    """ function printing actual condition of board """
    for row in board: 
        print(" ".join(row))        

def mark_nearby_cells(board, parameter_list):
    """
    function for marking nearby sells
    """
pass


if __name__ == "__main__":
    main()