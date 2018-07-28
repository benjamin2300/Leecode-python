class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index = -1
        if haystack == '' and needle == '':
            return 0
    
        for i in range(0, len(haystack)-len(needle)+1):
            exist = True
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    exist = False
                    break
            if exist:
                index = i
                break
        return index