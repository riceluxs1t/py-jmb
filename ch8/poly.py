MOD = 10*1000*1000

def poly(n, first):
    if n == first:
        return 1

    if (n, first) in cache:
        return cache[(n, first)]

    ret = 0
    second = 1
    while second <= n - first:
        add = second + first - 1
        add *= poly(n - first, second)
        add %= MOD
        ret += add
        ret %= MOD
        second += 1

    cache[(n, first)] = ret
    return ret


C = input()
for _ in xrange(C):
    n = input()
    cache = {}
    result = 0
    for i in xrange(1, n + 1):
        result += poly(n, i)
    print result % MOD
