def print_board(board):
    print('---------')
    for row in board:
        print('|', end=' ')
        for element in row:
            print(element, end=' ')
        print('|')
    print('---------')


def create_board():
    rows = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(' ')
        rows.append(row)
    return rows


def _check_rows(board, player, board_length):
    for i in range(board_length):
        win = True
        for j in range(board_length):
            if board[i][j] != player:
                win = False
                break
        if win:
            return win


def _check_columns(board, player, board_length):
    for i in range(board_length):
        win = True
        for j in range(board_length):
            if board[j][i] != player:
                win = False
                break
        if win:
            return win


def _check_diagonals(board, player, board_length):
    win = True
    for i in range(board_length):
        win = True
        if board[i][i] != player:
            win = False
            break
    if win:
        return win

    for i in range(board_length):
        win = True
        if board[i][board_length - 1 - i] != player:
            win = False
            break
    if win:
        return win
    return False


def is_win(board, player):
    if _check_rows(board, player, len(board)) \
            or _check_columns(board, player, len(board)) \
            or _check_diagonals(board, player, len(board)):
        return True
    else:
        return False


def is_draw(board):
    for row in board:
        for place in row:
            if place == ' ':
                return False
    return True


def count_signs(board):
    x_count = 0
    o_count = 0
    for row in board:
        for element in row:
            if element == 'X':
                x_count += 1
            elif element == 'O':
                o_count += 1
    return (x_count, o_count)


def enter_coordinates(board, player):
    while True:
        print('Enter the coordinates: ', end='')
        try:
            x, y = list(map(int, input().split()))
            if board[x - 1][y - 1] != ' ':
                print('This cell is occupied! Choose another one!')
            else:
                board[x - 1][y - 1] = player
                break
        except ValueError:
            print('You should enter numbers!')
        except IndexError:
            print('Coordinates should be from 1 to 3!')


def check_state(board):
    if is_win(board, 'X'):
        print('X wins')
        return True
    elif is_win(board, 'O'):
        print('O wins')
        return True
    elif is_draw(board):
        print('Draw')
        return True
    return False

def swap_player(player):
    if player == 'X':
        return 'O'
    return 'X'


def start():
    board = create_board()
    player = 'X'
    print_board(board)
    while True:
        enter_coordinates(board, player)
        print_board(board)
        player = swap_player(player)
        if check_state(board):
            break


if __name__ == '__main__':
    start()
