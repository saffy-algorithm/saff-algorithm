T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())
    raw = list(map(int, input().split()))
    cac = []
    for i in range (a - b +1):
        sum_nums = sum(raw[i : i+b])
        cac.append(sum_nums)
    max_num = max(cac)
    min_num = min(cac)
    answer = max_num - min_num
    print(f"#{tc} {answer}")
