class Solution:
    def isValid(self, s: str) -> bool:
        dict = {")":"(","}":"{", "]":"["}

        #keep the characters in a hashmap to keep track
        #use a stack
        #if the string is valid it wont have members at the end
        #s= "()"
        stack = []
        for char in s:
            if char in dict: #closing bracket
                if stack and stack[-1] == dict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
        