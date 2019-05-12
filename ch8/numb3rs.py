def search(path):
    """
    Complete Search
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
    Memoization: search2(here, days) = the probability of Dr. Dunibal hiding in "q"th village, given that Dr. Dunibal hides in "here"th village on "days" day,
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
    Memoization: search3(here, days) = the probability of Dr. Dunibal hiding in "here"th village, given that "days" days have passed since jailbrek.
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
