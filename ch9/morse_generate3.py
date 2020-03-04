
# initialize
M = 1000000000 + 100
bino = [[0] * 201 for x in xrange(201)]
skip = 0


def calcBino():
    for i in xrange(201):
        bino[i][0] = bino[i][i] = 1
        for j in xrange(1, i):
            bino[i][j] = min(M, bino[i - 1][j - 1] + bino[i - 1][j])
    

def generate3(n, m, s):
    global skip

    if skip < 0:
        return

    if n == 0 and m == 0:
        print s
        skip -= 1
        return

    if bino[n + m][n] <= skip:
        skip -= bino[n + m][n]
        return

    if n > 0:
        generate3(n - 1, m, s + '-')

    if m > 0:
        generate3(n, m - 1, s + 'o')


C = input()
for _ in xrange(C):
    n, m, k = map(int, raw_input().strip().split())
    skip = k - 1
    calcBino()
    generate3(n, m, "")