class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        chs = [0] * (len(nums)+1)
        for num in nums:
            chs[num] = 1
        
        for ch in chs:
            if ch == 0:
                return chs.index(ch)