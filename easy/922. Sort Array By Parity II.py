# solution A
class Solution:
    def sortArrayByParityII(self, A):
        r = [0] * len(A)
        o = 1
        e = 0
        for i in A:
            if i % 2 == 0:
                r[e] = i
                e += 2
            else:
                r[o] = i
                o += 2
        return r


# solution B:
class Solution:
    def sortArrayByParityII(self, A):
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2 == 1:
                while A[j] % 2 == 1:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A
