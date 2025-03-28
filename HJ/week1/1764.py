## 시간초과남

import sys

N, M = map(int, sys.stdin.readline().split())

# 듣
names1 = [sys.stdin.readline().strip() for i in range(N)]

# 보
names2 = [sys.stdin.readline().strip() for i in range(M)]

# 듣보
names = sorted([name for name in names1 if name in names2])

print(len(names))
for name in names:
    print(name)


# # 조금 고쳐봤는데 이것도 시간초과임 
# import sys

# N, M = map(int, sys.stdin.readline().split())

# # 듣
# names1 = [sys.stdin.readline().strip() for i in range(N)]

# # 듣보목록
# names = []
# for i in range(M):
#     name = sys.stdin.readline().strip()
#     if name in names1:
#         names.append(name)

# names = sorted(names)

# print(len(names))
# s = ""
# for name in names:
#     s += name
# print(s)