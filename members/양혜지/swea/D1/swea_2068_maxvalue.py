# T = int(input())

# for i in range(N)

T = int(input())


for tc in range(1, T+1):
    numbers = list(map(int,input().split()))
    max_value = -1
    
    for number in numbers:
        if max_value < number:
            max_value = number
        
    # for idx in range(len(numbers)):
        
    
    print(f'#{tc} {max_value}')

