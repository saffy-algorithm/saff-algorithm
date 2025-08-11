# 예시 데이터
arr = [10, 20, 30, 40, 50]  # 검색할 리스트
N = len(arr)                # 원소 개수
v = 30                       # 찾고 싶은 값

# 값 찾기
idx = -1
for i in range(N):
    if arr[i] == v:
        idx = i
        break

print(idx)  # 2 (인덱스는 0부터 시작)
--------------------------
arr = [10, 20, 30, 40, 30, 50, 30]
N = len(arr)
v = 30

indexes = []
for i in range(N):
    if arr[i] == v:
        indexes.append(i)

if indexes:
    print("모든 인덱스:", indexes)  # [2, 4, 6]
else:
    print("값이 없음")
------------------

arr = [10, 20, 30, 40, 30, 50, 30]
N = len(arr)
v = 30

idx = -1
for i in range(N):
    if arr[i] == v:
        idx = i  # 찾을 때마다 갱신

print("마지막 인덱스:", idx)  # 6
