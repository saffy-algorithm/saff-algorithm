
for tc in range (1, 11):
    build_num = int(input())
    builds = list(map(int, input().split()))
    
    num_i = []
    for i in range(2, build_num-2):
        if builds[i] - builds[i-1] > 0 and builds[i] - builds[i+1] > 0:
            if builds[i] - builds[i-2] > 0 and builds[i] - builds[i+2] > 0:
                num_i.append(i)
    count = 0
    for n in num_i:
        count += builds[n] - max(builds[n-2], builds[n-1], builds[n+1], builds[n+2])
    print(f"#{tc} {count}")



# for tc in range(1, 11):
# build_num = int(input())
# builds = list(map(int, input().split()))

# total_view = 0

# for i in range(2, build_num - 2):
#     # 현재 위치 기준으로 양쪽 2칸의 최대값 구하기
#     max_neighbor = max(builds[i - 2], builds[i - 1], builds[i + 1], builds[i + 2])

#     # 현재 건물이 그들보다 높은 경우에만 조망권 발생
#     if builds[i] > max_neighbor:
#         total_view += builds[i] - max_neighbor

# print(f"#{tc} {total_view}")