import heapq
from collections import defaultdict
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        adjacency_list = defaultdict(list)
        for idx, (a, b) in enumerate(edges):
            adjacency_list[b].append((a, succProb[idx]))
            adjacency_list[a].append((b, succProb[idx]))

        weights = [0.0] * n
        weights[start_node] = -1.0
        pq = [(-1.0, start_node)]

        while pq:
            curr_weight, curr_node = heapq.heappop(pq)
            for next_node, next_weight in adjacency_list[curr_node]:
                weight = -curr_weight * next_weight
                if weight <= weights[next_node]:
                    continue
                weights[next_node] = weight
                heapq.heappush(pq, (-weight, next_node))

        return weights[end_node]


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProbability(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.2], start_node=0,
                                  end_node=2))
    print(solution.maxProbability(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.3], start_node=0,
                                  end_node=2))
    print(solution.maxProbability(n=3, edges=[[0, 1]], succProb=[0.5], start_node=0, end_node=2))
