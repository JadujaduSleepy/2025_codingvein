import sys 
input = sys.stdin.readline

# 문자열 입력 받기 (공백으로 나누지 않음!) 
ready = input().rstrip()
bomb = input().rstrip()

stack = []
bomb_length = len(bomb)

# 폭발열 문자가 있으면 True, 없으면 False
def boom(stack, bomb):
    # 스택의 길이가 폭발열 문자보다 짧으면 그냥 false
    if len(stack)< len(bomb):
        return False
    alphabet = stack[-bomb_length:] 
    check = '' # 문자열 합치기 위해 또 선언... 
    for x in alphabet:
        check += x 
    
    return check==bomb
    
# 스택에 매번 검사를 돌려서 시간 초과 에러가 발생했었음 
# 그래서 폭발열의 마지막 글자 들어왔을 때만 봐준다 
for x in ready: 
    stack.append(x)
    # stack에 넣은게 폭발열만큼의 길이 이상 들어있고, bomb 마지막 글자가 들어왔다면  
    if len(stack)>=bomb_length and x==bomb[-1]:
        if boom(stack, bomb):
            for x in range(bomb_length):
                stack.pop() # 폭발

if len(stack)>0:
    print(''.join(stack))
else:
    print("FRULA")