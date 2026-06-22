class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for item in strs :
            key = "".join(sorted(item))

            if key not in group:
                group[key] = []
            
            group[key].append(item)

        return list(group.values())

            

            



