from collections import defaultdict
from math import log


def recognize(segment, previousMatch):
    if segment == n:
        return 0

    if cache[(segment, previousMatch)] != 1:
        return cache[(segment, previousMatch)]

    ret = -1e200

    for thisMatch in xrange(m):
        cand = T[previousMatch][thisMatch] + M[thisMatch][R[segment]] + recognize(segment + 1, thisMatch)

        if ret < cand:
            ret = cand
            choice[(segment, previousMatch)] = thisMatch

    cache[(segment, previousMatch)] = ret
    return ret


def reconstruct(segment, previousMatch):
    choose = choice[(segment, previousMatch)]
    ret = corpus[choose]

    if segment < n - 1:
        ret = ret + " " + reconstruct(segment + 1, choose)

    return ret




m, q = map(int, raw_input().strip().split())
corpus = raw_input().strip().split()
B = map(float, raw_input().strip().split())

for num in B:
    if num != 0:
        num = log(num)

T = []
for i in xrange(m + 1):
    if i == 0:
        T.append(B)
    else:
        T.append(map(log, map(float, raw_input().strip().split())))

M = []
for _ in xrange(m + 1):
    M.append(map(log, map(float, raw_input().strip().split())))

for _ in xrange(q):
    choice = {}
    cache = defaultdict(lambda: 1)

    input_sentence = raw_input().strip().split()
    n = int(input_sentence[0])
    input_sentence = input_sentence[1:]

    R = []

    for word in input_sentence:
        if word in corpus:
            R.append(corpus.index(word))

    recognize(0, 0)
    print reconstruct(0, 0)
