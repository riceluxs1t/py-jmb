# 프로그래밍 대회에서 배우는 알고리즘 문제 해결 전략 in Python

주변 사람들에게 열심히 소위 JMB 이란 책을 전파하는 개발자입니다.
책을 처음 접했을 때의 기쁨을 다른 사람들에게도 알리고 싶었습니다.

하지만...

- "C++ 를 몰라서 예제 코드가 이해가 안되요.."
- "C++만 알았다면.. 좀 더 개념 이해가 잘 되었을 텐데 아쉬워요."
- "실제로 예제 솔루션을 제출 해보고 싶은데..입출력 부분이 빠져 있어요.."

등등의 안타까운 피드백등이 많았죠.

놀랍게도, 저자에게 책의 예제를 파이썬으로 다시 쓴 코드를 공유해도 된다는 허락을 받았습니다. 

그래서 탄생했습니다. **PyJMB**

## PyJMB
- pep8 을 지키는 클린 코드
- Python 2.7
- 챕터별 예제 문제의 C++ 소스 코드를 최대한 Pythnoic 하게 옮김
- 개별 문제의 파이썬 소스코드는 그대로 긁어서 제출 가능

## Example
### C++
```c++
// 생략 된 함수 헤더

const int coverType[4][3][2] = {
	{ { 0, 0 }, { 1, 0 }, { 0, 1 } },
	{ { 0, 0 }, { 0, 1 }, { 1, 1 } },
	{ { 0, 0 }, { 1, 0 }, { 1, 1 } },
	{ { 0, 0 }, { 1, 0 }, { 1, -1 }}
};

bool set(vector<vector<int> >& board, int y, int x, int type, int delta) {
	bool ok = true;
	for(int i = 0; i < 3; i++) {
		const int ny = y + coverType[type][i][0];
		const int nx = x + coverType[type][i][1];
		if(ny < 0 || ny >= board.size() || nx < 0 || nx >= board[0].size())
			ok = false;
		else if ((board[ny][nx] += delta) > 1)
			ok = false;
	}
	return ok;
}

int cover(vector<vector<int> >& board) {
	int y = -1, x = -1;
	for(int i = 0; i < board.size(); ++i) {
		for(int j = 0; j < board[i].size(); ++j) {
			if(board[i][j] == 0) {
				y = i;
				x = j;
				break;
			}
		}
		if (y != -1) break;
	}

	if(y == -1) return 1;
	int ret = 0;
	for(int type = 0; type < 4; ++type) {
		if(set(board, y, x, type, 1))
			ret += cover(board);
		set(board, y, x, type, -1);
	}
	return ret;
}

// 생략 된 입출력
```

### Python2.7
```python
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

# 추가 된 입출력
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
```

