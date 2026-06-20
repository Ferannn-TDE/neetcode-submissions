class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for i,num in enumerate(nums):
            if my_dict.get(num) is not None:
                return True
            else:
                my_dict[num] = i
        return False
    

        