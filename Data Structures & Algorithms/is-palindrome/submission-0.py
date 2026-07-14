class Solution:
    def isPalindrome(self, s: str) -> bool:
        #flip the word
        #remove the non-alphanumeric numbers
        cleanedS = ''.join(char.lower() for char in s if char.isalnum())
        flippedWord = cleanedS[::-1] #flipped word without charcters

        return cleanedS == flippedWord
        

       
        print(cleanedS)
        print(flippedWord)
        