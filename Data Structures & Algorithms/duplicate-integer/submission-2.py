class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #set
        #convert each array into a set
        #compare it to the original array given to me
        #if the set is equal to the original array, then there are no duplicate integers
        #otherwise there are
        #(o(n))

        check = set()

        for i in range(len(nums)):
            if nums[i] in check:
                #print(check)
                return True
            else:
                check.add(nums[i])
                print(check)
        return False
        