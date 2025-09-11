# A형_Tree

T = int(input())

for tc in range(1, T+1):
    # 나무의 수
    N = int(input())
    # 나무의 높이
    raw = list(map(int, input().split()))

    # 날짜 수 세기
    target = max(raw)

    # 날짜 카운트 리스트
    zero = [0]
    one_two = [1,2]*(N*target)
    sum_days = zero + one_two


    
    for i in range(N):
        tall = raw[i]
        day = 1

        while tall < target:
            # 홀
            if day % 2 == 1 and tall + 1 <= target:
                while sum_days[day] < 1:
                    check = day + 2
                    if sum_days[check] == 1:
                        sum_days[check] = 0
        
                sum_days[day] = 0       
                tall += 1
                day += 1

            # 짝
            elif day % 2 == 0 and tall + 2 <= target:
                while sum_days[day] < 1:
                    check = day + 2
                    if sum_days[check] == 2:
                        sum_days[check] = 0
                sum_days[day] = 0   
                tall += 2
                day += 1

            else:
                day += 1

    answer = 0
    for i in range(1, len(sum_days)+1):
        if i != 0:
            answer = i
            break

    print(f"#{tc} {answer}")