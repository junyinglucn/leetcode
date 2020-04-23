# solution A
class Solution:
    def allCellsDistOrder(self, R, C, r0, c0):
        d={}
        for i in range(R):
            for j in range(C):
                dis=abs(i-r0)+abs(j-c0)
                if dis in d:
                    d[dis].append([i,j])
                else:
                    d[dis]=[]
                    d[dis].append([i,j])
        out=[]
        for index in sorted(d.keys()):
            out.extend(d[index])
        return out

# solution B
class Solution:
    def allCellsDistOrder(self, R, C, r0, c0):
        out=[]
        for i in range(R):
            for j in range(C):
                out.append([i,j])
        out.sort(key=lambda x : abs(x[0]-r0)+abs(x[1]-c0))
        return out