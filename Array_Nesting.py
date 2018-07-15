class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        re = [0] * len(nums)
        length = 0
        for i in range(len(nums)):
            num = nums[i]
            l = 0
            index = i
            while re[index] == 0:
                l+=1
                re[index] = 1
                index = nums[index]
                #print index
            length = max(l, length)
        return length
                