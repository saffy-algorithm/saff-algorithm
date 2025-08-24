T = 10 # testcase 개수 10
 
def inorder(node):  # 중위순회하는 함수 구현
    if node * 2 <= N: # 왼쪽 자식노드가 있는경우 왼쪽 자식노드 호출
        inorder(node * 2)
         
    print(chars[node], end="") # 왼쪽 자식노드 호출이 끝나면 chars[node]에 저장된 글자 출력
     
    if node * 2 + 1 <= N:   # 오른쪽 노드가 있는경우 오른쪽노드 호출
        inorder(node * 2 + 1) 
         
 
for tc in range(1, T + 1):
    N = int(input()) # node의 수
    tree = [0] * (N + 1) # tree / 1부터 N까지의 노드 /  0번 인덱스는 사용하지않음
    chars = [''] * (N + 1) # 글자를 저장 / 인덱스로 자식을 알 수 없기 때문에 해당 노드 번호에 맞는 글자 확인용
     
    tree[1] = 1 # tree의 root는 1로 주어짐
      
    for _ in range(N): # 트리의 정보를 N번 입력받음
        info = input().split() # 정보 입력
         
        if len(info) == 4: # info의 입력길이가 4인경우
            index, char, left, right = info
            # 1. 자기 인덱스에 글씨 적어넣기
            # 2. 왼쪽 자식노드 번호 등록해놓기
            tree[int(index) * 2] = left
            # 3. 오른쪽 자식노드 번호 등록해놓기
            tree[int(index) * 2 + 1] = right
             
        elif len(info) == 3: # 길이가 3인경우
            index, char, left = info
            # 1. 자기 인덱스에 글씨 적어넣기
            # 2. 왼쪽 자식노드 번호 등록해놓기
            tree[int(index) * 2] = left
             
        else:                # 길이가 2인경우
            index, char = info
            # 1. 자기 인덱스에 글씨 적어넣기
             
        chars[int(index)] = char # 1번행동은 모든경우에 해야하므로 밖으로 빼서 동작
     
    print(f'#{tc}', end=" ")    # testcase 번호부터 출력
    inorder(1)
    print() # 모든 출력이 끝난 후 한줄 띄우기
