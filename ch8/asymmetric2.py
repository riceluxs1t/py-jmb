MOD = 1000000007

def tiling(width):
    if width <= 1:
        return 1

    if width in cache:
        return cache[width]

    ret = (tiling(width - 2) + tiling(width - 1)) % MOD

    cache[width] = ret
    return ret


def asymmetric2(width):
    if width <= 2:
        return 0

    if width in cache2:
        return cache2[width]

    ret = asymmetric2(width - 2) % MOD
    ret = (ret + asymmetric2(width - 4)) % MOD
    ret = (ret + tiling(width - 3)) % MOD
    ret = (ret + tiling(width - 3)) % MOD

    cache2[width] = ret
    return ret


C = input()
for _ in xrange(C):
    n = input()
    cache = {}
    cache2 = {}
    print asymmetric2(n)
