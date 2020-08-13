# Solution A
class Solution:
    def twoSum(self, numbers, target):
        if not numbers:
            return [0, 0]
        i = 0
        j = len(numbers) - 1
        while i < j:
            res = numbers[i] + numbers[j]
            if res == target:
                return [i + 1, j + 1]
            elif res < target:
                i += 1
            else:
                j -= 1
        return [0, 0]


# Solution B
class Solution:
    def twoSum(self, numbers, target):
        for i in range(len(numbers) - 1):
            num = target - numbers[i]
            left = i + 1
            right = len(numbers) - 1
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == num:
                    return [i + 1, mid + 1]
                elif numbers[mid] > num:
                    right = mid - 1
                else:
                    left = mid + 1
        return [0, 0]
