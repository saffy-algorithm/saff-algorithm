'''
- 인도네시아 내의 모든 섬을 해저터널로 연결하려 함
- 직접적으로 연결된 경우도 있지만 간접적으로 연결 된 경우도 있다

# 조건
- 환경 부담금 정책이 있음
환경 부담 세율(E)와 각 해저터널 길이(L)의 제곱(E *L^2)만큼 지불


# 입력
첫 줄은 전테 테스트 케이스
섬의 개수 N이 주어짐
각 섬들의 정수인 X좌표, 세 번째 줄에는 각 섬들의 정수인 Y좌표가 주어짐
마지막에 E가 주어짐

'''

def is_palindromic_row(board, r, c, length):
    left = 0
    right = length - 1
 
    while left < right:
        if board[r][c + left] != board[r][c + right]:
            return False
        left += 1
        right -= 1
 
    return True
 
def is_palindromic_col(board, r, c, length):
    top, bottom = 0, length - 1
    while top < bottom:
        if board[r + top][c] != board[r + bottom][c]:
            return False
        top += 1
        bottom -= 1
    return True
 
def solution():
    # _ = input()
    N = 100
    board = [list(input()) for _ in range(N)]
    for length in range(N, 1, -1):
        for r in range(N):
            for c in range(N - length + 1):
                if is_palindromic_row(board, r, c, length):
                    return length
                if is_palindromic_col(board, c, r, length):
                    return length
 
    return 1
 
for _ in range(1, 11):
    t = int(input())
    print(f'#{t} {solution()}')
