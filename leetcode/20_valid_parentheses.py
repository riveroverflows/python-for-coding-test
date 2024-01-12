class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in ("(", "{", "[",):
                stack.append(ch)

            if ch in (")", "}", "]",):
                if not stack:
                    stack.append(ch)
                    continue
                last = stack[-1]
                if ch == ")" and last == "(":
                    stack.pop()
                    continue
                if ch == "}" and last == "{":
                    stack.pop()
                    continue
                if ch == "]" and last == "[":
                    stack.pop()
                    continue
                stack.append(ch)

        return not stack


if __name__ == "__main__":
    solution = Solution()
    # print(solution.isValid("()"))
    # print(solution.isValid("()[]{}"))
    # print(solution.isValid("(]"))
    print(solution.isValid("(])"))
