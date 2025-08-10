def number_to_int(txt):
    if txt == "ZRO":
        return (0, txt)
    elif txt == "ONE":
        return (1, txt)
    elif txt == "TWO":
        return (2, txt)
    elif txt == "THR":
        return (3, txt)
    elif txt == "FOR":
        return (4, txt)
    elif txt == "FIV":
        return (5, txt)
    elif txt == "SIX":
        return (6, txt)
    elif txt == "SVN":
        return (7, txt)
    elif txt == "EGT":
        return (8, txt)
    elif txt == "NIN":
        return (9, txt)
    
T = int(input())

for tc in range(1, T+1):
    a, N = map(str, input().split())
    N = int(N)
    number = list(map(str, input().split()))
    arr_num = []
    
    for i in range(N):
        x = number[i]
        arr_num.append(number_to_int(x))
    arr_num.sort()
    
    print(f'#{tc}')
    for j in range(N):
        print(arr_num[j][1], end=" ")
    print()
        
        
    
    