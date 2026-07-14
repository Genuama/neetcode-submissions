class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #compare the counts of the characters in each word
        countS = Counter(s)
        countT = Counter(t)

        return countS == countT
        