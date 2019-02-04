import sys
sys.setrecursionlimit(10000)


def climb(days, climbed):
    if days == m:
        return 1 if climbed >= n else 0
    if (days, climbed) in cache:
        return cache[(days, climbed)]
    ret = 0.25*climb(days + 1, climbed + 1) + 0.75*climb(days + 1, climbed + 2)
    cache[(days, climbed)] = ret
    return ret


C = input()
for _ in xrange(C):
    n, m = list(map(int, raw_input().split()))
    cache = {}
    print climb(0, 0)
