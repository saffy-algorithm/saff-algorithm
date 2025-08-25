# 중위 순회

T = 10

def inorder(node):
    if node*2 <= N:
        inorder(node*2)
    print(chars[int(tree[node])], end = '')
    if node*2+1 <= N:
        inorder(node*2+1)


for tc in range(1, T+1):
    N = int(input())

    # N 개 인덱스 번호 (1의 자식이 무조건 2, 3이 아니다. 1만 고정)
    tree = [0] * (N+1)

    # N 개 인덱스 번호에 해당하는 문자
    chars = [''] * (N+1)

    tree[1] = 1
    for _ in range(N):
        info = input().split()

        if len(info) == 4:
            index, char, left, right = info
            # 1. 자기 인덱스에 글씨 적어넣기 -> 공통부분이라 한 번에 처리
            # 2. 왼쩍 자식 노드 번호 등록해놓기
            tree[int(index)*2] = left
            # 3. 오른쪽 자식노드 번호 등록해놓기
            tree[int(index)*2+1] = left


        elif len(info) == 3:
            index, char, left = info
            # 1. 자기 인덱스에 글씨 적어넣기 -> 공통부분이라 한 번에 처리
            # 2. 왼쩍 자식 노드 번호 등록해놓기
            tree[int(index)*2] = left

        else: # len(info) == 2:
            index, char = info
            # 1. 자기 인덱스에 글씨 적어넣기 -> 공통부분이라 한 번에 처리

        # 1. 자기 인덱스에 글씨 적어넣기
        chars[int(index)] = char
        # chars.append(char)
    print(f"#{tc} ", end = "")
    inorder(1)
    print()
    

# 8            
# 1 W 2 3
# 2 F 4 5
# 3 R 6 7
# 4 O 8
# 5 T
# 6 A
# 7 E
# 8 S