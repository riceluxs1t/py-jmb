def pack(capacity, item):
    if item == n:
        return 0

    if (capacity, item) in cache:
        return cache[(capacity, item)]

    ret = pack(capacity, item + 1)

    if capacity >= volume[item]:
        ret = max(ret, pack(capacity - volume[item], item + 1) + need[item])

    cache[(capacity, item)] = ret
    return ret


def reconstruct(capacity, item, picked):
    if item == n:
        return

    if pack(capacity, item) == pack(capacity, item + 1):
        reconstruct(capacity, item + 1, picked)

    else:
        picked.append(name[item])
        reconstruct(capacity - volume[item], item + 1, picked)


C = input()
for _ in xrange(C):
    name = []
    volume = []
    need = []
    cache = {}

    n, w = list(map(int, raw_input().strip().split()))
    for _ in xrange(n):
        a, b, c = raw_input().strip().split()
        b = int(b)
        c = int(c)
        name.append(a)
        volume.append(b)
        need.append(c)

    final_pack = []
    reconstruct(w, 0, final_pack)
    print cache[(w, 0)], len(final_pack)
    for thing in final_pack:
        print thing
