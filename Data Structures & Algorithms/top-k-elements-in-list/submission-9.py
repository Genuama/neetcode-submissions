class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        output = []

        for n, count in counts.items():
            #sorted based on frequency
            #print first k
            sorted_items = sorted(counts.items(), key = lambda x: x[1], reverse=True)
        print(sorted_items)
        for i in range(k):
            output.append(sorted_items[i][0])
        return output
       

       #print(sorted(nums))
        