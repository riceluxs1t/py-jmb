def path(y, x):
	if y == n - 1:
		return triangle[y][x]

	if (y, x) in cache:
		return cache[(y, x)]

	ret = max(path(y + 1, x), path(y + 1, x + 1)) + triangle[y][x]
	cache[(y, x)] = ret
	return ret


C = input()
for _ in xrange(C):
	n = input()
	triangle = []
	cache = {}
	for _ in xrange(n):
		row = map(int, raw_input().strip().split())
		row = [element for element in row if element != '']
		triangle.append(row)
	print path(0, 0)
