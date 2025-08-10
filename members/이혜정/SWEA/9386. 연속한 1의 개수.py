# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AXALDUIq97oDFASI

# ver1. 더 많은 분기, 비효율적
T = int(input())

for t in range(T):
    N = int(input())
    sequence = list(map(int, input()))
    max_cnt = -1
    cnt = 0

    for i in range(N - 1):  # i번째 값과 i+1번째 값에 접근할 것이기 때문에, N-1까지만 순회
        if sequence[i] == 1:    # 현재값이 1이면 cnt 하나 증가
            cnt += 1
            if sequence[i + 1] == 0:    # 다음 값이 0이면 최대값과 비교하고, cnt 초기화
                if max_cnt < cnt:
                    max_cnt = cnt
                cnt = 0
            # 여기까지만 하면, 마지막 원소가 1일 때 처리가 안 됨

            # 마지막 값이 1일 때 cnt 하나 증가하고, 최대값과 비교
            elif sequence[i + 1] == 1 and i + 1 == N - 1:
                cnt += 1
                if max_cnt < cnt:
                    max_cnt = cnt

    print(f'#{t + 1} {max_cnt}')


# ver 2. 현재값만 따져서 간단하게 풀이
T = int(input())

for t in range(T):
    N = int(input())
    sequence = list(map(int, input()))
    max_cnt = -1    # 연속한 1 개수의 최대값 저장할 변수
    cnt = 0         # 연속한 1 개수 저장할 변수

    for i in range(N):
        if sequence[i] == 0:    # 0이면 cnt 초기화
            cnt = 0
        elif sequence[i] == 1:  # 1이면 cnt 하나 증가
            cnt += 1
            if max_cnt < cnt:   # 최대값과 계속 비교하고, 최대값 초과 시 교체
                max_cnt = cnt

    print(f'#{t+1} {max_cnt}')