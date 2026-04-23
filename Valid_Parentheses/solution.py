class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                top = stack.pop() if stack else None
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)

        return not stack
