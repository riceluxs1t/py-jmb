from collections import defaultdict
from math import log


def recognize(segment, previousMatch):
    if segment == n:
        return 0

    if cache[(segment, previousMatch)] != 1:
        return cache[(segment, previousMatch)]

    ret = -1e200

    for thisMatch in xrange(m):
        cand = T[previousMatch][thisMatch] + M[thisMatch][R[segment]] + recognize(segment + 1, thisMatch + 1)

        if ret < cand:
            ret = cand
            choice[(segment, previousMatch)] = thisMatch

    cache[(segment, previousMatch)] = ret
    return ret


def reconstruct(segment, previousMatch):
    choose = choice[(segment, previousMatch)]
    ret = corpus[choose]

    if segment < n - 1:
        ret = ret + " " + reconstruct(segment + 1, choose + 1)

    return ret





m, q = map(int, raw_input().strip().split())
corpus = raw_input().strip().split()

B = map(float, raw_input().strip().split())
for i in xrange(m):
    B[i] = float('-inf') if B[i] == 0 else log(B[i])

T = []
T.append(B)
for i in xrange(m):
    C = map(float, raw_input().strip().split())
    for j in xrange(m):
        C[j] = float('-inf') if C[j] == 0 else log(C[j])
    T.append(C)

M = []
for _ in xrange(m):
    D = map(float, raw_input().strip().split())
    for i in xrange(m):
        D[i] = float('-inf') if D[i] == 0 else log(D[i])
    M.append(D)


for _ in xrange(q):
    choice = defaultdict(lambda: 1)
    cache = defaultdict(lambda: 1)

    input_sentence = raw_input().strip().split()
    n = int(input_sentence[0])
    input_sentence = input_sentence[1:]

    R = [corpus.index(i) for i in input_sentence]

    recognize(0, 0)
    print reconstruct(0, 0)
