# 📅 Week 1 문제 기록


#### 📌 [BOJ 1234 - N과 M (1)](https://www.acmicpc.net/problem/1234)
- **풀이자:** 홍길동
- **풀이 날짜:** 2025.08.01

### 🧠 문제 분석
- DFS를 사용해 1부터 N까지의 숫자를 중복 없이 M개 고르는 순열 생성
- 백트래킹으로 탐색 중 visited 배열로 중복 방지

### 💭 접근
1. 순열을 직접 생성 → itertools.permutations 가능하지만 DFS로 구현
2. 깊이가 M이 되면 결과 저장
3. 탐색 후 visited 원상 복구
