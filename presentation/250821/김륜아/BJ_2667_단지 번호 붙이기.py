# 단지 번호 붙이기

from collections import deque

# 각 번지수에 해당하는 집 개수 세는 함수            
def BFS(i, j):
    global block_nums

    q = deque()
    q.append((i, j))

    # 첫 번째 집 카운트
    cnt = 1

    while q:
        i, j = q.popleft()
        for delta in range(4):
            ni = i + di[delta]
            nj = j + dj[delta]
            if 0 <= ni < N and 0 <= nj < N:
                # 각 단지의 집을 찾고 방문 체크
                if raw[ni][nj] == 1 and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    cnt += 1
                    q.append((ni, nj))
    return cnt


N = int(input())
raw = [list(map(int, input())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

block_nums = 0
house_nums = []

visited = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        # 처음 찾은 i,j로 함수를 돌릴 것이다.
        # 함수가 돌아가면서 같은 단지 내 위치는 1로 바뀔 것이다
        # 그래서 각 단지를 count 할 수 있음.
        if raw[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            block_nums += 1
            house_nums.append(BFS(i, j))
    
house_nums.sort()
print(block_nums)
for i in range(len(house_nums)):
    print(house_nums[i])
