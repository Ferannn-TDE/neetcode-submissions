class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myArray = []
        currGroup = []
        strs.sort(key = len)
        group = {}
        for item in strs :
            key = "".join(sorted(item))

            if key not in group:
                group[key] = []
            
            group[key].append(item)
        
        for item in group :
            myArray.append(group[item])

        return myArray

            

            



