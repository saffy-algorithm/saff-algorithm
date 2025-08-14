# 계산기1

# stack = [] -> 피연산자 나오면 스택에 append
# 연산자는 연산자 스택에 append
# 다 반복하면 stack에 값 한개만 남고 그걸 print

T = 10
for tc in range(1, T+1):
    N = int(input())
    num_list = input()
    
    stack = []
    stack2 = []
    
    for i in range(N):
        if num_list[i] == '+':
            stack2.append(num_list[i])
        else:
            stack.append(int(num_list[i]))
            
        if len(stack) >= 2 and len(stack2) >=1:
            x = stack.pop()
            y = stack.pop()
            stack.append(x+y)
            
    answer = stack.pop()
    print(f'#{tc} {answer}')