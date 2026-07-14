class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        #output = []
        #if the n(count) of element = k 
        # add element to output
        #return output

        #use counter to get count of each element
        #sort them according to decreasing frequency
        #return [:k] elements

        sorted_keys = sorted(counts, key=lambda x: counts[x], reverse = True)
        return sorted_keys[:k]
        