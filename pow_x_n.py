class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = {}
        rx = 1
        k = 0

        rx *= x
        k += 1
        res[k] = rx
        print rx

        while k <= float(abs(n))/2:
            rx *= rx
            k *= 2
            res[k] = rx
            print rx
        keys = res.keys()
        print keys
        sortedKey = sorted(keys)[::-1]
        r = abs(n)
        rx = 1
        for i in range(len(sortedKey)):
            if r - sortedKey[i] >= 0:
                r -= sortedKey[i]
                rx *= res[sortedKey[i]]
                
        

        if n>0:
            return rx
        else:
            return 1/float(rx)
        