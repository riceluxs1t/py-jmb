def hugs(members, fans):
	n = len(members)
	m = len(fans)

	aList = [0] * n
	for i in xrange(n):
		if members[i] == 'M':
			aList[i] = 1

	bList = [0] * m
	for i in xrange(m):
		if fans[i] == 'M':
			bList[m - i - 1] = 1

	cList = karatsuba(aList, bList)
	all_hugs = 0

	for i in xrange(n - 1, m):
		if cList[i] == 0:
			all_hugs += 1

	return all_hugs

def karatsuba(aList, bList):
	n = len(bList)
	m = len(aList)

	if m < n:
		return karatsuba(bList, aList)

	if m == 0 or n == 0:
		return []

	if m <= 50:
		return multiply(aList, bList)

	half = m / 2

	a0 = aList[: half]
	a1 = aList[half: ]
	b0 = bList[: min(n, half)]
	b1 = bList[min(n, half): ]

	z2 = karatsuba(a1, b1)
	z0 = karatsuba(a0, b0)

	addTo(a0, a1, 0)
	addTo(b0, b1, 0)

	z1 = karatsuba(a0, b0)
	subFrom(z1, z0)
	subFrom(z1, z2)

	result = []

	addTo(result, z0, 0)
	addTo(result, z1, half)
	addTo(result, z2, half + half)

	return result

def addTo(aList, bList, k):
	n = len(bList)
	m = len(aList)
	# increase the capacity of aList.
	if n + k > m:
		diff = n + k - m
		for _ in xrange(diff):
			a.append(0)

	for i in xrange(n):
		a[i + k] += b[i]

def subFrom(aList, bList):
	n = len(bList)
	m = len(aList)

	if n > m:
		diff = n - m
		for _ in xrange(diff):
			a.append(0)
	a.append(0)

	for i in xrange(n):
		a[i] -= b[i]

def multiply(aList, bList):
	n = len(bList)
	m = len(aList)

	c = [0] * (m + n + 1)

	for i in xrange(m):
		for j in xrange(n):
			c[i + j] += aList[i] * bList[j]

	return c


C = input()
for _ in xrange(C):
	members = raw_input().strip()
	fans = raw_input().strip()
	print hugs(members, fans)
