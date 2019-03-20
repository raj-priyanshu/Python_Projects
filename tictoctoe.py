from typing import List, Union
import random

layout = (
    "┏━━━┳━━━┳━━━┓\n"
    "┃ {0} ┃ {1} ┃ {2} ┃\n"
    "┣━━━╋━━━╋━━━┫\n"
    "┃ {3} ┃ {4} ┃ {5} ┃\n"
    "┣━━━╋━━━╋━━━┫\n"
    "┃ {6} ┃ {7} ┃ {8} ┃\n"
    "┗━━━┻━━━┻━━━┛")

status: List[Union[int, str]] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

used_postion = set()


def print_board(layout_, status_):
    print(layout_.format(*status_))
    return None


def select_char():
    chars = ('X', 'O')
    if random.randint(0, 1) == 0:
        return chars[::-1]
    return chars


def player_move(status_, char_):
    try:
        user_ip = input("Enter board position: ")
        position_ = int(user_ip)
        while position_ in used_postion:
            user_ip = input("Already used input. \n Enter new board position: ")
            position_ = int(user_ip)
        used_postion.add(position_)
        status_[position_ - 1] = char_
        return status_
    except ValueError:
        print('Please enter a valid position.')
        player_move(status_, char_)


def win_check():
    for elem in winners:
        if status[elem[0]] == status[elem[1]] == status[elem[2]]:
            return  status[elem[0]]
    return None


print_board(layout, status)
character = select_char()
move_available = 9
x = move_available + 1
is_draw=True
while move_available:
    player_move(status, character[(x % 2)])
    move_available = move_available - 1
    x = move_available + 1
    print_board(layout, status)
    temp = win_check()
    if temp:
        print(f'player {temp} has won the game.')
        is_draw=False
        break

if is_draw:
	print('Game is draw.')
