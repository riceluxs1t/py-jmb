def match_pattern(w, s):
	if (w, s) in cache:
		return cache[(w, s)]
	while s < len(S) and w < len(W) and (W[w] == '?' or W[w] == S[s]):
		w += 1
		s += 1

	if w == len(W):
		cache[(w, s)] = (s == len(S))
		return cache[(w, s)]
	
	if W[w] == '*':
		skip = 0
		while skip + s <= len(S):
			if match_pattern(w + 1, s + skip):
				cache[(w, s)] = True
				return True
			skip += 1

	cache[(w, s)] = False
	return False

def match_pattern_smart(w, s):
	if (w, s) in cache:
		return cache[(w, s)]
	
	if s < len(S) and w < len(W) and (W[w] == '?' or W[w] == S[s]):
		cache[(w, s)] = match_pattern_smart(w + 1, s + 1)
		return cache[(w, s)]

	if w == len(W):
		cache[(w, s)] = (s == len(S))
		return cache[(w, s)]
	
	if W[w] == '*':
		if match_pattern_smart(w + 1, s) or (s < len(S) and match_pattern_smart(w, s + 1)):
			cache[(w, s)] = True
			return True
		
	cache[(w, s)] = False
	return False


C = input()
for _ in xrange(C):
	W = raw_input().strip()
	n = input()
	matches = []
	for _ in xrange(n):
		S = raw_input().strip()
		cache = {}
		if match_pattern_smart(0, 0):
			matches.append(S)

	matches.sort()
	for match in matches:
		print match
