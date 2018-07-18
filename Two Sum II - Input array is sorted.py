class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = 0
        e = len(numbers) - 1
        
        while s < e:
            if numbers[s] + numbers[e] > target:
                e-=1
            elif numbers[s] + numbers[e] < target:
                s+=1
            else:
                return [s+1, e+1]