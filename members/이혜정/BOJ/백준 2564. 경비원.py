# https://www.acmicpc.net/problem/2564 (Silver I)

w,h = list(map(int, input().split()))

def cal_dist(direction, dist):
    if direction == 1:      #북
        return dist
    elif direction == 2:    #남
        return 2 * w + h - dist
    elif direction == 3:    #서
        return 2 * (w + h) - dist
    elif direction == 4:    #동
        return w + dist

store_num = int(input()) # 상점 수
store = []

# 상점 위치 입력 받기
for _ in range(store_num):
    store.append(list(map(int, input().split())))

# 동근 위치 입력 받기
dg_direct, dg_dist = list(map(int, input().split()))
dg_dist = cal_dist(dg_direct, dg_dist)

# 둘레
total_dist = 2 * (w + h)

result = 0

for i in range(len(store)):
    store_dist = cal_dist(store[i][0], store[i][1])

    dist1 = abs(store_dist - dg_dist)
    dist2 = total_dist - dist1

    result += min(dist1, dist2)


print(result)