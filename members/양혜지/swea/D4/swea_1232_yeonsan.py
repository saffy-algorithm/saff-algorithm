# 사칙연산

def post_order(n):
    if left[n] != 0 or right[n] != 0:
        x = post_order(left[n])
        y = post_order(right[n])
        if tree[n] == "-":
            return x - y
        elif tree[n] == "+":
            return x + y
        elif tree[n] == "*":
            return x * y
        elif tree[n] == "/":
            return x / y
    else:
        return tree[n]
T = 10
for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    for i in range(N):
        x = list(map(str, input().split()))
        if len(x) == 2:
            tree[int(x[0])] = int(x[1])
        else:
            tree[int(x[0])] = x[1]
            left[int(x[0])] = int(x[2])
            right[int(x[0])] = int(x[3])
    answer = int(post_order(1))
    print(f'#{tc} {answer}')