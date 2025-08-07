T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    max_idx = 0 # 첫 시작을 최대로 가정
    min_idx = 0
    
    for i in range(1, N):
        if arr[max_idx] <= arr[i]:
            max_idx = i
        if arr[min_idx] > arr[i]:
            min_idx = i

    print(f'#{t} {abs(max_idx - min_idx)}')