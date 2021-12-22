def print_board(board):
    print('---------')
    for row in board:
        print('|', end=' ')
        for element in row:
            print(element, end=' ')
        print('|')
    print('---------')


def create_board(cells):
    rows = []
    n = 0
    for i in range(3):
        row = []
        for j in range(3):
            row.append(cells[j + n])
        rows.append(row)
        n += 3
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
            if place == '_':
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


cells = input()
board = create_board(cells)
x_o = count_signs(board)
print_board(board)
if (x_o[0] - x_o[1]) == 2 or (x_o[1] - x_o[0]) == 2 or is_win(board, 'X') and is_win(board, 'O'):
    print('Impossible')
elif is_win(board, 'X'):
    print('X wins')
elif is_win(board, 'O'):
    print('O wins')
elif is_draw(board):
    print('Draw')
else:
    print('Game not finished')