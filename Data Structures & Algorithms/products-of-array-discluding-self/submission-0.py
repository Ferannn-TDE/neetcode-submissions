class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        myAns = []
        for i,num in enumerate(nums):
            prod = 1
            j = 0
            while j < len(nums):
                if j != i:
                    prod *= nums[j]
                if j == len(nums) - 1:
                    myAns.append(prod)
                j+=1
            

        return myAns

