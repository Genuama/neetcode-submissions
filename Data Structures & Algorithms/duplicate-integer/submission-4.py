class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       #use a dictionary
       #return True if any value has a count more than once, return false otherwise

        dict = Counter(nums)  

        for n,count in dict.items():
            if count > 1:
                return True
        return False