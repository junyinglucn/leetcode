import itertools
import collections

class Solution:
    def diagonalSort(self, mat):
        r = len(mat)
        c = len(mat[0])
        d = collections.defaultdict(list)
        for i, j in itertools.product(range(r), range(c)):
            d[i - j].append(mat[i][j])
        d = {k: iter(sorted(v)) for k, v in d.items()}
        for i, j in itertools.product(range(r), range(c)):
            mat[i][j] = next(d[i - j])
        return mat
