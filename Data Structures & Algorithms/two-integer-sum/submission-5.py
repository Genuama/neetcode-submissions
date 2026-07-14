class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #{3: 0, }

        for i, num in enumerate(nums): #{0: 3, 1:4, 2:5, 3:6}
            diff = target - num #4

            if diff in seen:
                return [seen[diff], i] #[0,1]
            seen[num] = i #
    

        

        