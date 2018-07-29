class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = []
        dp.append(0)
        dp.append(0)
        
        for i in range(2, len(cost)+1):
            dp.append(min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2]))
        print dp
        return dp[len(cost) ]