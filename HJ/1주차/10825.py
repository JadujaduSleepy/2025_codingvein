N = int(input()) # 첫번째줄 입력
students = [0 for i in range(N)] # N개 길이 리스트 초기화

# 이중리스트로 저장
for i in range(N):
    students[i] = input().split()
    students[i][1:] = map(int, students[i][1:]) # 점수들 숫자로 바꾸기

# 정렬
students = sorted(students, key=lambda x: (-x[1], x[2], -x[3], x[0]))

# 출력
for i in range(N):
    print(students[i][0])


# # List Comprehension 로 바꾼 버전
# # 약간 더 빠르고 메모리는 약간 더 먹음. 큰 차이는 X
# N = int(input())

# students = [[x[0]] + list(map(int, x[1:])) for x in [input().split() for i in range(N)]]
# students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

# for i in range(N):
#     print(students[i][0])