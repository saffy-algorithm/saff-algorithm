# 각 열에 퀸을 1개 배치하는 조합을 재귀적으로 나열하기

pos = [0] * 8 # 각 열에서 퀸의 위치를 출력

def put() -> None:
    """ 각 열에 배치한 퀸의 위치를 출력 """
    for i in range(8):
        print(f'{pos[i]:2}', end ='')
    print()

def set