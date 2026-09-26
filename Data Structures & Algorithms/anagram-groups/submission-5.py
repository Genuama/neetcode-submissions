class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = {}
        for string in strs:
            
            sorted_key = "".join(sorted(string))
            if sorted_key in dicts:
                dicts[sorted_key].append(string)
            else:
                dicts[sorted_key] = [string]
        return list(dicts.values())


