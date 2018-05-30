class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        n = len(nums)
        for i in range(n):
            left = target - nums[i]
            if left in nums and nums.index(left)!=i:
                return [i, nums.index(left)]
        """
        dict = {}
        for i in range(len(nums)):
            x = nums[i]
            if target-x in dict:
                return (dict[target-x], i)
            dict[x] = i
