import os
import time
import random

def main():
    print("Let's the seabattle begins!")
    time.sleep(1)
    field_size() 

def choose_game_mode():
    pass   

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
                                 


def fields_output():
    return 

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