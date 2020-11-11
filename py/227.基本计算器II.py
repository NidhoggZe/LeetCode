
class Solution:
    def calculate(self, s: str) -> int:
        nums = []
        ops = []
        dic = {'+':1, '-':1, '*':2, '/':2}
        last = 0


        for c in s:
            if c == ' ':
                continue
            if c.isdigit():
                last = last * 10 + int(c)
            else:
                nums.append(last)
                last = 0
                while ops and dic[ops[-1]] >= dic[c]:
                    if ops[-1] == '*':
                        ops.pop()
                        num2 = nums.pop()
                        num1 = nums.pop()
                        nums.append(num1 * num2)
                    elif ops[-1] == '/':
                        ops.pop()
                        num2 = nums.pop()
                        num1 = nums.pop()
                        nums.append(num1 // num2)

                    elif c == "+" or c == '-':
                        if ops[-1] == '+':
                            ops.pop()
                            num2 = nums.pop()
                            num1 = nums.pop()
                            nums.append(num1 + num2)
                        elif ops[-1] == '-':
                            ops.pop()
                            num2 = nums.pop()
                            num1 = nums.pop()
                            nums.append(num1 - num2)
                ops.append(c)
        
        nums.append(last)

        while ops:
            op = ops.pop();
            if op == '+':
                num2 = nums.pop()
                num1 = nums.pop()
                nums.append(num1 + num2)
            elif op == '-':
                num2 = nums.pop()
                num1 = nums.pop()
                nums.append(num1 - num2)
            elif op == '*':
                num2 = nums.pop()
                num1 = nums.pop()
                nums.append(num1 * num2)
            elif op == '/':
                num2 = nums.pop()
                num1 = nums.pop()
                nums.append(num1 // num2)


        return nums[0]


Solution().calculate('1*2-3/4+5*6-7*8+9/10')