class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {"(" : ")", "{" : "}", "[" : "]"}
        stack = []

        for c in s:
            # opening bracket -> push onto stack
            if c in parentheses:
                stack.append(c)
            
            else: # closing bracket
                if not stack:
                    return False # can't put closing bracket first into empty stack
                
                top_of_stack = stack.pop()

                if parentheses[top_of_stack] != c: # closing in dictionary != current closing
                    return False

        return not stack # if stack is full, not valid
