class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        q = 0
        rList = []
        digits[-1] += 1
        for i in range(len(digits)):
            digits[-1-i] = digits[-1-i] + q
            q = 0
            if digits[-1-i] <  10:
                break
            else:
                q = digits[-1-i] / 10 
                digits[-1-i] = digits[-1-i] % 10
                  
        print q     
        if q == 0:
            return digits
        else:
            rList.append(q)
            return rList + digits
        return digits