T = 10

for tc in range(1, T+1):
    N = int(input())
    boxes = list(map(int, input().split()))
    
    for i in range(N):
        # 최대, 최소 인덱스 찾기
        max_idx = 0
        min_idx = 0
        
        for j in range(1, len(boxes)):
            if boxes[j] > boxes[max_idx]:
                max_idx = j
            if boxes[j] < boxes[min_idx]:
                min_idx = j
        
        # 평탄화 작업
        boxes[max_idx] -= 1
        boxes[min_idx] += 1
        
        # 박스 높이 차이가 1 이하이면 종료
        if boxes[max_idx] - boxes[min_idx] <= 1:
            break
    
    # 다시 한 번 최대/최소 계산
    max_val = boxes[0]
    min_val = boxes[0]
    
    for h in boxes:
        if h > max_val:
            max_val = h
        if h < min_val:
            min_val = h
    
    answer = max_val - min_val
    print(f'#{tc} {answer}')