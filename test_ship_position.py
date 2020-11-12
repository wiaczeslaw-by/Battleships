def check_correct_positon (board,board_size, ship_size,user_row, user_col, ship_orientation):
    """sprawdza czy statek może zostać postawiony na wybranych współrzędnych
    - w pierwszym warunku sprawdza czy statek mieści się w tablicy
    - w drugim warunku sprawdza czy pola statku i pola sąsiadujące są wolne (x)
    jesli oba warunki sa spełnione zwraca True
    NIESTETY NIE DZIAŁA JESLI STATEK PRZYLEGA DO KRAWĘDZI - musze jeszcze to poprawić"""

    if ship_orientation = "horizontal" :
        test_count = 0
        if user_col + ship_size <= board_size + :
            test_count +=1
        
        space_test = 0
        for row in range(user_row - 1, user_row + 1):
            for column in range (user_col -1, user_col + 1):
                if board[row][column] == "x"
                space_test += 1
        if space_test == (ship_size+2)*2+2:
            test_count +1 = 0
        if test_count == 2:
            return True
        else :
            return False
