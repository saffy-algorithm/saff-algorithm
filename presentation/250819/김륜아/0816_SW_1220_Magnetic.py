#   Magnetic (N극 S극 교착 상태 개수 구하기)

T = 10

for tc in range(1, T+1):
    square_len = int(input())
    table = [list(map(int, input().split())) for _ in range(100)]
    table_vertical = list(zip(*table))

    magnetic = 0

    for line in table_vertical:

        # 위가 N극, 아래가 S극 -> vertical -> 왼쪽이 N극, 오른쪽이 S극
        count_1 = 0
        
        for num in line:
            
            # 1 -> N극 성질 갖는 자성체
            if num == 1:
                count_1 += 1
            
            # 2 -> S극 성질 갖는 자성체
            elif num == 2 and count_1 >= 1:
                magnetic += 1
                count_1 = 0

                    
    print(f"#{tc} {magnetic}")


