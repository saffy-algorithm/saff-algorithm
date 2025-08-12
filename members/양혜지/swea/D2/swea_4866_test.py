T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    N = len(arr)
    check = []
    switch = 1

    for i in range(N):
        if arr[i] == "(" or arr[i] == "{":
            check.append(arr[i])
        elif arr[i] == ")":
            if not check:
                switch = 0
                break
            k = check.pop()
            if k == "(":
                pass
            else:
                switch = 0
                break
        elif arr[i] == "}":
            if not check:
                switch = 0
                break
            k = check.pop()
            if k == "{":
                pass
            else:
                switch = 0
                break
    if check:
        switch = 0
    print(f'#{tc} {switch}')