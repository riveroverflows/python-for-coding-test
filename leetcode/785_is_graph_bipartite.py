from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        q = deque()
        color = True
        for i in range(len(graph)):
            visited = {i: color}
            q.append(i)
            while q:
                cur_v = q.popleft()
                color = visited[cur_v]
                for next_v in graph[cur_v]:
                    if next_v in visited:
                        if visited.get(next_v) == color:
                            return False
                    else:
                        q.append(next_v)
                        visited[next_v] = not color
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
    print(solution.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
