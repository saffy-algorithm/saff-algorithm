T = int(input())
for tc in range(1, T+1):
    width = int(input()) # 0~8
    heights = list(map(int, input().split()))
    answer = 0
    max_height = 0
    for i in range(width):
        if heights[i]<= max_height:
            continue
        
        max_height = heights[i]
        fall_count = 0
        for j in range(i+1, width):
            if heights[i]> heights[j]:
                fall_count += 1
            answer = max(answer, fall_count)
    print(f'#{tc} {answer}')