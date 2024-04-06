class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(num, tmp):
            if not num:
                res.append(tmp)
                return
            for i in range(len(num)):
                backtrack(num[:i] + num[i + 1:], tmp + [num[i]])

        backtrack(nums, [])
        return res
