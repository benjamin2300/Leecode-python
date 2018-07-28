class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summon = 0
        record = [0] * len(nums)
        record[0] = nums[0]
        for i in range(1, len(nums)):
            record[i] = max(record[i-1]+nums[i], nums[i])
        print record
        return max(record)
                