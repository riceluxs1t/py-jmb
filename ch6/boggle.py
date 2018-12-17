SIZE_OF_BOARD = 5
board = []
dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]


def in_range(y, x):
    return x >= 0 and y >= 0 and x <= 4 and y <= 4


def has_word(y, x, word):
    if not in_range(y, x):
        return False
    if board[y][x] != word[0]:
        return False
    if len(word) == 1:
        return True
    for direction in xrange(8):
        nextY = y + dy[direction]
        nextX = x + dx[direction]
        if has_word(nextY, nextX, word[1:]):
            return True
    return False


C = input()
for _ in xrange(C):
    for __ in xrange(SIZE_OF_BOARD):
        board.append(raw_input().strip())
    N = input()
    for __ in range(N):
        word_to_find = raw_input().strip()
        already_found = False
        for y in xrange(SIZE_OF_BOARD):
            for x in xrange(SIZE_OF_BOARD):
                if has_word(y, x, word_to_find):
                    print word_to_find, 'YES'
                    already_found = True
                    break
            else:
                continue
            break
        if not already_found:
            print word_to_find, 'NO'
                
