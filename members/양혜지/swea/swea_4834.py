T = int(input())

for tc in range(1,T+1):
    N = int(input())
    numbers = []
    input_num = map(int,input())
    numbers.extend(input_num)
 
    count =  [0] * 10
 
    for num in numbers:
        count[num] += 1
 
    max_num = 0
    max_idx = 0

    for idx in range(len(count)): 
        if count[idx] >= max_num:
            max_num = count[idx]
            max_idx = idx
    print(f"#{tc} {max_idx} {max_num}")