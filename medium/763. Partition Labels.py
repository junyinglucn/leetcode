class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        def findlast(aw, S):
            for i in range(len(S) - 1, -1, -1):
                if S[i] == aw:
                    return i

        def breakpoint(startindex):
            aw = S[startindex]
            last = findlast(aw, S)

            j = startindex + 1
            while j < last:
                temp = findlast(S[j], S)
                if temp > last:
                    last = temp
                j += 1

            output.append(last - startindex + 1)
            return last

        output = []
        startindex = 0
        while startindex < len(S):
            startindex = breakpoint(startindex) + 1
        return output
