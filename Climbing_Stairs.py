class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        climb_dp = [1, 2]
        for i in range(n):
            if i!=0 and i!=1:
                climb_dp_i = climb_dp[i-1] + climb_dp[i-2]
                climb_dp.append(climb_dp_i)
        return climb_dp[n-1]