from collections import defaultdict

def classify(a, b):
	M = N[a : b + 1]

	if M == M[0] * len(M):
		return 1

	progressiveness = True
	for i in xrange(len(M) - 1):
		if int(M[i + 1]) - int(M[i]) != int(M[1]) - int(M[0]):
			progressiveness = False

	if progressiveness and abs(int(M[1]) - int(M[0])) == 1:
		return 2

	alternating = True
	for i in xrange(len(M)):
		if int(M[i]) != int(M[i % 2]):
			alternating = False

	if alternating:
		return 4

	if progressiveness:
		return 5

	return 10

def memorize(begin):
	if begin == len(N):
		return 0

	if begin in cache:
		return cache[begin]

	ret = float('inf')

	for L in xrange(3, 6):
		if begin + L <= len(N):
			ret = min(
				ret, 
				memorize(begin + L) + classify(begin, begin + L - 1)
			)

	cache[begin] = ret
	return ret

C = input()
for _ in xrange(C):
	N = raw_input().strip()
	cache = defaultdict(int)
	print memorize(0)
