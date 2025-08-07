# N = 3 # 가지고 있는 데이터의 수
# numbers = [1, 2, 3] # 모든 경우의 수 체크
# visited = [0]*N # 비선형적 -> 재귀

# def subset(count):
#     if count == N: # 고를지 말지 의사결정만 
#         # visited 결정
#         print(visited)
#         return
    
#     # 초기값이 0이기 때문에 O, X 중에 O만 가면됨
#     # visited 조작하지 않고 그대로 보낸다는 뜼
#     # 보내는 것만 생각하는 중 (되돌아오는 건 재낀 상태)
#     subset(count+1)
#     visited[count] = 1
#     subset(count+1)
#     # 번복, 되돌아오는 중
#     visited[count] = 0
    
# subset(0) # 프린트 위에서 찍고 서브셋 호출하러 옴



N = 3 # 가지고 있는 데이터의 수
numbers = [1, 2, 3] # 모든 경우의 수 체크
visited = [0]*N # 비선형적 -> 재귀

def subset(count):
    if count == N: # 고를지 말지 의사결정만 
        # visited 결정
        for i in range(N):
            if visited[i]:
                print(numbers[i], end = " ")
        return
    
    # 초기값이 0이기 때문에 O, X 중에 O만 가면됨
    # visited 조작하지 않고 그대로 보낸다는 뜼
    # 보내는 것만 생각하는 중 (되돌아오는 건 재낀 상태)
    subset(count+1)
    visited[count] = 1
    subset(count+1)
    # 번복, 되돌아오는 중
    visited[count] = 0
    
subset(0) # 프린트 위에서 찍고 서브셋 호출하러 옴