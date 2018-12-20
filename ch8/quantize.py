def precalc():
	A.sort()
	p_sum.append(A[0])
	p_square_sum.append(A[0] * A[0])
	for i in xrange(1, N):
		p_sum.append(p_sum[i - 1] + A[i])
		p_square_sum.append(p_square_sum[i - 1] + (A[i] * A[i]))

def min_error(lo, hi):
	sum_ = p_sum[hi]
	if lo != 0:
		sum_ = sum_ - p_sum[lo - 1]

	square_sum = p_square_sum[hi]
	if lo != 0:
		square_sum = square_sum - p_square_sum[lo - 1]

	m = int(0.5 + float(sum_) / (hi - lo + 1))

	ret = square_sum - (2 * m * sum_) + (m * m * (hi - lo + 1))
	return ret

def quantize(from_, parts):
	if from_ == N:
		return 0

	if parts == 0:
		return float('inf')

	if (from_, parts) in cache:
		return cache[(from_, parts)]

	ret = float('inf')

	part_size = 1
	while from_ + part_size <= N:
		ret = min(
			ret,
			min_error(from_, from_ + part_size - 1) + 
			quantize(from_ + part_size, parts - 1)
		)
		part_size += 1

	cache[(from_, parts)] = ret
	return ret


C = input()
for _ in xrange(C):
	N, S = map(int, raw_input().strip().split())
	A = map(int, raw_input().strip().split())
	p_sum = []
	p_square_sum = []
	cache = {}
	precalc()
	print quantize(0, S)

