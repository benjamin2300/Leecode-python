class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        cs = [0]*n
        
        if n==1:
            return True
        #check possible
        p = False
        for i in range(n-1):
            if i+nums[i] >= n-1:
                print i, nums[i], n-1
                p = True
        if not p:
            return False
        
        end = False
        ss = nums[0]
        cs[0] = 1
        su1 = 0
        su2 = sum(cs)
        print cs
        print nums
        while su1 != su2:
            su1 = su2
            for i in range(n):
                if cs[i] == 1:
                    cnum = nums[i]
                    #print cnum
                    for j in range(cnum):
                        if i+j+1 < n:
                            cs[i+j+1] = 1
                            if i+j+1 == n-1:
                                return True
            su2 = sum(cs)
            #print cs
        if cs[n-1] == 1:
            return True
        else:
            return False

