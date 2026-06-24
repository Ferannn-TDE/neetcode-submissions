class Solution:
    
    def encode(self, strs: List[str]) -> str:
        myStr = []
        for item in strs:
            myStr.append(str(len(item)) + "#" + item)
        
        return "".join(myStr)

    def decode(self, s: str) -> List[str]:
        myAns = []
        i = 0
        
        while i < len(s) :
            j = i

            while j < len(s) and s[j] != "#":
                j+=1

            length = int(s[i:j])

            word = s[j+1:j+length+1]

            myAns.append(word)

            i = j + length + 1

        return myAns




                
                


