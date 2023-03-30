class Solution:
    @staticmethod
    def is_valid(s: str) -> bool:
        stack = list()
        for char in s:
            if char == '(':
                stack.append(')')
                continue
            if char == '{':
                stack.append('}')
                continue
            if char == '[':
                stack.append(']')
                continue
            if not stack or stack.pop() != char:
                return False
        return not stack


print(Solution.is_valid(s="()"))
print(Solution.is_valid(s="()[]{}"))
print(Solution.is_valid(s="(]"))
print(Solution.is_valid(s="{(([]))[]}"))
