# 연속된 1의 개수

T = int(input()) # T : 3
for tc in range(1, T+1): # tc : 1
    N = int(input()) # N : 10
    arr = list(map(int, input())) # 0011001110
    
    max_v = cnt = 0
    for i in range(N):
        if arr[i] == 1:
            cnt += 1

            if max_v < cnt:
                max_v = cnt
                
        else :
            cnt = 0
    
    print(f'#{tc} {max_v}')
