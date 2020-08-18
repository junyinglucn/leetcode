# solution A
class Solution:
    def relativeSortArray(self, arr1, arr2):
        d = {}
        out = []
        dif = []
        for i in arr1:
            if i in arr2:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
            else:
                dif.append(i)
        dif.sort()
        for i in arr2:
            out += [i] * d[i]
        out = out + dif
        return out


# solution B
class Solution:
    def relativeSortArray(self, arr1, arr2):
        count = [0] * 1001
        out = []
        dif = []
        for i in arr1:
            count[i] += 1
        for i in arr2:
            out += [i] * count[i]
            count[i] = 0
        for i in range(1001):
            if count[i] > 0:
                dif += [i] * count[i]
        out = out + dif
        return out
