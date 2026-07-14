class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #edge case
        #empty - return false
        #else search, use a dict(collection), return true if count exceeds 1
        #return false otherwise

        dicts = {} #{1:1, 2:1, }
        count = 0

        for num in nums:
            if num in dicts:
                dicts[num] += 1
                count+=1

            else:
                dicts[num] = 1
        for num, count in dicts.items():
            if count > 1:
                return True
        return False
