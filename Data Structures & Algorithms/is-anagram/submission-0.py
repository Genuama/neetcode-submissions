class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if the both have different lenghts, they are not anagrams
        #how do you check that it is indeed an anagram?
        #how do i compare both strings to check that they both have the same characters.
        #sort both strings alphabeticallly, if they are the same, return true, return false otherwise


       
       
        new_s = list(s)
        new_s.sort()

        new_t = list(t)
        new_t.sort()
        return new_s == new_t



        