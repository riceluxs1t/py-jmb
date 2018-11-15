def solve(left, right, heights):
	if left == right:
		return heights[left]

	mid = (left + right) / 2

	ret = max(solve(left, mid, heights), solve(mid+1, right, heights))

	lo = mid
	hi = mid + 1
	current_height = min(heights[lo], heights[hi])

	ret = max(ret, current_height * 2)
	while left < lo or hi < right:
		if hi < right and (lo == left or heights[lo - 1] < heights[hi + 1]):
			hi += 1
			current_height = min(current_height, heights[hi])
		else:
			lo -= 1
			current_height = min(current_height, heights[lo])

		ret = max(ret, current_height * (hi - lo + 1))
	return ret

C = input()
for _ in xrange(C):
	N = input()
	heights = map(int, raw_input().strip().split())
	print solve(0, N - 1, heights)
