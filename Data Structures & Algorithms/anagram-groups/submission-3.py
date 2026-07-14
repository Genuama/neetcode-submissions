class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #use a dict
        #sort words and add to the dict
        #iterate through list
        #take first word
        #if sorted word is in dict, add to the list
        #otherwise, add it as a key value pair sorted: [word] 
        #return the values in the dict in the form of a list 

        dict = {}
        for word in strs: #pots
            key = ''.join(sorted(word)) #opst
            if key not in dict: 
                dict[key] = [] 
            dict[key].append(word)
        return list(dict.values())


