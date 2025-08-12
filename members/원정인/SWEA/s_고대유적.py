T = int(input())
for tc in range(T):
    N,M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    # 연속된 1의 갯수 세기, 
    cnt = 0
    cnt_lst =[]
    for n in range(N):
        for m in range(M):
            if arr[n][m] == 1:
                cnt += 1
                cnt_lst.append(cnt)