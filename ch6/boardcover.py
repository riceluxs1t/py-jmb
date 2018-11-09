COVER_TYPE = [
	[(0, 0), (1, 0), (0, 1)],
	[(0, 0), (0, 1), (1, 1)],
	[(0, 0), (1, 0), (1, 1)],
	[(0, 0), (1, 0), (1, -1)]
]

def set(board, y, x, type_, delta):
	ok = True

	for i in xrange(0, 3):
		ny = y + COVER_TYPE[type_][i][0]
		nx = x + COVER_TYPE[type_][i][1]
		if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board[0]):
			ok = False
			continue
		board[ny][nx] += delta
		if board[ny][nx] > 1:
			ok = False

	return ok

def cover(board):
	y = -1
	x = -1

	for i in xrange(len(board)):
		for j in xrange(len(board[i])):
			if board[i][j] == 0:
				y = i
				x = j
				break
		if y != -1:
			break

	if y == -1:
		return 1

	ret = 0
	for type_ in xrange(4):
		if set(board, y, x, type_, 1):
			ret += cover(board)

		set(board, y, x, type_, -1)

	return ret


C = input()
for _ in xrange(C):
	H, W = map(int, raw_input().strip().split())
	board = []
	for _ in xrange(H):
		row = raw_input().strip()
		row = row.replace('#', '1')
		row = row.replace('.', '0')
		row = map(int, list(row))
		board.append(row)

	print cover(board)
