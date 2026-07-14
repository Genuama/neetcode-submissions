class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #two pointer approach
        #sort to help us out
        #if sum of i,r,l is less than 0, move left, if equal to zero, move both pointers, otherwise move
        #right pointer
        #update output if sum == 0
        #return output = []


        output = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1

            while l<r:
                sums = nums[i] + nums[r] + nums[l]
                if sums == 0:
                    output.append([nums[i], nums[r], nums[l]])
                    r-=1
                    l+=1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1    
                elif sums < 0:
                    l+=1
                else:
                    r-=1
        return output


        