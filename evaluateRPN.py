from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []



        for i in tokens:
            if i == "+":
                hold1 = stack.pop()
                hold2 = stack.pop() #make sure to start the operation with this one
                homie = hold2 + hold1
                stack.append(homie)
            elif i == "-":
                hold1 = stack.pop()
                hold2 = stack.pop()  # make sure to start the operation with this one
                homie = hold2 - hold1
                stack.append(homie)
            elif i == "*":
                hold1 = stack.pop()
                hold2 = stack.pop()  # make sure to start the operation with this one
                homie = hold2 * hold1
                stack.append(homie)
            elif i == "/":
                hold1 = stack.pop()
                hold2 = stack.pop()  # make sure to start the operation with this one
                homie = (hold2 // hold1)
                stack.append(homie)
            else:
                change = int(i)
                stack.append(change)
        return stack[0]



solution = Solution()
the = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
result = solution.evalRPN(the)
print(result)