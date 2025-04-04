import sys

string = list(sys.stdin.readline().rstrip())
쾅 = list(sys.stdin.readline().rstrip())    # 리스트로 저장

temp = []
for i in range(len(string)):

    temp.append(string[i])

    if temp[-len(쾅):] == 쾅:
        # len(쾅)만큼 제거
        for j in range(len(쾅)):
            temp.pop()

result = ''.join(temp) if temp else 'FRULA'
print(result)
