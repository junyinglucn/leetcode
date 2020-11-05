class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        def findlast(aw, S):
            for i in range(len(S) - 1, -1, -1):
                if S[i] == aw:
                    return i

        def breakpoint(startidx):
            aw = -S[startidx]
            last = findlast(aw, S)

            j = startidx + 1
            while j < last:
                tmp = findlast(S[j], S)
                if tmp > last:
                    last = tmp
                j += 1

            output.append(last - startidx + 1)
            return last

        output = []
        startidx = 0
        while startidx < len(S):
            startidx = breakpoint(startidx) + 1
        return output
