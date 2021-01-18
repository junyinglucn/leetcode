class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        candidates.sort()
        res = []

        def dfs(i, tmp_sum, tmp_list):
            if tmp_sum == target:
                res.append(tmp_list)
                return
            if tmp_sum > target or i == len(candidates):
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                dfs(j + 1, tmp_sum + candidates[j], tmp_list + [candidates[j]])

        dfs(0, 0, [])
        return res
