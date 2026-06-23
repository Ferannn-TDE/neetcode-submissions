class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        myAns = []
        for num in nums:
            if num not in myDict :
                myDict[num] = 0
            myDict[num] += 1
        
        DictList = sorted(myDict.items(), key = lambda item: item[1], reverse=True)

        for num in range(k):
            myAns.append(DictList[num][0])
        
        return myAns




