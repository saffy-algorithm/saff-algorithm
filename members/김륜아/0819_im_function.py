# IM

def door(i):
    global cnt
    
    if i == 1:
        cnt += 1
        i += 1
        door(i)

    elif i > 1:
        if visited[i] == 0:
            visited[i] = 1
            i = door_raw[i]
            cnt += 1
            door(i)
        
        elif visited[i] == 1:
            i += 1
            cnt += 1

            if i == N:
                return
            else:
                door(i)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    raw = list(map(int, input().split()))

    # raw 데이터 0번째 인덱스에 의미없는 0을 넣어줌
    door_raw = [0]

    # 1번째 문은 1번째 인덱스에 위치하도록 설계
    door_raw += raw
    
    # 방문 리스트 N+1만큼 (0번째는 사용하지 않을 것이다)
    # 아직 방문하지 안 했을 때를 0, 방문하면 1
    visited = [0]*(N+1)

    # 이동한 횟수를 누적 카운트
    cnt = 0

    door(1)

    print(f"#{tc} {cnt}")
