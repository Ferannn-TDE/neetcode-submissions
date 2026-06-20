class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        if len(s) != len(t) :
            return False
        for char in s:
            if my_dict.get(char) is None:
                my_dict[char] = 1;
            else:
                my_dict[char] += 1
        
        for char in t:
            if my_dict.get(char) is None:
                return False
            else:
                if my_dict[char] == 0 :
                    return False
                else :
                    my_dict[char] -= 1
        return True



        