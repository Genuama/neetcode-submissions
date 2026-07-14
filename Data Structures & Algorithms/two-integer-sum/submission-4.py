class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #a + b = c
        # c - a = b
        
        #how to solve it? 
        # for i in range(len(nums)): 
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        #brute force solution goes through the array twice, 0(n^2)
        #properties that make this easy
        #use a dictionary for 0(1) lookups
        count = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in count:
                return [count[complement], i]
            else:
                count[nums[i]] = i


        