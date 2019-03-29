def search(path):
    """
    완전탐색
    """

    if len(path) == d + 1:
        if path[:-1] != q:
            return 0.0
        ret = 1.0
        for i in xrange(len(path) - 1):
            ret /= deg[path[i]]
        return ret

    else:
        ret = 0
        for j in xrange(n):
            if connected[path[:-1]][j]:
                path.append(j)
                ret += search(path)
                path.pop()
        return ret


def search2(here, days):
    """
    메모이제이션: search2(here, days) = 두니발 박사가 days일 째에 here번 마을에 숨어 있을 때, 마지막 날에 q번 마을에 있을 조건부 확률
    """

    if days == d:
        return 1.0 if here == q else 0.0

    if (here, days) in cache:
        return cache[(here, days)]

    ret = 0.0

    for there in xrange(n):
        if connected[here][there]:
            ret += search2(there, days + 1) / float(deg[here])

    cache[(here, days)] = ret
    return ret



def search3(here, days):
    """
    메모이제이션: search3(here, days) = 탈옥 후 days 째에 두니발 박사가 here번 마을에 숨어 있을 확률
    """

    if days == 0:
        return 1.0 if here == p else 0.0

    if (here, days) in cache:
        return cache[(here, days)]

    ret = 0.0

    for there in xrange(n):
        if connected[here][there]:
            ret += search3(there, days - 1) / float(deg[there])

    cache[(here, days)] = ret
    return ret


C = input()
for _ in xrange(C):
    n, d, p = list(map(int, raw_input().strip().split()))

    connected = []
    deg = []

    for _ in xrange(n):
        temp = list(map(int, raw_input().strip().split()))
        deg.append(temp.count(1))
        connected.append(temp)

    t = input()
    q = list(map(int, raw_input().strip().split()))

    cache = {}
    for i in xrange(t):
        print search3(q[i], d),
    print
