class Solution:
    def isValid(self, s: str) -> bool:
        arr_s = list(s)
        stack = []

        for b in arr_s:
            if b in "({[":
                stack.append(b)
            
            if b == ')':
                if (len(stack) == 0 or stack[-1] != '('):
                    return False
                else:
                    stack.pop()


            if b == ']':
                if (len(stack) == 0 or stack[-1] != '['):
                    return False

                else:
                    stack.pop()
            
            if b == '}':
                if (len(stack) == 0 or stack[-1] != '{'):
                    return False

                else:
                    stack.pop()
            
        return len(stack) == 0
            