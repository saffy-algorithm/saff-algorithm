# 1번째
# for tc in range(1, 11):
#     buildings_num = int(input())
#     buildings_height = list(map(int, input().split()))
#     max_building_heigt = 0
#     for i in range(2, buildings_num-2):
#         if buildings_height[i]>= max(buildings_height[i-2],
#                                      buildings_height[i-1],buildings_height[i+1],buildings_height[i+2]):
#             max_building_heigt += (buildings_height[i]-max(buildings_height[i-2], buildings_height[i-1],
#                                                             buildings_height[i+1],buildings_height[i-2]))
#     print(f'#{tc} {max_building_heigt}')


# 2번째
# for tc in range(1, 11):
#     buildings_num = int(input())
#     N = list(map(int, input().split()))
#     max_d = 0
#     for i in range(2, buildings_num-2):
#         if max(N[i-2:i+3])==N[i]:
#             high = max(max(N[i-2:i]), max(N[i+1:i+3]))
#             max_d += N[i] - high
#     print(f'#{tc} {max_d}')

# T = int(input())
# for tc in range(1, 1+T):
#     N = int(input())





# 8/7
# for tc in range(1, 11):
#     max_view = 0
#     N = int(input())
#     bi = list(map(int, input().split()))
#     for i in range(2, N-2):
#         max_i = max(bi[i-2], bi[i-1], bi[i+1], bi[i+2])
#         if bi[i]>max_i:
#             max_view += (bi[i]- max_i)
#     print(max_view)

T = int(input())
for tc in range(1, 1+T):
    