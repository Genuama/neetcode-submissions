class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dicts = {")": "(", "]": "[", "}": "{"}


        for string in s:
            if string not in dicts:
                stack.append(string)
            else:
                if not stack or stack.pop() != dicts[string]:
                    return False
        return not stack
            
           


        