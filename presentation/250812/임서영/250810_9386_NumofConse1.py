T = int(input())

for tc in range(T):
    N = int(input())
    num_lst = list(map(int, input()))

    cnt_list = []
    count = 0

    for num in num_lst:
        if num == 1:
            count += 1
        else:
            cnt_list.append(count)
            count = 0

        cnt_list.append(count)
    
    print(f'#{tc+1} {max(cnt_list)}')

