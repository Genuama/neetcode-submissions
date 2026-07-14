class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s =s.replace(" ","")   
        lower_s = new_s.lower()
        clean_text = ''.join(char for char in lower_s if char.isalnum())

        return clean_text== clean_text[::-1]