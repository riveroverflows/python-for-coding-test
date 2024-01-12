class Solution:
    def longestValidParentheses(self, s: str) -> int:
        answer = 0
        if len(s) < 2:
            return 0
        for i, ch in enumerate(s):
            if ch == "(":
                if i == 0:
                    answer += 1
                    continue
                if i > 0:
                    if s[i - 1] == ")" and i + 1 < len(s) and s[i + 1] == ")":
                        answer += 1
            else:
                if i > 0:
                    if s[i - 1] == "(":
                        answer += 1

        return answer


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestValidParentheses(")("))
    print(solution.longestValidParentheses("(()"))
