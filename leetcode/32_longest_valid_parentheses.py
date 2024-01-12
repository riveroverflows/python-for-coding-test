class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        answer = 0
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append([i, ch])
                continue
            if ch == ")":
                if not stack:
                    stack.append([i, ch])
                    continue
                if stack[-1][1] == "(":
                    stack.pop()
                else:
                    stack.append([i, ch])
                    continue
            if stack:
                length = i - stack[-1][0]
            else:
                length = i + 1

            answer = max(answer, length)
        return answer


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestValidParentheses(")(()))()()()"))  # 6
    print(solution.longestValidParentheses("()"))  # 2
    print(solution.longestValidParentheses(")("))  # 0
    print(solution.longestValidParentheses("(()"))  # 2
    print(solution.longestValidParentheses(")()())"))  # 4
    print(solution.longestValidParentheses(""))  # 0
    print(solution.longestValidParentheses("()(()"))  # 2
