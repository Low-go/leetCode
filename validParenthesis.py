class Solution:
    def isValid(self, s: str) -> bool:
        #use of a stack to simplify this

        stack =[]

        if len(s) == 1:
            return False

        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            elif i == ")":
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif i == "]":
                if len(stack) > 0 and stack[-1] == "[":
                    stack.pop()
                else: return False
            elif i == "}":
                if len(stack) > 0 and stack[-1] == "{":
                    stack.pop()
                else:
                    return False


        if len(stack) == 0:
            return True
        else:
            return False
