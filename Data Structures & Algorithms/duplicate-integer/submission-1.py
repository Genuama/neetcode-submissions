class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set(nums)
        print(mySet)
        if len(mySet) == len(nums):
            return "false"
        else:
            return "true" 
         