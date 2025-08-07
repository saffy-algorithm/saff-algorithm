T = int(input())

for tc in range(1, T+1):
    A = int(input())
    raw = list(map(int, input().split()))
    drop_nums = []

    if len(raw) == 1:
        answer = 0
    else:
        for i in range(len(raw)-1):
            drop_num = 0
            for j in range(i+1, len(raw)):
                if raw[i] > raw[j]:
                    drop_num += 1
            drop_nums.append(drop_num)
        answer = max(drop_nums)
    print(f"#{tc} {answer}")
