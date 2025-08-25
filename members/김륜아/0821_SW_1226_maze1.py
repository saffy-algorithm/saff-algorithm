# 미로1

T = 10

def BFS(i, j, N):
    # 출발 지점을 1로 채워주고 시작(방문 체크)
    visited[i][j] = 1

    # 네 방향 중 갈 수 있는 위치들 저장
    q = [[i, j]]

    # q가 사라질 때까지 반복
    while q:
        # q 제일 처음 값부터 체크
        i, j = q.pop(0)

        # raw[i][j] == 3이면 도착지 찾았으니 1로 return
        if raw[i][j] == 3:
            return 1

        # 네방향 탐색
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            move_i, move_j = i + di, j + dj

            # N*N 범위
            if 0 <= move_i < N and 0 <= move_j < N:

                # 벽도 아니고 방문하지 않은 곳들만 찾기
                if raw[move_i][move_j] != 1 and visited[move_i][move_j] != 1:
                    # 방문체크
                    visited[move_i][move_j] = 1
                    # 갈 수 있는 위치 q에 append
                    q.append([move_i, move_j])

for tc in range(1, T+1):
    t = int(input())
    N = 16
    raw = [list(map(int, input())) for _ in range(N)]

    # 출발점 찾기
    find = False
    for i in range(N):
        for j in range(N):
            if raw[i][j] == 2:
                s_i, s_j = i, j
                find = True
                break
        if find:
            break   
    
    # visited
    visited = [[0] * 16 for _ in range(16)]

    answer = BFS(s_i, s_j, N)
    if not answer:
        answer = 0

    print(f"#{tc} {answer}")