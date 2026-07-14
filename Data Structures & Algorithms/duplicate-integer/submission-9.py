class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #edge case
        #empty - return false
        #else search, use a dict(collection), return true if count exceeds 1
        #return false otherwise

        set_nums = set(nums)

        return len(set_nums) < len(nums)