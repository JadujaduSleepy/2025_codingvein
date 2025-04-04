# 2025-04-01
# https://www.acmicpc.net/problem/9935
# 메모리 43596KB 시간 972ms

import sys

# 백준 제출시 삭제
sys.stdin = open('input.txt', 'r')

total = input()
target = input()

stack = []

for i in range(len(total)) :
    stack.append(total[i]) # 스택에 문자 추가
    check = "".join(stack[-len(target):]) # 최근 target 길이의 스택 문자

    #스택보다 폭발 문자열이 더 길면 체크하는 의미가 없어서 넣어본 코드...
    if (len(stack) < len(target)) : 
        continue
    
    # 폭발하나요?
    if (check == target): 
        for i in range(len(target)) : # 네
            stack.pop()

if (len(stack)==0) :
    print("FRULA")
else :
    print("".join(stack))

    

    

    
