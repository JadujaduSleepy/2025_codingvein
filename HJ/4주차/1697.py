import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

visited = [0]*(100000+1)

q = deque()
q.append((n, 0))

while q:
    x, t = q.popleft()

    if x == k:   # 동생 위치라면
        break

    for dx in (-1, 1, x):
        nx = x + dx

        if nx == k:
            q.appendleft((nx, t+1))
            break

        if nx < 0 or nx > 100000:
            continue

        if not visited[nx]:
            q.append((nx, t+1))
            visited[nx] = 1

print(t)