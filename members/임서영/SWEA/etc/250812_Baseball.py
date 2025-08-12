T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    stats = list(map(int, input().split()))

    answer = 1 # 한 명이 팀일수도

    stats.sort()

    for i in range(N-1):
        temp = 1
        for j in range(i+1, N):
            if stats[j] - stats[i] > K:
                break
            temp += 1
        answer = max(answer, temp)

    print(f'#{tc} {answer}')    



###투포인터 기법으로 풀기
T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    stats = list(map(int, input().split()))

    answer = 1 # 한 명이 팀일수도

    stats.sort()

    left = 0
    right = 0

    while right < N:
        if stats[right] - stats[left] <= K:
            right += 1
            answer = max(answer , right-left)
            continue
        left += 1
    print(answer)

