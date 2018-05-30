class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        if num1 == '0' or num2 == '0':
            return "0"
        
        l1 = len(num1)
        l2 = len(num2)
        mm = []
        tl = l1 + l2 
        tz = tl - l2
        for i in range(l1):
            for zz in range(i):
                mm.append(0)
            for j in range(l2):
                m = int(num1[i])*int(num2[j])
                mm.append(m)
            for zz in range(tz-i):
                mm.append(0)
       # print mm
        q=0
        r=0
        am = []
        for i in range(tl):
            a = 0
            for j in range(l1):
                a += mm[i+j*tl]
            a += q
            q = a / 10
            r = a % 10
            am.append(str(r))
        
        am = am[::-1]

        if am[0] == '0':
            am = am[1:]

        
       
                
        return ''.join(am)
            