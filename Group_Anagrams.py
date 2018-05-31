class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        for s in strs:
            sd = self.convertToDict(s)
            sdKey = self.toKey(sd.values())
            print sdKey
            if sdKey in res:
                res[sdKey].append(s)
            else:
                res[sdKey] = [s]
        return res.values()
        """
         anagrams = []
        checkDict = []

        for i in range(len(strs)):
            s = strs[i]
            sdict = self.convertToDict(s)
            if sdict in checkDict:
                a = anagrams[checkDict.index(sdict)]
                a.append(s)
            else:
                e = [s]
                anagrams.append(e)
                checkDict.append(sdict)
            
        return anagrams
        """
       
            
    def convertToDict(self, s):
        sdict = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 
                 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0,
                 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0,
                 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0,
                 'y':0, 'z':0 }
        for i in range(len(s)):
            sdict[s[i]] += 1
        return sdict
    
    def toKey(self, sd):
        return ''.join(str(i) for i in sd)
    
    def checkDictSame(self, dict1, dict2):
        #print dict1, dict2
        #print len(dict1)
        for key in dict1.keys():
            if dict1[key] != dict2[key]:
                return False
        return True