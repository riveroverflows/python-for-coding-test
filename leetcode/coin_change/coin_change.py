from collections import deque
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque()
        queue.append((amount, 0))
        visited = set()

        while queue:
            remain_amount, qty = queue.popleft()
            if remain_amount == 0:
                return qty

            for coin in coins:
                change = remain_amount - coin
                if change not in visited and 0 <= change:
                    queue.append((change, qty + 1))
                    visited.add(change)

        return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.coinChange(coins=[1, 2, 5], amount=11))
    print(solution.coinChange(coins=[1, 2, 3, 4, 5], amount=11))
