arr = list(map(int, input().split()))
M = int(input())

for i in range(len(arr) - M + 1):
    sub = arr[i : i+M]
    # 순 증가 수열인지 확인
    switch = True
    for j in range(M-1):
        if sub[j] >= sub[j+1]:
            switch = False
    
    if switch == False:
        print("no")
    else:
        print("yes")