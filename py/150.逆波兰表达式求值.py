from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for c in tokens:
            if c.isdigit() or (c[0] == '-' and c[1:].isdigit()):
                nums.append(int(c))
            else:
                num2 = nums.pop()
                num1 = nums.pop()
                if c == '+':
                    nums.append(num1 + num2)
                elif c == '-':
                    nums.append(num1 - num2)
                elif c == '*':
                    nums.append(num1 * num2)
                else:
                    nums.append(int(num1 / float(num2)))
        
        return nums[0]

Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])