from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}
        for s in strs:
            sorted_s = sorted(list(s))
            sorted_key = str(sorted_s)
            if sorted_key in answer:
                el = answer[sorted_key]
                el.append(s)
                answer[sorted_key] = el
            else:
                answer[sorted_key] = [s]
        return list(answer.values())


if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(solution.groupAnagrams(strs=["ddddddddddg", "dgggggggggg"]))
