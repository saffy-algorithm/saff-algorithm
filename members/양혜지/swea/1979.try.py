T = int(input())  # 테스트 케이스 수 입력

for tc in range(1, T+1):
    N, K = map(int, input().split())  # 퍼즐의 크기 N과 단어 길이 K 입력
    cube = [list(map(int, input().split())) for _ in range(N)]  # 퍼즐판 정보 입력

    count = 0  # 정답: 단어가 들어갈 수 있는 자리 수

    # 가로 방향 탐색
    for arr in cube:  # 퍼즐의 각 행을 하나씩 검사
        tmp = 0  # 연속된 1의 개수를 저장할 변수
        for idx in range(N):
            if arr[idx] == 1:
                tmp += 1  # 1이면 연속된 길이 증가
            else:
                tmp = 0  # 0이 나오면 끊기므로 초기화

            if tmp == K:
                try:
                    # K개의 연속된 1 뒤에 0이 나와야 정확히 K칸 자리로 인정
                    if arr[idx + 1] == 0:
                        count += 1
                except IndexError:
                    # 인덱스를 벗어나면 마지막 칸이므로 유효한 자리로 인정
                    count += 1
                    tmp = 0  # 중복 카운트를 방지하기 위해 초기화

        # 줄 끝에서 정확히 K개로 끝나는 경우도 카운트
        if tmp == K:
            count += 1

    # 세로 방향 탐색
    for r in range(N):  # 각 열을 하나씩 검사
        tmp = 0
        for c in range(N):
            if cube[c][r] == 1:
                tmp += 1  # 1이면 연속된 길이 증가
            else:
                tmp = 0  # 0이 나오면 끊기므로 초기화

            if tmp == K:
                try:
                    # 다음 칸이 0이면 정확히 K칸 자리로 인정
                    if cube[c + 1][r] == 0:
                        count += 1
                except IndexError:
                    # 마지막 칸이면 유효한 자리로 인정
                    count += 1
                    tmp = 0  # 중복 방지

        # 열 끝에서 정확히 K개로 끝나는 경우도 카운트
        if tmp == K:
            count += 1

    # 결과 출력
    print(f"#{tc} {count}")
