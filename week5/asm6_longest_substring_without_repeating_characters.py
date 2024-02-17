class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        answer, startpoint = 0, 0
        substr_dict = {}
        for endpoint in range(len(s)):
            curr_s = s[endpoint]
            if curr_s in substr_dict:
                startpoint = max(startpoint, substr_dict[curr_s] + 1)
            substr_dict[curr_s] = endpoint
            answer = max(answer, endpoint - startpoint + 1)
        return answer


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s="abcabcbb"))  # 3
    print(solution.lengthOfLongestSubstring(s="pwwkew"))  # 3
    print(solution.lengthOfLongestSubstring(s=" "))  # 1
    print(solution.lengthOfLongestSubstring(s="dvdf"))  # 3
    print(solution.lengthOfLongestSubstring(s="bbbbb"))  # 1
