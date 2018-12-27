def path(y, x):
	if y == n - 1:
		return triangle[y][x]

	if (y, x) in cache_path:
		return cache_path[(y, x)]

	ret = max(path(y + 1, x), path(y + 1, x + 1)) + triangle[y][x]
	cache_path[(y, x)] = ret
	return ret

def count(y, x):
	if y == n - 1:
		return 1

	if (y, x) in cache_count:
		return cache_count[(y, x)]

	ret = 0

	if path(y + 1, x + 1) >= path(y + 1, x):
		ret += count(y + 1, x + 1)

	if path(y + 1, x + 1) <= path(y + 1, x):
		ret += count(y + 1, x)

	cache_count[(y, x)] = ret
	return ret


C = input()
for _ in xrange(C):
	n = input()
	triangle = []
	cache_path = {}
	cache_count = {}
	for _ in xrange(n):
		row = map(int, raw_input().strip().split())
		row = [element for element in row if element != '']
		triangle.append(row)
	print count(0, 0)
