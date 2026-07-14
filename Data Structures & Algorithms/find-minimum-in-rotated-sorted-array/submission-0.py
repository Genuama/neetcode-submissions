class Solution:
    def findMin(self, nums: List[int]) -> int:
        #binary search

        l = 0
        r = len(nums) - 1
        output = 0


        while l < r:
            mid = (r+l)//2

            if nums[mid] > nums[r] :
                l = mid +1
            elif nums[mid] < nums[r]:
                r = mid

        return nums[r]
        