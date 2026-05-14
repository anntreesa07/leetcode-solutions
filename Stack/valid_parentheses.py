# 20. Valid Parentheses

#we use a stack to keep track of the opening parentheses. We iterate through the string and for each character, we check if it is an opening or closing parenthesis. If it is an opening parenthesis, we push it onto the stack. If it is a closing parenthesis, we check if the stack is empty (which means there is no corresponding opening parenthesis) or if the top of the stack does not match the corresponding opening parenthesis. If either of these conditions is true, we return False. Finally, we check if the stack is empty at the end of the iteration, which means all parentheses are valid.


class Solution(object):
    def isValid(self, s):
        

        stack=[]

        pairs = {
                    ")" : "(",
                    "]" : "[",
                    "}" : "{"
                }

        for ch in s:
            if ch in '({[':
                stack.append(ch)
            elif stack==[]:
                return False
            elif ch in ']})':
                if stack.pop()!=pairs[ch]:
                    return False

        if stack==[]:
            return True
        else:
            return False

        