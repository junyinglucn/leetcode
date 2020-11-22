class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        p = 0
        while p < n - 3:
            if nums[p] + 3 * nums[p + 1] > target:
                break
            if nums[p] + 3 * nums[-1] < target:
                while p < n - 4 and nums[p] == nums[p + 1]:
                    p += 1
                p += 1
                continue
            k = p + 1
            while k < n - 2:
                if nums[p] + nums[k] + 2 * nums[k + 1] > target:
                    break
                if nums[p] + nums[k] + 2 * nums[-1] < target:
                    while k < n - 3 and nums[k] == nums[k + 1]:
                        k += 1
                    k += 1
                    continue
                i = k + 1
                j = n - 1
                new_target = target - nums[p] - nums[k]
                while i < j:
                    if nums[i] + nums[j] > new_target:
                        j -= 1
                    elif nums[i] + nums[j] < new_target:
                        i += 1
                    else:
                        res.append([nums[p], nums[k], nums[i], nums[j]])
                        i += 1
                        j -= 1
                        while i < j and nums[i] == nums[i - 1]:
                            i += 1
                        while i < j and nums[j] == nums[j + 1]:
                            j -= 1
                while k < n - 3 and nums[k] == nums[k + 1]:
                    k += 1
                k+=1
            while p < n - 4 and nums[p] == nums[p + 1]:
                p += 1
            p += 1
        return res
