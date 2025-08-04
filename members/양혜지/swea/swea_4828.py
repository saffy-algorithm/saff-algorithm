T = int(input())

for i in range(1, T+1):
    N = int(input())
    l = list(map(int,input().split()))

    min1 = 999999
    max2 = -999999

    for j in l:
        if j > max2:
            max2 = j
        if j < min1:
            min1 = j
    
    print(f'#{i} {max2 - min1}')