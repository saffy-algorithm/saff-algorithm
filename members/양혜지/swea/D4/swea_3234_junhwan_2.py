# 준환이의 양팔저울
# 메모이제이션
# 비트 연산자

def dfs(count, diff):
    global visited
    
    if dp[visited].get(diff):
        return dp[visited][diff]
    
    # 탈출 조건
    if count == N:
        # 리턴 해주기 전에 기록하기
        dp[visited][diff] = 1
        return dp[visited][diff]

    # 누적
    case_count = 0
    # N개 중에 골라줄거임
    for i in range(N):
        if visited & (1 << i): # 1을 i만큼 밀어라 / 방문되었었다
            continue
        
        # OR / 방문 체크
        visited |= (1 << i)
        case_count += dfs(count + 1, diff + weight[i])
        if diff - weight[i] >= 0:
            case_count += dfs(count + 1, diff - weight[i])
        visited ^= (1 << i)
 
    dp[visited][diff] = case_count
    return case_count
        
        
T = int(input())
for tc in range(1, T+1):
    
    N = int(input())
    weight = list(map(int, input().split()))
    total_weight = sum(weight)
    
    answer = 0 # 경우의 수 발생 시 엔서에 누적
    
    dp = [{} for _ in range(2**9)] # 딕셔너리
    visited = 0
    
    answer = dfs(0, 0) # 엔서에 dfs의 결과를 줄거임 / 인자를 두개줄거임
    
    print(f"#{tc} {answer}")