# 사칙연산

# 숫자만 있는지 or 연산자까지 있는지 고려
# 후위 순회
def post_order(n):
    if left[n] != 0 or right[n] != 0: # 현재 노드
        x = post_order(left[n]) # 왼쪽 서브트리값
        y = post_order(right[n]) # 오른쪽 서브트리값
        if tree[n] == "-":
            return x - y
        elif tree[n] == "+":
            return x + y
        elif tree[n] == "*":
            return x * y
        elif tree[n] == "/":
            return x / y
    # 현재 노드가 걍 숫자만 있으면 값 그대로 리턴
    else:
        return tree[n]
    
 # 테스트케이스 10개 
T = 10
for tc in range(1, T + 1):
    N = int(input())

    # 트리 만들기 > 완전이진트리
    tree = [0] * (N + 1) # 노드 번호에 해당하는 값 저장
    left = [0] * (N + 1) # 왼쪽 번호 저장
    right = [0] * (N + 1) # 오른쪽 번호 저장
    for i in range(N):
        x = list(map(str, input().split())) # 한줄로 노드정보 입력 받기
        if len(x) == 2: # 길이가 2면
            tree[int(x[0])] = int(x[1]) # 숫자노드다
        else: # 그게 아니면 (길이가 4면)
            tree[int(x[0])] = x[1] # 연산자 저장
            left[int(x[0])] = int(x[2]) # 왼쪽 자식
            right[int(x[0])] = int(x[3]) # 오른쪽 자식

    # 1번으로 돌아오니까 1번 계산 결과 저장하고 프린트        
    answer = int(post_order(1))
    print(f'#{tc} {answer}')