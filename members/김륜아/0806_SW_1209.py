# 문제해결 기본 - Sum

for tc in range(1, 11):
    T = int(input())
    raw = [list(map(int, input().split())) for _ in range(100)]

    # 행 최댓값
    max_row_sum = 0
    max_column_sum = 0
    for i in range(100):
        row_sum_cac = 0
        column_sum_cac = 0
        for j in range(100):
            row_sum_cac += raw[i][j]
            column_sum_cac += raw[j][i]
        
        if row_sum_cac > max_row_sum:
            max_row_sum = row_sum_cac
    
        if column_sum_cac > max_column_sum:
            max_column_sum = column_sum_cac
    
    # 대각선_1, 2 합
    diagonal_1_sum = 0
    diagonal_2_sum = 0
    for i in range(100):
        diagonal_1_sum += raw[i][i]
        diagonal_2_sum += raw[i][99-i]

    max_answer = max(max_row_sum, max_column_sum, diagonal_1_sum, diagonal_2_sum)

    print(f"#{tc} {max_answer}")