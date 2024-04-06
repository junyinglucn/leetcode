class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        li_dict, ans = list(), list()
        for item in A:
            str_dict = dict()
            for i in item:
                str_dict[i] = str_dict.get(i, 0) + 1
            li_dict.append(str_dict)

        for j in set(A[0]):
            if all([j in x for x in li_dict[1:]]):
                num = min([y[j] for y in li_dict])
                ans.extend([j] * num)
        return ans
