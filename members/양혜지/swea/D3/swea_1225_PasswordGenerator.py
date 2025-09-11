# 암호 생성기

from collections import deque

T = 10
for tc in range(1, T + 1):
    input()
    q = deque(list(map(int, input().split())))
    i = 1
    
    
    # 언제까지 가져다 붙일 지 ... 몰름 ?
    # 0이거나 0보다 작으면 break 하고 0 append
    while True:
        x = q.popleft()
        if x-i <= 0:
            q.append(0)
            break
        
        else:
            q.append(x-i)
            
        i +=1
        if i > 5:
            # 재할당
            i = 1 
            
    print(f'#{tc}', end=' ')
    print(*q)
        
    
    

# 왼쪽에 있는 애 i라고 치고 걔한테 1을 뺴서 맨 뒤에 붙여
# 맨 왼쪽에 있는 애는 pop
# 다음은 2 빼서 붙이고 .....
# 언제 멈춤 ? 5까지 빼면 한 세트 돈걸로 하고 멈춤

# i는 1부터 5까지 
# 첫번쨰 값 ???
# 첫번째 값에서 i를 빼
# 뺀 값이 0이거나 0보다 작으면 q.append(0)
# 0 append를 언제해 ?????????????


#1 6 2 2 9 4 1 3 0 
#2 9 7 9 5 4 3 8 0 
#3 8 7 1 6 4 3 5 0 
#4 7 5 8 4 8 1 3 0 
#5 3 8 7 4 4 7 4 0 
#6 6 7 5 9 6 8 5 0 
#7 7 6 8 3 2 5 6 0 
#8 9 2 1 7 3 6 3 0 
#9 4 7 8 1 2 8 4 0 
#10 6 8 9 5 8 5 2 0 
