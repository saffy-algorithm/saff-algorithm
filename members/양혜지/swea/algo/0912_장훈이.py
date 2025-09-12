# 항상 생각해야할 것
# 1. 종료 조건은 무엇인가 : N명의 모든 점원을 고려했을 때
#    - 가지치기 : 이미 높이가 B 이상이면 더 이상 쌓을 필요 없다
# 2. 가지의 수 :
#    - 점원을 탑에 포함 시키는 경우 or 안 시키는 경우

# 재귀호출 문제 풀이시
# 1. 전체조건을 생각한 후에 2. 가지치기를 하센

def recur(idx, total_height): # idx는 cnt # 파라미터에 높이도 같이 전달 ㄱ
    global min_answer
    if total_height >= B: # 가지치기 : B이상이면 더 이상 쌓지 마라
        # 지금 현재 탑 높이랑, 내가 최소값으로 가지고 있던거랑 비교
        min_answer = min(min_answer, total_height) 
        return

    if idx == N: # N명을 모두 고려함
        return
    
    # 두번 호출
    recur(idx + 1, total_height + heights[idx]) # 탑에 포함 시키는 경우
    recur(idx + 1, total_height) # 탐에 포한 안 시키는 경우

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    min_answer = 1e8 # 나올 수 있는 최대 범위 (정답이 나오는 게 보장됐을때만 사용)
    min_answer = 200000 # 나올 수 없다면 최대 값으로 # 정석은 10000 * N
    recur(0, 0)
    print(f'#{tc} {min_answer - B}')