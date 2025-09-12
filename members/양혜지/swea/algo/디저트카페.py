# 디저트 카페 투어
# 대각선 방향으로 움직이고
# 사각형 모양을 그리며 출발한 카페로 돌아와야함
# 투어 도중 해당 지역을 벗어나면 안됨
# 카페 투어 중에 같은 숫자의 디저트를 팔고 있는 카페가 있으면 안됨
# 하나의 카페에서 디저트 섭취 안됨 -> 무조건 이동
# 왔던 길 되돌아가기 안됨

# 디저트를 가장 많이 먹을 수 있는 경로 찾고
# 디저트 수를 정답으로 출력
# 디저트 못 먹으면 -1 출력

# 중복되지 않는 거, 포함되는 거, 
# 가능한 모든 경우 중(전체 순회)에서 가장 큰 값

# 시작점 sr sc -> 마름모로 순회
# visited에 저장하고(중복체크) 어펜드 그 길이가 -> 출력값
# 직진 -> 꺾기 3번 -> 종료 조건이 3이되면 ??
# 마름모는 최대 3번 방향 변경 가능하고 다시 내자리로 돌아와
# 정지 왜 필요한가 ?

dr = [1, 1, -1, -1]
dc = [-1, 1, 1, -1]

def dfs(idx, r, c, sub, start_r, start_c):
    global answer
    # 만약 idx > 3(이미 4번 이상 턴) 이면 더 진행하지 않음
    if idx > 3:
        return

    for d in range(idx, idx + 2):
        nr = r + dr[d % 4]
        nc = c + dc[d % 4]

        # 시작점으로 돌아오는 경우: (원래는 arr[start_r][start_c]가 sub에 있으므로
        # 일반 중복검사로는 못 들어감) — 이 경우 길이가 4 이상이면 유효 루프
        if 0 <= nr < N and 0 <= nc < N and nr == start_r and nc == start_c and idx == 3:
            # sub에는 시작 디저트를 포함한 현재까지의 방문 목록이므로,
            # 시작으로 돌아온 순간의 전체 방문 수는 len(sub)
            if len(sub) >= 4:  # 문제에서 요구하는 최소 루프 길이 조건(예시) — 필요시 조정
                answer = max(answer, len(sub))
            continue

        # 범위 내이고, 그 디저트 번호를 아직 먹지 않았다면 진행
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] not in sub:
            sub.append(arr[nr][nc])
            dfs(d, nr, nc, sub, start_r, start_c)
            sub.pop()

# 메인에서 호출 예시:
# 시작할 때 sub를 시작 디저트로 초기화
for i in range(N - 2):
    for j in range(1, N - 1):
        dfs(0, i, j, [arr[i][j]], i, j)

    



