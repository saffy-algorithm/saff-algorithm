T = int(input())

for tc in range(1, T+1):
    date = input()

    month = date[4:6]
    day = date[6:]

    if 0 < int(month)<  13:
        if int(month) in [1, 3, 5, 7, 8, 10, 12]:
            if 0< int(day) <= 31:
                print(f'#{tc} {date[:4]}/{month}/{day}')
        elif int(month) in [4, 6, 9, 11]:
            if 0< int(day) <= 30:
                print(f'#{tc} {date[:4]}/{month}/{day}')
        elif int(month) == 2:
            if 0 < int(day) <= 28:
                print(f'#{tc} {date[:4]}/{month}/{day}')
            else:
                print(f'#{tc} -1')
    else:
        print(f'#{tc} -1')