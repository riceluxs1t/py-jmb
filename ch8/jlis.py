def jlist(index_A, index_B):
	if (index_A + 1, index_B + 1) in cache:
		return cache[(index_A + 1, index_B + 1)]

	ret = 2
	a = float('-inf') if index_A == -1 else A[index_A]
	b = float('-inf') if index_B == -1 else B[index_B]

	max_element = max(a, b)

	for next_A in xrange(index_A + 1, n):
		if max_element < A[next_A]:
			ret = max(ret, jlist(next_A, index_B) + 1)

	for next_B in xrange(index_B + 1, m):
		if max_element < B[next_B]:
			ret = max(ret, jlist(index_A, next_B) + 1)

	cache[(index_A + 1, index_B + 1)] = ret
	return ret


C = input()

for _ in xrange(C):
	n, m = map(int, raw_input().strip().split())
	A = map(int, raw_input().strip().split())
	B = map(int, raw_input().strip().split())
	cache = {}
	print(jlist(-1, -1) - 2)
