def value_of_crops(farm_lst, N):
    crop_value = 0
    for r in range(N):
        col_idx = abs((N//2) - r)
        col_count = N - (abs((N//2) - r)*2)

        for c in range(col_idx, col_idx+col_count):
            crop_value += farm_lst[r][c]
    return crop_value



t = int(input())

for num in range(t):
    N = int(input())
    farm_lst = []
    for _ in range(N):  
        farm = list(map(int, input()))
        farm_lst.append(farm)

    result = value_of_crops(farm_lst, N)
    print(f'#{t} {result}')

