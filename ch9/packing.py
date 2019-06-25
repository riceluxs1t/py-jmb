def pack(capacity, item):
    if item == N:
        return 0

    if (capacity, item) in cache:
        return cache[(capacity, item)]

    ret = pack(capacity, item + 1)

    if capacity >= things[item][1]:
        ret = max(ret, pack(capacity - things[item][1], item + 1) + things[item][2])
    cache[(capacity, item)] = ret

    return ret


def reconstruct(capacity, item):
    if item == N:
        return

    if pack(capacity, item) == pack(capacity, item + 1):
        reconstruct(capacity, item + 1)

    else:
        picked.append(things[item][0])
        reconstruct(capacity - things[item][1], item + 1)


C = input()
for _ in xrange(C):
    N, W = map(int, raw_input().strip().split())

    things = [] # list of tuples -> (name, volume, need)
    cache = {}
    picked = []

    for _ in xrange(N):
        name, vol, need = raw_input().strip().split()
        vol = int(vol)
        need = int(need)
        things.append((name, vol, need))

    reconstruct(W, 0)

    print cache[(W, 0)], len(picked)
    for x in picked:
        print x
