class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        re = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[re] = nums[i]
                re += 1
        return re 
        