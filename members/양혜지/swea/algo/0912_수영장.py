# # 완전 탐색

# # 1. 종료 조건 : 12개월을 모두 고려한 경우
# # 2. 가지의 수 : 4게 (1일, 1달, 3달, 1년)
# def recur(month, total_cost):
#     global min_answer
#     if month > 12:
#         # Todo : 최소값 갱신
#         min_answer = min(min_answer, total_cost)
#         return

#     # 1일권으로 다 사는 경우 -> 다음달로 재귀호출이 넘어감
#     # 현재 달에 1일권 가격으로 일수를 곱해서 더해준 값을 다음 재귀 호출로 넘겨주는 거
#     recur(month +1, total_cost + (days[month] * cost_day))   
#     # 1달권으로 다 사는 경우 -> 
#     recur(month +1,  total_cost, cost_month)
#     # 3달권으로 다 사는 경우 -> 
#     recur(month +3, total_cost, cost_month3)
#     # 1년 이용권으로 사는 경우 -> 12 더해주고 끝냄 '
#     # (1월에 사는 거 아니면 의미없긴 함 -> 재귀 밖에서 해도 되는 조건)
#     recur(month +12, total_cost, cost_year)


# T = int(input())
# for tc in range(1, T+1):
#     # 이용권 가격들 (1일, 1달, 3달, 1년)
#     cost_day, cost_month, cost_month3, cost_year = map(int, input().split())
#     # 12개월 이용계획 (1월부터 생각할 수 있도록 인덱스에 0을 붙여줘버림)
#     days = [0] + list(map(int, input().split()))
#     min_answer = 31 * 12 * 3000 # 최대금액 (31일 * 12개월 * 3000원)
#     recur(1, 0) # 1월부터 시작
#     print(f'#{tc} {min_answer}')


# DP (재귀 호출보다 금방 끝남)
T = int(input())
for tc in range(1, T+1):
    # 이용권 가격들 (1일, 1달, 3달, 1년)
    cost_day, cost_month, cost_month3, cost_year = map(int, input().split())
    # 12개월 이용계획 (1월부터 생각할 수 있도록 인덱스에 0을 붙여줘버림)
    days = [0] + list(map(int, input().split()))

    # 누적해서 저장해 나아갈 dp 리스트 (그림과 동일)
    dp = [0] * 13
    # 시작점 초기화 (1월, 2월)
    # 1월의 가격 (1일권 구매 vs 1달권 구매)
    dp[1] = min(days[1] * cost_day, cost_month)
    # 2월의 가격 = 1월의 가격 + (1일권 구매 vs 1달권 구매)
    dp[2] = dp[1] + min(days[2] * cost_day, cost_month)

    # 3월 ~ 12월은 반복하면서 계산
    for month in range(3, 13):
        # N월의 최소 비용 후보
        # 1. (N-3)월에 3개월 이용권을 구입한 경우
        # 2.  (N-1)월의 최소 비용 + 1일권 구매
        # 3.  (N-1)월의 최소 비용 + 1달권 구매
        dp[month] = min(dp[month-3] + cost_month3
                        , dp[month-1] + (days[month] * cost_day)
                        , dp[month-1] + cost_month)
        
    # 12월의 누적 최소 금액 vs 1년권
    answer = min(dp[12], cost_year)
    print(f'#{tc} {answer}')
 
# 따라서
# 완탐 먼저 고려 -> 안되면 DP -> 안되면 Greedy