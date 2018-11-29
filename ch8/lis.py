def lis(start):
	if start + 1 in cache:
		return cache[start + 1]

	ret = 1
	for next_ in xrange(start + 1, n):
		if start == -1 or S(start) < S(next_):
			ret = max(ret, lis(next_) + 1)

	cache[start] = ret
	return ret

def S(start):
	if start == -1:
		return float('-inf')
	else:
		return S_[start]


C = input()
for _ in xrange(C):
	n = input()
	cache = {}
	S_ = map(int, raw_input().strip().split())
	print lis(-1) - 1
