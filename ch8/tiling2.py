MOD = 1000000007
def tiling(width):
	if width <= 1:
		return 1

	if width in cache:
		return cache[width]

	ret = (tiling(width - 2) + tiling(width - 1)) % MOD
	cache[width] = ret
	return ret


C = input()
for _ in xrange(C):
	n = input()
	cache = {}
	print tiling(n) % MOD
