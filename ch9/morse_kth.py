# initialize
M = 1000000000 + 100
bino = [[0] * 201 for x in xrange(201)]


def calcBino():
    for i in xrange(201):
        bino[i][0] = bino[i][i] = 1
        for j in xrange(1, i):
            bino[i][j] = min(M, bino[i - 1][j - 1] + bino[i - 1][j])
    

def kth(n, m, skip):
    if n == 0:
        return 'o' * m

    if skip < bino[n + m - 1][n - 1]:
        return '-' + kth(n - 1, m, skip)

    return 'o' + kth(n, m - 1, skip - bino[n + m - 1][n - 1])


C = input()
for _ in xrange(C):
    n, m, k = map(int, raw_input().strip().split())
    skip = k - 1
    calcBino()
    print kth(n, m, skip)