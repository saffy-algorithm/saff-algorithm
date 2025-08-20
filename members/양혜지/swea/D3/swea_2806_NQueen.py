# 행에서 queen 조건에 맞으면 다음 행으로
# row + col
# row - col
# 만약에 퀀을 n 개 다 놨어 . . . 그러면 count 하나
# 




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    for i in range(N):
        for j in range(N):
            if i == N-1:
                count +=1 