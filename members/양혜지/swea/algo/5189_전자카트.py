# 시작이랑 끝은 무조건 1
# 입력 값 0
# 사무실은 0, 구역은 N-1
# 어떤 순서로 구역을 방문할지 -> 순열
# 종료조건 : 모든 관리구역(사무실 제외)의 방문 순서가 결정된 상태 
# -> 순열 다 만들어졌을 떄
    
def perm(cnt):
    global answer

    # 순열 생성
    if cnt == len(a):
        office = 0
        # 순열을 돌아
        for i in range(len(picked) -1):
            office += arr[picked[i]][picked[i+1]]

        # 마지막에서 첫번째로 다시 돌아오는 구간
        office += arr[picked[-1]][0]
        # 첫번째에서 다음으로 
        office += arr[0][picked[0]]

        answer = min(answer, office)
        return

    for i in range(len(a)):
        if not visited[i]:
            picked.append(a[i])
            visited[i] = 1
            perm(cnt + 1)
            picked.pop()
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    answer = 1e9

    # 관리구역 번호
    a = []
    for i in range(1, N):
        a.append(i)
    
    picked = [] # 현재까지 뽑은 방문 순서 기록 -> 순열을 넣어놓을 것
    visited = [0] * len(arr) # 어떤 구역을 이미 썼는지 체크

    # 실행 / 출력
    perm(0)
    print(f'#{tc} {answer}')