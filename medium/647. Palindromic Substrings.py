# Solution A
class Solution:
    def countSubstrings(self, s):
        count=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                char=s[i:j+1]
                if char==char[::-1]:
                    count+=1
        return count

# Solution B
