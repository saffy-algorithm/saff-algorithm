T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    swap = 0
    for i in range(N):
        if A[i] != B[i]:
            swap+=1
            for j in range(1, N):
                A[i] = 1-A[i]
                
