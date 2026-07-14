class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicts = Counter(nums) 
        print(dicts.items())
        sorted_dicts = sorted(dicts.items(), key=lambda x: -x[1]) #the negative sorts it in descending order
        
        #return the list of the first k elements
        top_k = []
        top_k_pairs = sorted_dicts[:k]
        print(top_k_pairs)

        for num,value in top_k_pairs:
            top_k.append(num)
        return top_k
        

