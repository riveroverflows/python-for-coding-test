class Solution:
    @staticmethod
    def is_valid(s: str) -> bool:
        stack = list()
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
                continue
            if char in [')', '}', ']']:
                pop = stack.pop()
                if char == ')' and pop != '(':
                    return False
                if char == '}' and pop != '{':
                    return False
                if char == ']' and pop != '[':
                    return False
        return not stack


print(Solution.is_valid(s="()"))
print(Solution.is_valid(s="()[]{}"))
print(Solution.is_valid(s="(]"))
