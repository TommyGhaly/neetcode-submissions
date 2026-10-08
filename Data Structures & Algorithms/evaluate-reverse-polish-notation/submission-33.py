class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for t in tokens:
            if t in ("+", "-", "*", "/"):
                b = nums.pop()
                a = nums.pop()
                if t == "+":
                    nums.append(a + b)
                elif t == "-":
                    nums.append(a - b)
                elif t == "*":
                    nums.append(a * b)
                else:
                    nums.append(int(a / b))
            else:
                nums.append(int(t))
        return nums[0]