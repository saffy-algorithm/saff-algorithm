for tc in range(10):
    N = int(input())
    buildings = list(map(int, input().split()))
 
    total_view = 0 # 총 조망권
 
    for i in range(2, N-2):
        neighbor_apt = [buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2]]
        if buildings[i] > max(neighbor_apt):
            view = buildings[i] - max(neighbor_apt)
            total_view += view
 
    print(f'#{tc+1} {total_view}')