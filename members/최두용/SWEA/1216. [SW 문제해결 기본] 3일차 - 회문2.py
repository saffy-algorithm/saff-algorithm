# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14Rq5aABUCFAYi

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