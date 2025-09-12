T = int(input())
 
for tc in range(T):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    position = 0 #현재 위치
    answer = 0 #충전 횟수
 
    while position + K < N:
        for i in range(position+K, position, -1):
            if i in charge:
                position = i
                answer += 1
                break
        else:
            answer = 0
            break
         
    print(f'#{tc+1} {answer}')