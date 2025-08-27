# 스위치 조작

# ai랑 bi 인덱스의 값이 다르면 ai의 해당 인덱스부터 끝까지 숫자를 바꿔
# 숫자를 바꾸는 방법 ? 0이면 1로 바꾸고 1이면 0으로 바꿔라
# 바꿀 때마다 cnt 누적
# ai랑 bi랑 같으면 종료

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Ai = list(map(int,input().split()))
    Bi = list(map(int,input().split()))
    
    cnt = 0
    
    for i in range(N):
        if Ai[i] != Bi[i]:
            cnt +=1
            for j in range(i, N):
                Ai[j] = 1-Ai[j]
                     
    print(f'#{tc} {cnt}')
            
            