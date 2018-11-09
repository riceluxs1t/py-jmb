from collections import defaultdict


def count_parings(taken, n):
	first_free = -1
	for i in xrange(n):
		if not taken[i]:
			first_free = i
			break

	if first_free == -1:
		return 1

	ret = 0
	for pair_with in xrange(first_free + 1, n):
		if not taken[pair_with] and are_friends(first_free, pair_with):
			taken[first_free] = True
			taken[pair_with] = True
			ret += count_parings(taken, n)
			taken[first_free] = False
			taken[pair_with] = False
	return ret

def are_friends(first_person, second_person):
	return _are_friends[(first_person, second_person)]


C = input()
for _ in xrange(C):
	n, m = map(int, raw_input().strip().split())
	_are_friends = defaultdict(bool)
	friends_relationships = map(int, raw_input().strip().split())
	for i in xrange(0, 2 * m, 2):
		first_person = friends_relationships[i]
		second_person = friends_relationships[i + 1]
		_are_friends[(first_person, second_person)] = True
		_are_friends[(second_person, first_person)] = True

	taken = [False] * n
	print count_parings(taken, n)
