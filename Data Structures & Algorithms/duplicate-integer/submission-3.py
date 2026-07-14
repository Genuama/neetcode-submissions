class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #set
        #convert each array into a set
        #compare it to the original array given to me
        #if the set is equal to the original array, then there are no duplicate integers
        #otherwise there are
        #(o(n))

        
        new_set = set(nums) 
        return len(list(new_set)) != len(nums)
       