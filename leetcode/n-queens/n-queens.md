# [N-Queens](https://leetcode.com/problems/n-queens/)

## 조합을 이용한 방법

### 접근 방법

- n 크기의 조합 구하기
- 조합을 순회하면서 퀸의 공격 범위 체크
- 모든 퀸이 서로 공격하지 않으면 answer에 추가
- 조합을 모두 순회하면 answer 리턴

### 결과

- Test Case 통과
- 제출 시 시간 초과
  - `n = 6` 부터 시간 초과