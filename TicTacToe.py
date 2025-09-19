import random

print('Добро пожаловать в игру Крестики-Нолики!')

def player_input():
    player1 = input("Пожалуйста выберите символ 'X' или 'O'")
    pass


#решаем кто ходит первым
def choose_first():
    pass

#очистка между ходами
from IPython.display import clear_output
clear_output()

#вывод доски
def display_board(board):
    test_board = ['#','X','O','X','O','X','O','X','O','X']
    display_board(test_board)
    pass

#проверка на пустое место для хода
def space_check(board, position):
    
    pass

#запрашиваем ход у игрока (позиция 1-9)
def player_choice(board):

    space_check(board, position)
    place_marker(board, marker, position)

    pass

#поставить символ на доску
def place_marker(board, marker, position):
    
    pass

place_marker(test_board,'$',8)
display_board(test_board)

#проверка на выигрыш
def win_check(board, mark):
    
    pass

#проверка на полное заполнение поля
def full_board_check(board):
    
    pass

#перезапуск игры по желанию пользователя
def replay():
    
    pass

#while True:
    # Настройка игры
    #pass

    #while game_on:
        # Ход Игрока 1
        
        
        # Ход Игрока 2
            
            #pass

    #if not replay():
        #break