# 최대 높이 / 최대 높이 위치
# 최소 높이 / 최소 높이 위치
# 최대 높이를 빼서 최소 높이에 줘
# 평탄화 n회 하고
# 최대 높이에서 최소높이를 빼

T = 10 # 총 10개의 test case가 주어짐
for tc in range(1, T+1): # 테스트 케이스 1부터 10까지 돌면서
    N = int(input()) # 덤프 횟수를 입력 받아
    boxes = list(map(int,input().split())) # 각 상자의 높이 값 리스트를 입력 받아
    
    for i in range(N): # 덤프 횟수를 돌아
        min_idx = 0 # 최소값의 인덱스 0으로
        max_idx = 0 # 최대값의 인덱스 0으로
        
        for j in range(1, 100): # 덤프 횟수 1부터 99까지 돌아
            if boxes[max_idx] < boxes[j]: # 최대값 인덱스보다 상자 높이값이 크면
                max_idx = j #  위치를 max_idx에 넣기
            if boxes[min_idx] > boxes[j]: # 최소값 인덱스보다 상자 높이값이 작으면
                min_idx = j #  위치를 min_idx에 넣기
                
        boxes[max_idx] -= 1 # 최대값에서는 -1
        boxes[min_idx] += 1 # 최소값에서는 +1을 하면서 평탄화 ㄱㄱ
        
    # 평탄화가 된 최대값 최소값 변수
    max_val = boxes[0] # 평탄화가 된 최대값 -> 받을 변수 지정
    min_val = boxes[0] # 평탄화가 된 최소값 -> 받을 변수 지정
    
    for t in range(len(boxes)):
        max_val = max(max_val, boxes[t]) # boxes를 돌면서 누가누가 제일 높은가 비교
        min_val = min(min_val, boxes[t]) # boxes를 돌면서 누가누가 제일 낮은가 비교
        
    answer = (max_val - min_val) # 최고점 - 최저점
    print(f'#{tc} {answer}')
    
    
        
# for t in range(len(boxes)):
#     if max_val < boxes[t]:
#         max_val = boxes[t]
#     if min_val > boxes[t]:
#         min_val = boxes[t]