class Solution:
    def isAnagram(self, s, t):
        ds={}
        dt={}
        for i in s:
            if ds.get(i):
                ds[i]+=1
            else:
                ds[i]=1
        for i in t:
            if dt.get(i):
                dt[i]+=1
            else:
                dt[i]=1
        if ds==dt:
            return True
        else:
            return False