# 연속한 1의 개수

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    raw = list(map(int, input().strip()))
    
    count_one = 0
    count_list = []
    for i in range(N):
        if raw[i] == 1:
            count_one += 1
            count_list.append(count_one)
        else:
            count_one = 0
    print(f"#{tc} {max(count_list)}")