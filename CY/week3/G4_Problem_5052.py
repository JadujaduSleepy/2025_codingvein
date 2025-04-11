import sys
input = sys.stdin.readline

t = int(input()) # test 케이스 수 
count = 0

def check(phone, num):
    see = False
    # 처음에 이중 포문으로 돌리고 시간이 초과되었다
    # 어차피 정렬을 해둔 상태(string)라서 접두어 여부를 검토할 때는 인접한 것들만 확인하면 된다 
    # i와 그 다음 애들부터 검토 
    for i in range(num-1):
        see = phone[i+1].startswith(phone[i])
        if see == True:
            return False
            break
        else:
            continue
    return True

while count < t:
    count += 1 # 한 번씩 하는 거니까 
    num = int(input()) # 전화번호 수 입력 
    phone= []
    for _ in range(num):
        # phone.append(input()) - 자꾸 strip()을 빼먹어서 틀린다 
        phone.append(input().strip()) 
    
    phone.sort() # string 정렬 
    
    if check(phone, num)==True:
        print("YES")
    else:
        print("NO")