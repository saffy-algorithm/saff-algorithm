def inorder_traverse(T):
    if T <= N:
        inorder_traverse(T*2)
        print(arr[T], end='')
        inorder_traverse(T*2+1)


T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = ['']
    for _ in range(N):
        temp = list(input().split())
        arr.append(temp[1])

    print(f'#{tc}', end=' ') 
    inorder_traverse(1)
    print()
