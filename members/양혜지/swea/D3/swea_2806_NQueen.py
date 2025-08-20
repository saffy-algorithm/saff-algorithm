# 조합이랑 비슷하다고 보면 됨
# 가로검사 할 필요 없음
# 대각선의 합이 같거나 -> 좌하향
# 대각선의 차가 같거나 -> 우하향
# ㄴ 너도 그러면 visited를 사용할 수 있겠네 라고 생각하시긔


# 행에서 queen 조건에 맞으면 다음 행으로
# row + col
# row - col
# 만약에 퀀을 n 개 다 놨어 . . . 그러면 count 하나
# 


T = int(input())

def n_queen(row):
    # answer는 전역 변수니까 글로벌 처리
    global answer
        
    # 재귀로 짤거니까 탈출조건이 필요
    if row == N :
        answer += 1
        return
    
    for col in range(N):
        # 세로 검사 통과 & 좌하향 통과 & 우하향 통과
        if not col_visited[col] and not main_diag_visited[row-col + N-2]:
            col_visited[col] = 1 # 방문처리
            main_diag_visited[row-col +N-1]
            sub_diag_visited[row]
            
            
    
    
        
for tc in range(1, T+1):
    N = int(input())
    
    
    # 테케마다 필요한 visited 세팅
    
    col_visited = [0]*N
    # 좌하향 대각선 / 우하향 대각선
    main_diag_visited = [0]*(2*N-1)
    sub_diag_visited = [0]*(2*N-1)
    answer = 0
    
    n_queen = 0
    # 지금 내가 놓고 있는 번호의 수랑 행이랑 일치

    print(f'#{tc}')
    
    
# 조합이랑 똑같음!
# 골랐던 걸 빼고 또 고르고 ... 반복
# 하나를 고를 건데 다음 재귀에서 고른 녀석이 가로/세로/대각선으로 충돌 x

# 2차원 좌표상에서 뽑아내는거
# 행, 열 돌아야지 라고 보통 생각하는데 그럴 필요가 없고
# 한 번 고를 때, 첫번째 행에서 골랐다면 두번째는 바로 두번째 행으로 내려가묜 돼
# 각 행에서 하나씩 고르는 게 자명함!!
# for 행 이런 걸 돌아줄 필요가 없다 , 번째에 들어왔을 때 열만 골라주면 된다.
# 조합에서 전달했던 인자, 내가 지금까지 몇개를 골라냈는 지를 전달했었음!
# cnt가 지금 몇번째 퀸을 놓고 있는 지가 됨
# 몇번째 퀸을 놓는 지가 행의 번호와 같음, 해당 행 번호에서 열만 뽑아주면 돼
# 가로검사가 필요가없다!

# 열도 각 열에 대해서 한 번 씩만 나와야 돼!
# 열만 생각했을 때, visited 를 1차원으로 생각
# 지금 위치 기준 "위"로 좌하향 우하향 대각선을 검사하면 됨
# 이유 왜냐면! 위에서 내려올거니까 아래쪽에 검사할게 없자낭

# 행열의 특징!
# 대각선의 합이 같거나 대각선의 차가 같거나 흠?
# 좌하향하는 대각선은 행과열의 합이 똑같음
# 우하향하는 대각선은 행과열의 차가 똑같음
# visited를 사용할 수 있겠다는 느낌이 와야된대 모.모르겟어

# 좌하향일때
# visited[행과열의합] = 1 이면 이 대각선은 방문했었네.,, 하면 된대 흠?

# visited 통합하지말래 왜냐묜 합 / 차 그 값의 위치가 전혀 달라서 따로하란다
# 그래서 총 3개 열, 좌대각, 우대각 ㅎㅎ

def n_queen(row): # 지금 몇번째 뽑고 있는 지가 지금 행번호랑 똑같으니깐~
    global answer
    if row == N: # 다 골랐을 때 탈출
        answer += 1
        return

    for col in range(N): # 열을 하나 골라
        # 세로 검사 통과 & 좌하향 통과 & 우하향 통과
        # 쟤들이 다 미방문 상태일 때만 통과로 인정
        # 방문 안됐을 때!:
        if not col_visited[col] and not main_diag_visited[row-col+N-1] and not sub_diag_visited[row+col]:
            col_visited[col] = 1
            main_diag_visited[row-col+N-1] = 1
            sub_diag_visited[row+col] = 1

            n_queen(row+1)

            col_visited[col] = 0
            main_diag_visited[row-col+N-1] = 0
            sub_diag_visited[row+col] = 0


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    
    col_visited = [0] * N
    main_diag_visited = [0] * (2*N-2) # 우하향
    sub_diag_visited = [0] * (2*N-2) # 좌하향
    answer = 0

    n_queen(0)

    print(f"#{tc} {answer}")