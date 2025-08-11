T = int(input())

for tc in range(T):
    str1 = list(input())
    str2 = list(input())

    max_count = 0
    str_count = 0

    for i in str1:
        for j in str2:
            if i == j:
                str_count += 1
            if str_count > max_count:
                max_count = str_count
        str_count = 0
    
    print(f'#{tc+1} {max_count}')
