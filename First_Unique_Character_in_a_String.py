class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for c in s:
            if c in dic:
                dic[c]+=1
            else:
                dic[c] = 1
        
        index = 0
        print dic
        for c in s:
            if dic[c] == 1:
                return index
            else:
                index+=1
        return -1