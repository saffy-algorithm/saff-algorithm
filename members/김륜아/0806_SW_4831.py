# 전기차

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    Battery = list(map(int, input().split()))

    position = 0 # 현재 위치

    count = 0 # 충전소 들른 횟수

    while position + K < N:

        for step in range(K, 0, -1):
            if position + step in Battery:
                position += step
                count += 1
                break
        else:
            count = 0
            break

    print(f"#{tc} {count}")
        


    