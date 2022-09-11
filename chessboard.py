size = 8
board = ''
for i in range(size):
    for j in range(size):
        if (i + j) % 2 == 0:
            board += ' '
        else:
            board += '#'
    board += '\n'
print(board)
