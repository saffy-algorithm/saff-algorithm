T = int(input())

for tc in range(1, T+1):
    num_list = list(map(int, input().split()))

    num_sum = sum(num_list)
    avr = round(num_sum / len(num_list))
    
    print(f'#{tc} {avr}')