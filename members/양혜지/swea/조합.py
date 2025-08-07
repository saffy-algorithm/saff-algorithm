# 순열, 내가 뭘 골랐던 지 간에 탐색 범위에 영향을 미치지 않음

# 조합은 탐색 범위 바뀜
# 뭐 하나를 고르면 고른 것보다 큰 걸 다음걸로 고름
# 이 특징 때문에 얘는 방문 체크할 필요가 없음
# 탐색 범위 자체가 고른 녀석은 건너뛰고 체크하니깐

numbers = [1, 2, 3, 4, 5]
picked_numbers = []
M = 3

# 고른 수 뿐만 아니라, 몇번 째까지 골랐는 지를 인자로 넘겨줘야됨
# 고른 거 이후부터 새로골라! 라고 해야하니깐
def comb(count, idx):
    if count == M:
        print(picked_numbers)
        return
    
    # idx 부터 찾아보렴
    for i in range(idx, len(numbers)):
        picked_numbers.append(numbers[i])
        # 다음 호출을 할 때 전달해줘야돼 다음 범위를
        # idx : 지금 당장 탐색하고자하는 범위의 시작점
        # 내가 전달 할 건 고른 녀석을 넘겨줘야지요
        comb(count+1, i+1)
        picked_numbers.pop()

comb(0, 0)

################################################################
# 조합은 어떻게 보면 부분 집합이래

numbers = [1, 2, 3, 4, 5]
picked_numbers = []
M = 3

def comb(count, idx):
    print(picked_numbers) # 찍어내는 것만 위로 올려보라는데? 이해못함
    # 아 조합에서는 뽑고뽑고 노드 끝 맨 마지막만 출력을 했던 건데
    # 부분 집합은 그 뽑는 중간 과정을 전부 출력을 하면 부분집합 뽑는거랑 똑같아져서
    # 과정 전체를 보면 부분 집합이랑 똑같대
    if count == 5:
        return
    
    for i in range(idx, len(numbers)):
        picked_numbers.append(numbers[i])
        comb(count+1, i+1)
        picked_numbers.pop()

comb(0, 0)

# 실수했다는데
# M개 중에 N개 뽑기
# 고른 수가 M보다 작아
# 부분집합은 M개 중에 M개 뽑는 거 까지해야된대
# 그래서 탈출 조건을 M 까지로 해야된대 count == 5로
# 먼말인지모르겠더욤