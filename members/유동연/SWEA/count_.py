def counting_sort(DATA, Temp, k):

    COUNTS = [0]*(k+1)

    for i in range(len(DATA)):
        COUNTS[DATA[i]] +=1

    for i in range(1, k+1):
        COUNTS[i] += COUNTS[i-1]
    
    for i in range (len(DATA)-1, -1, -1):
        COUNTS[DATA[i]] -= 1
        Temp[COUNTS[DATA[i]]] = DATA[i]

arr = [0, 4, 1, 3, 1, 2, 4, 1] 
result = [0]*len(arr) 
counting_sort(arr, result, max(arr))
print(result)  