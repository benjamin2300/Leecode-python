class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) != 0:
                    p = stack.pop()
                    if not self.match(p, c):
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
    
    def match(self ,left, right):
        if left == '(' and right == ')':
            return True
        elif left == '[' and right == ']':
            return True
        elif left == '{' and right == '}':
            return True
        return False