board = []
dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]

def inRange(y, x):
    if x < 0 or y < 0 or x > 4 or y > 4:
        return False
    return True


def hasWord(y, x, word):
    if not inRange(y, x):
        return False
    if board[y][x] != word[0]:
        return False
    if len(word) == 1:
        return True
    for direction in xrange(8):
        nextY = y + dy[direction]
        nextX = x + dx[direction]
        if hasWord(nextY, nextX, word[1:]):
            return True
    return False


C = input()
for _ in xrange(C):
    for i in xrange(5):
        a = list(raw_input())
        board.append(a)
    N = input()
    for l in range(N):
        s = raw_input()
        alreadyfound = False
        for j in xrange(5):
            if alreadyfound:
                break
            for k in xrange(5):
                if alreadyfound:
                    break
                if hasWord(j, k, s):
                    print s, 'YES'
                    alreadyfound = True
                    break
        if not alreadyfound:
            print s, 'NO'
                
