def create_board():
    cells = input()
    print('---------')
    for i in range(1, 10):
        if i == 1 or i == 4 or i == 7:
            print('| ', end='')
        print(cells[i - 1], end=' ')
        if i % 3 == 0:
            print('|')
    print('---------')


create_board()