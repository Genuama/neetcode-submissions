class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #edge case
        #empty - return false
        #else search, use a dict(collection), return true if count exceeds 1
        #return false otherwise

        if not nums:
            return False

        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        for el, n in counts.items():
            if n > 1:
                return True
        return False
        