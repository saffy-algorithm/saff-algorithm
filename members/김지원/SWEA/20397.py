T= int(input())
 
for tc in range(T):
    M,N = map(int,input().split())
 
    arr = list(map(int,input().split()))
 
    for k in range(N):
        i,j = map(int,input().split()) 
        mid = i-1
        for num in range(1,j+1):
            if 0 <= mid - num < M and 0 <= mid + num < M:
                if arr[mid-num] == arr[mid+num]:
                    arr[mid+num] = 1 - arr[mid+num]
                    arr[mid-num] = 1- arr[mid-num]
         
         
    arr = [str(num) for num in arr]
 
    print(f"#{tc+1} {' '.join(arr)}")
 
