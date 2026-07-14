class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        nums_order = {num: i for i, num in enumerate(nums)}
        print(nums_order)
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_order and nums_order[complement] != i:
                return [i, nums_order[complement]]