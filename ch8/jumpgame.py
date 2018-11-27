def jump(y, x):
	if y >= n or x >= n:
		return False
	if y == n - 1 and x == n - 1:
		return True

	if (y, x) in cache:
		return cache[(y, x)]

	jump_size = board[y][x]
	ret = jump(y + jump_size, x) or jump(y, x + jump_size)
	cache[(y, x)] = ret
	return ret


C = input()
for _ in xrange(C):
	n = input()
	board = []
	for _ in xrange(n):
		board.append(
			map(int, raw_input().strip().split())
		)

	cache = {}
	if jump(0, 0):
		print "YES"
	else:
		print "NO"
