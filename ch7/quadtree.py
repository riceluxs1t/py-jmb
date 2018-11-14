def reverse(quadtree, index):
	if quadtree[index] == 'b' or quadtree[index] == 'w':
		return (quadtree[index], index + 1)

	index += 1
	upper_left, index = reverse(quadtree, index)
	upper_right, index = reverse(quadtree, index)
	lower_left, index = reverse(quadtree, index)
	lower_right, index = reverse(quadtree, index)

	return "x" + lower_left + lower_right + upper_left + upper_right, index

C = input()

for _ in xrange(C):
	quadtree = raw_input().strip()
	reversed_quadtree, _ = reverse(quadtree, 0)
	print reversed_quadtree
