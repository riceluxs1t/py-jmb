from collections import defaultdict


SIZE_OF_BOARD = 5
MAX_NUM_OF_ALPHABET_PER_WORD = 10
dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]


def in_range(y, x): 
    return x >= 0 and y >= 0 and x <= 4 and y <= 4


def has_word(y, x, word, cur_index, cache):
    if not in_range(y, x):
        return False

    cache[(y, x, cur_index)] = 1

    if board[y][x] != word[cur_index]:
        return False
    if cur_index == len(word) - 1:
        return True
    
    for direction in xrange(8):
        next_y = y + dy[direction]
        next_x = x + dx[direction]
        if not in_range(next_y, next_x):
            continue
        if cache[(next_y, next_x, cur_index + 1)]:
            continue
        if has_word(next_y, next_x, word, cur_index + 1, cache):
            return True
    return False


for _ in xrange(int(raw_input())):
    board = [] # board has to be emptied at the beginning of every test case
    for _ in xrange(SIZE_OF_BOARD):
        board.append(raw_input().strip())
    for _ in xrange(int(raw_input())):
        cache = defaultdict(int) # cache has to be emptied for every word.
        word_to_find = raw_input().strip()
        already_found = False
        for y in xrange(SIZE_OF_BOARD):
            for x in xrange(SIZE_OF_BOARD):
                if has_word(y, x, word_to_find, 0, cache):
                    print word_to_find, 'YES'
                    already_found = True
                    break
            if already_found:
                break
        if not already_found:
            print word_to_find, 'NO'
                
