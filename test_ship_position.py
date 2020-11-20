def check_correct_positon (board, board_size, ship_size, user_row, user_column, ship_orientation):
    """sprawdza czy statek może zostać postawiony na wybranych współrzędnych
    - w pierwszym warunku sprawdza czy statek mieści się w tablicy
    - w drugim warunku sprawdza czy pola statku i pola sąsiadujące są wolne (x)
    jesli oba warunki sa spełnione zwraca True
    NIESTETY NIE DZIAŁA JESLI STATEK PRZYLEGA DO KRAWĘDZI - musze jeszcze to poprawić"""

    if ship_orientation == "horizontal" :
        test_count = 0
        if user_column + ship_size < board_size + 1:
            test_count +=1
        
        space_test = 0
        for row in range(user_row - 1, user_row + 2):
            for column in range (user_column -1, user_column + ship_size + 1):
                if board[row][column] == "0":
                    space_test += 1
        if space_test == (ship_size+2)*3:
            test_count +=1
        if test_count == 2:
            return True
        else :
            return False

def init_board(board):    
    for i in range(7):
        board.append(["0"]*7)
    
    return board
    
def show_board(board):
    for row in range(1,6):
        print()
        for column in range(1,6):
            print(board[row][column], end="")
    print()

def get_ship_orientation() :
    print(""" Chose ship orientation :
                1. Horizonatl
                2. Vertical        
            """)
    ship_orientation = input("Your choice is (1 or 2):")
    if ship_orientation == "1":
        ship_orientation = "horizontal"
    elif ship_orientation == "2":
        ship_orientation = "vertical"
    return ship_orientation

def get_ship_coridnates():

    print("""Chose ship`s position (first field).
            Row - (from A to E)
            Column (from 1 to 5))
            """)
    ship_cordinates = input()
    user_column = int(ship_cordinates[1])
    user_row = int(ship_cordinates[0])
    return user_row, user_column

def mark_ships(board, ship_size, ship_orientation, user_row, user_column):
    if ship_orientation == "horizontal":
        for column in range(user_column, user_column + ship_size + 1):
            board[user_row][column] = "X"
    if ship_orientation == "vertical":
        for row in range(user_row, user_row + ship_size):
            board[row][user_column] = "X"


board = []
board_size = 5
ship_size = 2
init_board(board)
show_board(board)
ship_orientation = get_ship_orientation()
user_row, user_column = get_ship_coridnates()

if check_correct_positon(board, board_size, ship_size, user_row, user_column, ship_orientation) is True:
    mark_ships(board, ship_size, ship_orientation, user_row, user_column)
else:
    print("you cant")

show_board(board)