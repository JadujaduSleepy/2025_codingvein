import sys
input = sys.stdin.readline

from collections import deque

m, n = map(int, input().split())

# 처음부터 익은 토마토
q = deque()

tomatos = [0]*n
for i in range(n):
    tomatos[i] = list(map(int, input().split()))
    for j in range(m):
        if tomatos[i][j] == 1:
            q.append((i, j))

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

while q:
    y, x = q.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if not(0 <= nx < m and 0 <= ny < n):
            continue

        if tomatos[ny][nx] == -1:
            continue

        if not tomatos[ny][nx]:
            tomatos[ny][nx] = tomatos[y][x] + 1
            q.append((ny, nx))


result = max(tomatos[0])   # local maximum
for row in tomatos:
    if 0 in row:
        result = 0
        break
    else:
        if max(row) > result:
            result = max(row)

print(result-1)