MOD = 1000000007

def tiling(width):
    if width <= 1:
        return 1

    if width in cache:
        return cache[width]

    ret = (tiling(width - 2) + tiling(width - 1)) % MOD

    cache[width] = ret
    return ret


def asymmetric(width):
    if width % 2 == 1:
        return (tiling(width) - tiling(width/2) + MOD) % MOD

    ret = tiling(width)
    ret = (ret - tiling(width/2) + MOD) % MOD
    ret = (ret - tiling(width/2 - 1) + MOD) % MOD

    return ret


C = input()
for _ in xrange(C):
    n = input()
    cache = {}
    print asymmetric(n)
