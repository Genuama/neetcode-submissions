class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #create an empty list
        #sort all the elements of the list
        #if any of them is similar(have the same characters) attach them to the list with 
        #in pairs
        new_strs = []
        anagrams = {}
        for i in strs:
    
            sorted_i =   ''.join(sorted(i))
            new_strs.append(sorted_i)

  #how do i pair them up
  #use a dictionary
            if sorted_i not in anagrams:
                anagrams[sorted_i] = []
            anagrams[sorted_i].append(i) 
  
  
  
    
    
  
        return list(anagrams.values())
        
        