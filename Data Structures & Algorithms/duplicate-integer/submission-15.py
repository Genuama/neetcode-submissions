from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #use a set
        dicts = Counter(nums)

        print(dicts)

        for n, count in dicts.items():
            if count > 1:
                return True
        return False
        

        
        