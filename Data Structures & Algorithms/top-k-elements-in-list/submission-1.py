import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #ouput = []
        #dictionary to keep of all the elements in my array, counter
        #append the first element with the maximum count until the next k
        #return the list(output) in the end

        output = []

        counts = Counter(nums)
        
        arr = []

       
        for key, value in counts.items():
            arr.append([value, key])
            print(arr)
        arr.sort()
        print(arr)

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
            
        