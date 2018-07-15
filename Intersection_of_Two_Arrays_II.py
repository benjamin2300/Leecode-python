class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic1 = {}
        dic2 = {}
        #record dic1
        for n1 in nums1:
            if n1 in dic1:
                dic1[n1]+=1
            else:
                dic1[n1]=1
    
        for n2 in nums2:
            if n2 in dic2:
                dic2[n2]+=1
            else:
                dic2[n2]=1
        
        rl = []
        print dic1, dic2
        if len(dic1) > len(dic2):
            for i in dic2:
                if i in dic1:
                    if dic1[i] > dic2[i]:
                        for j in range(dic2[i]):
                            rl.append(i)
                    else:
                        for j in range(dic1[i]):
                            rl.append(i)
        else:
            for i in dic1:
                if i in dic2:
                    if dic1[i] > dic2[i]:
                        for j in range(dic2[i]):
                            rl.append(i)
                    else:
                        for j in range(dic1[i]):
                            rl.append(i)
        return rl