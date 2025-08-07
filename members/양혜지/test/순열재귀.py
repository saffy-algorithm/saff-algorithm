# 중복 없이 visited 사용
# 순서를 고려해서 M개 숫자를 고른 순열을 모두 출력하는 재귀함수

numbers = [1, 2, 3, 4, 5] # 순열을 만들 숫자들
picked_numbers = [] # 현재까지 고른 숫자들을 저장할 리스트 (지금까지 선택한 숫자를 저장합니다. 이걸 출력할겁니다)
M = 3 # 뽑을 숫자의 개수 (순열의 길이) (지금은 3개짜리 순열을 만들겠다는 뜻)
visited = [0]*len(numbers) # 각 숫자를 썼는지 확인하는 리스트 (0:안씀, 1:사용중) / visited : 같은 숫자를 중복해서 고르지 않기 위해 사용

def perm(count): # 재귀 함수 / count : 현재까지 몇 개 숫자를 골랐는지 나타냄
    # 예를 들어 count =2면 지금 2개 골라서 picked_numbers에 들어있다는 뜻
    if count == M: # 만약에 우리가 M개를 다 골랐다면
        print(picked_numbers) # 순열을 하나 완성한 것이므로 출력하고 함수 종료 (이게 재귀의 종료 조건)
        return
    
    for i in range(len(numbers)): # numbers에 있는 숫자들 중에서 아직 고르지 않은 숫자를 하나씩 선택해보겠다는 의미 / i는 인덱스 (0부터 4까지)
        if visited[i] == 1: # 만약 i번째 숫자를 이미 골랐다면 visited[i] == 1
            continue # 이번에는 건너뜁니다
        picked_numbers.append(numbers[i]) # 아직 고르지 않은 숫자를 picked_numbers에 추가 / 즉, 하나 골랐다는 뜻
        visited[i] = 1 # 이제 이 숫자를 골랐으니, 다시 안 쓰도록 visited[i]=1로 표시
        perm(count+1) # 하나를 골랐으니, 다음 숫자를 고르기 위해 재귀 호출함 / count+1이 되었으니 점점 M에 가까워짐
        picked_numbers.pop() # 위에서 append()로 숫자를 추가했으니, 이제 재귀가 끝나고 돌아올 때는 다시 제거해줘야함 -> 그래야 다른 숫자 넣을 수 있음 (백트래킹 과정)
        visited[i] = 0 # 이 숫자를 다시 안 쓴 상태로 돌려놓음 / 그래야 다른 경우에 이 숫자를 또 쓸 수 있음

perm(0) # 재귀 함수를 처음 호출 / 아직 아무것도 고르지 않았기 때문에 count=0

