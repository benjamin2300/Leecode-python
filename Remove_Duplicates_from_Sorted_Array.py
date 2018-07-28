class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        re = 0
        p = -1000
        for i in range(len(nums)):
            if p != nums[i]:
                nums[re] = nums[i]
                p = nums[i]
                re += 1
        return re
        