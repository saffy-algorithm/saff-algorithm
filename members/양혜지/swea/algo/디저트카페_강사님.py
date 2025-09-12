# 재귀없이
# 단순 반복문

# 특징
# 1. 맨 위를 꼭짓점으로 잡는 이유 .. 뭐라고 하셨지 ?
# 2. 꼭짓점부터 우하로 2칸, 좌하로 3칸 가기로 했다 라고 정해지면 나머지는 길이가 동일함
#    -> 직사각형이니까
# 3. 이 모양(직사각형)이 다 있다는 걸 검증하는 방법 : 

# 방향 세팅 미리
# 시계방향 델타 세팅
# 우하, 좌하, 좌상, 우상
dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]


# 돌면서 방문 체크
def desserts_run(r, c, turn1, turn2):
    desserts_set = set()

    # 0번 방향 수,  1번 방향 수, 2번 방향 수, 3번 방향 수
    counts = [turn1, turn2, turn1, turn2]

    for dir in range(4):
        for i in range(counts[dir]):
            r += dr[dir]
            c += dc[dir]
 
            if desserts[r][c] in desserts_set:
                return -1
            desserts_set.add(desserts[r][c])
    return len(desserts_set)


T = int(input())
for tc in range(1, T+1):
    N = int(input())        # N : 지역의 한 변의 길이
    desserts = [list(map(int,input().split())) for _ in range(N)]  # 디저트 종류 2차원 리스트
    answer = -1     # 디저트 먹은 수

    # 1. 시작점 정해주기
    # 행에 대해서는 아래 하나씩 두개 소거
    # 열에 대해서는 좌우 하나씩 두개 소거
    for s_r in range(N-2):
        for s_c in range(1, N-1): # 유효한 시작점 정함
             
            # 2. 얼마만큼 내려갈 수 있을까? turn1(우하), turn2(좌하)
            for turn1 in range(1, N-s_c):
                for turn2 in range(1, N - (s_r + turn1)):
                    if s_c - turn2 >= 0 and (turn1 + turn2) * 2 > answer:
                        answer = max(answer, desserts_run (s_r, s_c, turn1, turn2))
    print(f"#{tc} {answer}")

