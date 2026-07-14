class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search problem
        #check if left half is sorted, move pointer accordingly, check right half otherwise

        l  = 0
        r = len(nums) - 1


        while l<=r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
         