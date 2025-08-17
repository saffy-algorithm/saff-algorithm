for tc in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
 
    for i in range(dump):
        max_idx = boxes.index(max(boxes))
        boxes[max_idx] -= 1
 
        min_idx = boxes.index(min(boxes))
        boxes[min_idx] += 1
     
    height_gap = max(boxes) - min(boxes)
 
     
     
    print(f'#{tc} {height_gap}')