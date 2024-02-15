from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}
        for s in strs:
            str_set = sorted(list(s))
            set_to_str = str(str_set)
            if set_to_str in answer:
                el = answer[set_to_str]
                el.append(s)
                answer[set_to_str] = el
            else:
                answer[set_to_str] = [s]
        return list(answer.values())


if __name__ == "__main__":
    solution = Solution()
    # print(solution.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(solution.groupAnagrams(strs=["ddddddddddg", "dgggggggggg"]))
