N =  int(input())
 
for num in range(N):
 
    b = int(input())
 
    a = list(map(int,input().split()))
    result = []
    for i in range(len(a),0,-1):
        count = 0
        for j in range(i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                count += 1
 
        result.append(count)
         
    print(f'#{num+1} {max(result)}')