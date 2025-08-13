# 길찾기 DFS

def dfs(v): # v는 시작위치
    global switch
    if v == 99:
        switch = True
    
        
    


for _ in range(10):
    tc, gil = map(int,input().split())
    arr = list(map(int,input().split()))
    switch = False

    graph = [[] for _ in range()]
    for i in graph(0, len(arr), 2):
        a, b = arr[i], arr[i+1] # 어디
        graph[a].append(b) # 어떻게
        
        
        
        
        
        
        
        
    # 지금 노드랑 연결된 노드를 재귀로 호출
    # 도착하면 끝나
    # 도착을 찾으면 True로 반환
    # 0에서 시작하고 도착점은 99
    # 99를 찾으면 True ??
    # 더 이상 갈 수 없어 -> 0 반환 
    
