# https://www.acmicpc.net/problem/1316

N = int(input()) # test case 수
cnt = N # 처음에는 모든 문자가 그룹단어라고 가정

for _ in range(N):
    word = input() # test case 하나씩 입력

    for i in range(len(word) - 1): # 현재 스펠링과 '다음' 스펠링 비교할 것 => len(word) - 1 까지 반복
        if word[i] == word[i+1]: # 현재와 다음 스펠링이 같으면 pass
            pass
        elif word[i] in word[i+1:]: # 현재와 다음 스펠링이 다르면서 그 이후에 나타난다면
            cnt -= 1 # cnt 1 감소
            break # 그룹단어 아님을 확인했으므로 break

print(cnt)