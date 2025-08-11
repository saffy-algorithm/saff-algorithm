#배열 원소 중 최댓값 max_v 찾기
arr = [0, 32, 23, 44, 56]
N = len(arr)
max_v = arr[0]
for i in range(1, N):
    if max_v < arr[i]:
        max_v = arr[i]

# 배열 원소 중 최댓값의 인덱스 max_idx 찾기
max_idx = 0
for i in range(1, N):
    if arr[max_idx] < arr[i]:
        max_idx = i

# 배열 원소의 합
s = 0
for i in range(N):
    s+= arr[i]


#

