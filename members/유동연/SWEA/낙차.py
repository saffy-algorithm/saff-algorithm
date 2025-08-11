1번째, 연산량이 많음
T = int(input()) #t
for tc in range(T):

    width = int(input()) # 방의 길이
    boxes = list(map(int, input().split())) # 상자의 수
    num = 0
    cnt_lst = []
    for i in range(len(boxes)):
        cnt = 0
        for j in range(1+i, len(boxes)):
            if boxes[i] > boxes[j]:
                cnt+=1
            cnt_lst.append(cnt)
    print(f'#{tc+1} {max(cnt_lst)}')

# 조금 더 조건문 걸어 연산량 낮추기
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


