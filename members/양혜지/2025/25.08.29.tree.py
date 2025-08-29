# 전위 순회

def pre_order(T):
    if T > 0:
        print(T,end = ' ') #visit(T)
        pre_order(left[T]) # pre_order(T.left)
        pre_order(right[T])
        
def in_order(T):
    if T > 0:
        in_order(left[T]) # pre_order(T.left)
        print(T,end = ' ') #visit(T)
        in_order(right[T])    
    


V = int(input())
E = V -1
arr = list(map(int,input()))

left = [0] * (V+1) # 부모번호를 인덱스로 자식번호 저장
right = [0] * (V+1)
par = [0] * (V+1) # 자식번호를 인덱스로 부모번호 저장

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    par[c] = p
    
    if left[p] == 0:
        left[p] = c
        
    else:
        right[p] = c
        
        
root = 1
for i in range(1, V+1):
    if par[i] == 0: # 부모노드가 없는 경우
        root = i
        break