class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        
        count = 0
        found = False
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ':
                found = True
                count += 1
            elif s[i] == ' ' and found:
                break
        return count
            
        