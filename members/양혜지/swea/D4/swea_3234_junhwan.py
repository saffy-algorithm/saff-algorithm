# 준환이의 양팔저울

import math # 팩토리얼 가져다 쓰려고
def dfs(count, left, right): # 왼쪽에 얼마나 놨는지, 오른쪽에 얼마나 놨는지 알아야하니까
    global answer # 전역변수를 불러오는 꼴 (왜지)
    
    # 왼쪽 무게가 전체 무게의 절반이면 왼쪽, 오른쪽 어디 놔도 상관이 없음
    # 바로 2^(N)*(N!) 공식 때려버리기
    if left >= total_weight / 2: # 절반 이상이라면
        answer += 2**(N - count) * math.factorial(N - count) # 이렇게 하면 다음번으로 갈 필욧 없음
        return
    
    # 재귀니까 탈출조건 생각해야죠
    if count == N:
        answer += 1
        return

    # 무게 추를 하나 골라서 놓아줄거임
    for i in range(N):
        if visited[i]:
            continue
            
        visited[i] = 1
        # dfs 호출 2번 해야됨
        dfs(count + 1, left+weight[i], right)
        # 오른쪽에 놨더니 왼쪽 보다 이하야
        if right + weight[i] <= left:
            dfs(count + 1, left, right + weight[i])
        visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    answer = 0 # 경우의 수 발생 시 엔서에 누적
    
    N = int(input())
    weight = list(map(int, input().split()))
    total_weight = sum(weight) # 가지치기1 : 지금까지 놓인 토탈웨이트 중에 절반 이상이
    visited = [0]*N
    
    answer = 0
    
    # 무게 추를 하나 골라서 놓는 작업
    # 어떤 상태들을 넘겨주는 게 좋을까 ? 생각
    # 재귀로 짜면 탈출조건 필요 << 이 생각부터 해야됨 
    # 
    dfs(0, 0, 0)
    print(f"#{tc} {answer}")